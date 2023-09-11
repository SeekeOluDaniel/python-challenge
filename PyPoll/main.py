import os
import csv

# Specify the file path
election_path = "Resources\election_data.csv"

# Create Sets as needed
Candidate_Names = set()

# Create Lists as needed
# vote_count = []

# Open file and read
with open(election_path, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csvheader = next(csvreader)

# Define variables to be iterated over
    rowcount = 0
         

    for row in csvreader:
        rowcount = rowcount + 1
        candidate = row[2]
        
        if candidate != None and candidate != " ":
            if candidate not in Candidate_Names:
                Candidate_Names.add(candidate)

        
print(f"Total Votes: ", rowcount)
print(Candidate_Names)




