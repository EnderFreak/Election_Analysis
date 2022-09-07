#adding dependencies
import csv
import os

#assigning a variable for the file to load
file_to_load = os.path.join("Resources", "election_results.csv")

#assign var to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#open election_results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #print the header row
    headers = next(file_reader)
    print(headers)
    #print each row in the CSV file
    #for row in file_reader:
     #   print(row)



#1. the total number of votes cast
#2. a complete list of candidates who received votes
#3. % of votes each candidate won
#4. total number of votes each candidate won
#5. winner of the election based on popular vote
