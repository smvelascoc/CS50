import nltk
import sys
import os
import string
from numpy import log

FILE_MATCHES = 1
SENTENCE_MATCHES = 1


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """
    files_dict = dict()
    with os.scandir(directory) as files:
        for file in files:
            files_dict[file.name] = open(file).read()

    return files_dict
    #raise NotImplementedError


def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """
    tokens = nltk.tokenize.word_tokenize(document)
    tokens_filter = [word.lower() for word in tokens]

    #nltk.download('stopwords')
    for word in tokens:
        if (word.lower() in string.punctuation) or (word.lower() in nltk.corpus.stopwords.words("english")):
            tokens_filter.remove(word.lower())

    return tokens_filter
    #raise NotImplementedError


def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """
    idfs = dict()
    #Collect each word in all documents
    for document in documents:
        for word in documents[document]:
            if word not in idfs: idfs[word]=0

    #Count the documents in wich each word appears
    for word in idfs:
        for document in documents:
            if word in documents[document]: idfs[word]+=1

    #Compute idfs
    for word in idfs:
        idfs[word]=log(len(documents)/idfs[word])

    return idfs
    #raise NotImplementedError


def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """
    top_list = dict()

    #Performing the tf_idfs for all documents
    for document in files:
        #Starting at 0
        top_list[document] = 0

        #Performs tf_idfs
        for word_q in query:
            tf_idfs = 0
            if word_q in idfs:
                # Counting the frequency of the word in document
                tf = 0
                for word_d in files[document]:
                    if word_d == word_q: tf += 1
                # Performing tf_idfs
                tf_idfs = tf * idfs[word_q]

            top_list[document] += tf_idfs

    top_list = sorted(top_list.items(), key=lambda item: item[1], reverse=True)

    #Create the list to return
    top_filter = list()

    t=0
    for key in top_list:
        t += 1
        if t > n:
            break
        else:
            top_filter.append(key[0])

    return top_filter
    #raise NotImplementedError


def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """
    top_sent = dict()
    #print(sentences)
    for sentence in sentences:
        top_sent[sentence] = dict()
        top_sent[sentence]["match"] = 0
        top_sent[sentence]["density"] = 0
        #Perform the matching computation
        for word_q in query:
            if word_q in sentences[sentence]: top_sent[sentence]["match"] += idfs[word_q]
        # Perform density measuer
        for word_s in sentences[sentence]:
            if word_s in query: top_sent[sentence]["density"] += 1/len(sentences[sentence])

    #print(top_sent)
    top_sent = sorted(top_sent.items(), key = lambda item: (item[1]["match"], item[1]["density"]), reverse = True)
    #print(f"Sorted list {top_sent}")
    #input()

    t=0
    top_list = list()
    for key in top_sent:
        #print(key)
        t += 1
        if t > n:
            break
        else:
            top_list.append(key[0])

    return top_list
    #raise NotImplementedError


if __name__ == "__main__":
    main()
