import os
import csv

infile = os.path.join("Resources_PyPoll", "election_data.csv")
outfile = os.path.join("Analysis", "election_results.txt")

# set parameters

# total votes
total_votes = 0
winning_candidate_votes = 0

# votes for candidates
candidate_list = []
candidate_votes = {}
winning_candidate = ""

with open(infile, 'r') as election_data:
    csv_reader = csv.reader(election_data)
    # check the header
    header = next(csv_reader)
    # print(header)

    # start the loop
    for row in csv_reader:

        # designate the names
        candidate_name = row[2]

        # running total for votes
        total_votes += 1

        # if the name isn't in the list, add to list and set the votes of new entry to zero
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            candidate_votes[candidate_name] = 0

            # add a vote to the corresponding candidate
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

# complete operation for tabulating under the with statement to save text files with less hassle
with open(outfile, 'w') as txt_file:

    # print to terminal - make it look like the ReadME
    election_results = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n"
    )
    print(f"{election_results}")
    # save the file
    txt_file.write(election_results)

    # loop through counts to compare values and decide the winner
    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percent = round(float(votes) / float(total_votes) * 100, 2)
        # print(candidate_votes)
        # compare vote values and end the loop w/ the largest value
        if votes > winning_candidate_votes:
            winning_candidate_votes = votes
            winning_candidate = candidate
        # simple layout to follow the README
        candidate_count = (f"{candidate}: {vote_percent}% ({votes})\n")
        print(f"{candidate_count}")

        txt_file.write(candidate_count)

    voting_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n"
         )
    print(f"{voting_summary}")

    txt_file.write(voting_summary)
