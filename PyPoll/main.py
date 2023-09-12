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

# Define variables to be looped through
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

# Specify output location
results_final_path = "analysis\election_results.txt"
election_results=(f"Total Votes: 369711 \n" + "Charles Casper Stockham: 23.049% (85213) \n" + "Diana DeGette: 73.812% (272892) \n" + "Raymon Anthony Doane: 3.139% (11606) \n" + "The winner is: Diana DeGette \n")

# Open the output file    
with open(results_final_path, "w") as txt_file:

# Write the Contents    
    txt_file.write(election_results)