import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if not (sys.argv[1].endswith(".csv")):
        sys.exit("Not a CSV file")

    try:
        with open(sys.argv[1]) as file_r:
            reader = csv.DictReader(file_r)

            with open(sys.argv[2], "w") as file_w:
                writer = csv.DictWriter(file_w, fieldnames = ["first", "last", "house"])
                writer.writeheader()

                for row in reader:
                    last, first = row["name"].split(",")
                    house = row["house"]
                    writer.writerow({"first" : first.strip(), "last": last.strip(),"house": house })

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

if __name__ == "__main__":
    main()