import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    evidence = list()
    labels = list()

    reader = csv.DictReader(open(filename))
    for row in reader:
        buffer_evidence = list()
        buffer_evidence.append(int(row["Administrative"]))
        buffer_evidence.append(float(row["Administrative_Duration"]))
        buffer_evidence.append(int(row["Informational"]))
        buffer_evidence.append(float(row["Informational_Duration"]))
        buffer_evidence.append(int(row["ProductRelated"]))
        buffer_evidence.append(float(row["ProductRelated_Duration"]))
        buffer_evidence.append(float(row["BounceRates"]))
        buffer_evidence.append(float(row["ExitRates"]))
        buffer_evidence.append(float(row["PageValues"]))
        buffer_evidence.append(float(row["SpecialDay"]))
        #Month matchs with
        #match row["Month"]:
        if row["Month"] == 'Jan': buffer_evidence.append(0)
        if row["Month"] == 'Feb': buffer_evidence.append(1)
        if row["Month"] == 'Mar': buffer_evidence.append(2)
        if row["Month"] == 'Apr': buffer_evidence.append(3)
        if row["Month"] == 'May': buffer_evidence.append(4)
        if row["Month"] == 'June': buffer_evidence.append(5)
        if row["Month"] == 'Jul': buffer_evidence.append(6)
        if row["Month"] == 'Aug': buffer_evidence.append(7)
        if row["Month"] == 'Sep': buffer_evidence.append(8)
        if row["Month"] == 'Oct': buffer_evidence.append(9)
        if row["Month"] == 'Nov': buffer_evidence.append(10)
        if row["Month"] == 'Dec': buffer_evidence.append(11)
        #End of month match
        buffer_evidence.append(int(row["OperatingSystems"]))
        buffer_evidence.append(int(row["Browser"]))
        buffer_evidence.append(int(row["Region"]))
        buffer_evidence.append(int(row["TrafficType"]))
        buffer_evidence.append(1) if row["VisitorType"] == "Returning_Visitor" else buffer_evidence.append(0)
        buffer_evidence.append(1) if row["Weekend"] == "TRUE" else buffer_evidence.append(0)

        evidence.append(buffer_evidence)
        labels.append(1) if row["Revenue"] == "TRUE" else labels.append(0)
    #print(evidence[0])
    #print(labels[0])
    return (evidence, labels)
    #raise NotImplementedError


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    model = KNeighborsClassifier(n_neighbors=1)
    model.fit(evidence, labels)

    return model
    #raise NotImplementedError


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    sensitivity = 0
    specificity = 0
    tot_true = 0
    tot_false = 0

    for val in zip(labels, predictions):
        if val[0] == 1:
            if val[0]==val[1]: sensitivity += 1
            tot_true += 1
        else:
            if val[0]==val[1]: specificity += 1
            tot_false += 1

    sensitivity /= tot_true
    specificity /= tot_false

    return (sensitivity, specificity)
    #raise NotImplementedError


if __name__ == "__main__":
    main()
