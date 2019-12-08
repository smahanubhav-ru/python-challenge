#PyPoll
import os
import csv

# Get file path
os.chdir(os.path.dirname(os.path.abspath(__file__)))
csvpath = os.path.join('.', 'Resources', 'election_data.csv')
txtpath = os.path.join('.', 'Resources', 'pypoll.txt')

# Declare variables, set default values
total_vote_count = 0

candidate_list = []
candidate_vote_count = {}

candidate_name = []
candidate_vote_percent = []
candidate_vote_total = []

# Read file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    # Loop through each row
    for row in csvreader:
        # Calculate Total Votes
        total_vote_count = total_vote_count + 1

        # Populate values        
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            candidate_vote_count[row[2]] = 0
        candidate_vote_count[row[2]] += 1

# Calculate the winner
winner = max(candidate_vote_count, key=candidate_vote_count.get)

# Calculate result for each candidate
for key,value in candidate_vote_count.items():
    candidate_name.append(key)
    candidate_vote_total.append(value)

for item in candidate_vote_total:
    candidate_vote_percent.append(round(item/total_vote_count*100,1))

result = list(zip(candidate_name,candidate_vote_percent,candidate_vote_total))

# Print the analysis to the terminal
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_vote_count))
print("-------------------------")

for item in result:
    print(item[0] + ": " + str("%.3f" % item[1]) + "% (" + str(item[2]) + ")")

print("-------------------------")
print("Winner: " + str(winner))
print("-------------------------")

# Export results to text file
with open(txtpath, mode='w', newline='') as txtfile:
    txtfile.writelines("Election Results"+"\n")
    txtfile.writelines("-------------------------"+"\n")
    txtfile.writelines("Total Votes: " + str(total_vote_count)+"\n")
    txtfile.writelines("-------------------------"+"\n")

    for item in result:
        txtfile.writelines(item[0] + ": " + str("%.3f" % item[1]) + "% (" + str(item[2]) + ")"+"\n")

    txtfile.writelines("-------------------------"+"\n")
    txtfile.writelines("Winner: " + str(winner)+"\n")
    txtfile.writelines("-------------------------"+"\n")