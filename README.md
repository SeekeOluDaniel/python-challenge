# python-challenge
 Week 3 Challenge Assignment
For the PyBank Challenge, here are my steps:
#1  Specify the location of the file
#2  Open file and read using csv.reader
#3  Skip header row as it is not needed
#4  Define variables
#5  Use for loop to determine the number of rows in the file (minus the header)
#6  Also use for loop to sum up the total profits for the period
#7  Calculate change from month to month, starting from month 2. Note that change will not be calculated for  month 1 because there is no prior data.
#8  Calculate average change which is total change divided by 85 months
#9  Iterate through each row to calculate greatest increase and greatest decrease in profits. Reset previous row to be the new starting point
#10 Display all the calculated results


For the PyPoll Challenge, these were my steps:
#1  Specify the location of the file
#2  Open file and read using csv.reader
#3  Skip header row as it is not needed
#4  Define variables
#5  Use for loop to determine the number of rows in the file (minus the header)
#6  Print out list of candidates who received votes

I had created a set to get the candidate options and was able to print out the complete list of candidates who received votes. However I got stumped by how to get the total number of votes that each candidate won. I reached out to a Learning Assistant who helped to clarify this by providing these lines of code which made my code for the complete list of candidates that received votes redundant:

candidate_options = []
candidate_votes = {}

if candidate not in candidate_options:
            candidate_options.append(candidate)
            candidate_votes[candidate] = 0
        candidate_votes[candidate] = candidate_votes[candidate] + 1

#7 I calculated the percentage won by each candidate but got stumped trying to print it out as shown in the output example for each candidate. Another Learning Assistant helped by providing these lines:

winning_count = 0
    
    for candidate in candidate_votes:

        votes = candidate_votes.get(candidate)

                if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

    I adapted these lines to suit my code, so the variables are mine: 
    vote_results = f"{candidate}: {round(percentage_won, 3)}% ({votes})\n"
        print(vote_results)