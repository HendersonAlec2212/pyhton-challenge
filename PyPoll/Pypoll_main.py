import os
import csv

#   * The total number of votes cast
#
#   * A complete list of candidates who received votes
#
#   * The percentage of votes each candidate won
#
#   * The total number of votes each candidate won
#
#   * The winner of the election based on popular vote.
#
# * As an example, your analysis should look similar to the one below:


# Thoughts - to be deleted --------------------------------------------------------------------------
# import the files to be read
# export the files to be written
# use empty string for winning candidate name
# differentiate the votes per candidate by using dictionary and having one of the values to be the key,
# candidate name maybe?

# Count the votes
# list candidates hint:list

# % votes for each candidate & total number votes won

# winner based on greatest number of votes


# if value in (row[2]) = khan then khan_vote =+1
# elseif value = Li them +=1
# else if O'Tooley
# elseif Correy


# ----------------------------------------------------------------------------------------------------
infile = os.path.join("Resources_PyPoll", "election_data.csv")
outfile = os.path.join("PyPoll", "Analysis")

# set parameters

# total votes
total_votes = 0
winning_candidate_votes = 0

# votes for candidates
candidate_list = []
candidate_votes = {}
winning_candidate = ""

with open(infile) as election_data:
    csv_reader = csv.reader(election_data)
    # check the header
    header = next(csv_reader)
    print(header)

    # start the loop
    for row in csv_reader:

        # designate the names
        candidate_name = row[2]

        # running total for votes
        total_votes += 1

        # if the name isnt in the list, add to list and set the votes of new entry to zero
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            candidate_votes[candidate_name] = 0
        else:
            candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1


