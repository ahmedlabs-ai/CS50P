import sys
import csv

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)

        rows = []
        for row in reader:
            split_name = row["name"].split(", ")
            row["first"] = split_name[1]
            row["last"] = split_name[0]
            del row["name"]
            rows.append(row)
    with open(sys.argv[2], "w")as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")