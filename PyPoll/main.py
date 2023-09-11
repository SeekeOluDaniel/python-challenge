import os
import csv

# Specify the file path
election_path = "Resources\election_data.csv"

# Create Sets as needed
candidate_options = []
candidate_votes = {}

# Open file and read
with open(election_path, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csvheader = next(csvreader)

# Define variables to be iterated over
    rowcount = 0 

    for row in csvreader:
        rowcount = rowcount + 1
        candidate = row[2]

        if candidate not in candidate_options:
            candidate_options.append(candidate)
            candidate_votes[candidate] = 0
        candidate_votes[candidate] = candidate_votes[candidate] + 1

    print(f"Total Votes: ", rowcount)

    total_votes = float(369711)
    winning_count = 0
    
    for candidate in candidate_votes:

        votes = candidate_votes.get(candidate)
        percentage_won = float(votes) / float(total_votes) * 100       
        
        vote_results = f"{candidate}: {round(percentage_won, 3)}% ({votes})\n"
        print(vote_results)

        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
    
print(f"The winner is: " + winning_candidate)

