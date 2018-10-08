# Modules
import os
import csv

#set path for file
csvpath = os.path.join("..", "pypoll", "Resources", "election_data_csv")

# set variables
total_votes = 0
candidate =""
candidate_list = []
vote_list = []
percent_list = []
winner = ""

# open the csv
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvreader)

    #read each row of data after the header
    for row in csvreader:
        # count the total number of months
        total_votes += 1

        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            vote_list.append(1)
        else:
            vote_list[candidate_list.index(row[2])] += 1

            # calculate percent of vote
            percent_list + [(100/total_votes) * x in vote_list]

            # Find the winner
            winner = candidate_list[vote_list.index(max(vote_list))]

            # Print the analysis to terminal
            print("Election Results")
            print("-----------------------")
            print("Total Votes: " + str(total_votes))
            print("-------------------")

            for x in candidate_list:
                print(x + ":" + str(format(percent_list[candidate_list.index(x)], '.3f') + "% (" + str(vote_list[candidate_list.index(x)])) + ")")

                f.write("-----------------------------------\n")
                f.write("winner: " + "\n")
                f.writer("------------------------\n")
                
                f.close()
                




]