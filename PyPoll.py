#adding dependencies
import csv
import os

#assigning a variable for the file to load
file_to_load = os.path.join("Resources", "election_results.csv")

#assign var to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialise the total vote counter
total_votes = 0

#new  list of candidates names
candidate_options = []

#empty dictionary to count each candidates votes
candidate_votes = {}

#winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open election_results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #print the header row - basically ignore this row and get to the data
    headers = next(file_reader)

    #print each row in the CSV file (excluding the header)
    for row in file_reader:
        total_votes = total_votes + 1
        #get candidate name from each row
        candidate_name = row[2]
        #if candidate does not match any exissting candidate..
        if candidate_name not in candidate_options:
            #add candidate name to candidate list
            candidate_options.append(candidate_name)
            #begin tracking that candidate's votes
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
    #determine the % votes for each candidate by looping through the counts
    for candidate_name in candidate_votes:
        #retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        #calculate % vote
        vote_percentage = round(float(votes)/float(total_votes) * 100 ,1)
        #NO LONGER NEEDED: print(f"{candidate_name}: received {vote_percentage}% of the vote.")

        #determing winning candidate
        if(votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes: ,})\n")

#print winning candidate
winning_candidate_summary = (
    f"------------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage}%\n"
    f"------------------------------\n")
print(winning_candidate_summary)


#print(candidate_votes)



#1. the total number of votes cast
#2. a complete list of candidates who received votes
#3. % of votes each candidate won
#4. total number of votes each candidate won
#5. winner of the election based on popular vote
