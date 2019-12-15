import os
import csv

total_vote = 0
popular_vote = 0
winner = None

# Set path for file
path = "C:/Users/Admin/Documents/UofA-PHX-DATA-PT-11-2019-U-C/03-Python/Homework/Instructions/PyPoll/Resources"
filename = "election_data.csv"
csv_file_path = os.path.join(path, filename)

with open(csv_file_path, 'r') as csv_file:
    csv_read = csv.reader(csv_file,delimiter=',')
    csv_list = list(csv_read)


# The total number of votes cast
    ## length of list minus the header
vote_count = len(csv_list) - 1
print(vote_count)


# creating an empty dictionary
vote_dict = {}


# A complete list of candidates who received votes
# The total number of votes each candidate won
    ## loop to find out all the possible list of candidates
for i in csv_list[1:]:
    candidate_key = i[2]
    if candidate_key in vote_dict:
        vote_dict[candidate_key] = vote_dict[candidate_key] + 1
    else:
        vote_dict[candidate_key] = 1

print(vote_dict)


# The percentage of votes each candidate won
for key in vote_dict:
    dict_value = vote_dict[key]
    vote_percentage = dict_value / vote_count
    print(key, dict_value, round(vote_percentage, 2))

# The winner of the election based on popular vote
    if dict_value > popular_vote:
        popular_vote = dict_value
        winner = key
print(winner)
