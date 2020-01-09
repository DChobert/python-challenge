import os
import csv

Pypollcsv = os.path.join('Pypoll','election_data.csv')

total_votes = 0
candidates_unique = []
candidate_votes = []

with open(Pypollcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        total_votes += 1
        candidate = (row[2])
        
        if candidate in candidates_unique:
            candidate_list = candidates_unique.index(candidate)
            candidate_votes[candidate_list] = candidate_votes[candidate_list] + 1
        else:
            candidates_unique.append(candidate)
            candidate_votes.append(1)

percentage = []
max_votes = candidate_votes[0]
max_index = 0

for x in range(len(candidates_unique)):
    vote_pct = round(candidate_votes[x]/total_votes*100, 2)
    percentage.append(vote_pct)
    
    if candidate_votes[x] > max_votes:
        max_votes = candidate_votes[x]
        max_index = x

winner = candidates_unique[max_index] 


print()
print('Election Results')
print()
print(f'Total Votes: {total_votes}')
print()
for x in range(len(candidates_unique)):
    print(f'{candidates_unique[x]} : {percentage[x]}% ({candidate_votes[x]})')
print()
print(f'Election winner: {winner.upper()}')
print()


#output txt file
output_file = os.path.join("pypoll_election_results.txt")
with open(output_file, "w", newline="") as datafile:
    datafile.write('\n')
    datafile.write('ELECTION RESULTS')
    datafile.write('\n')
    datafile.write(f'Total Votes: {total_votes}\n')
    datafile.write('\n')
    for x in range(len(candidates_unique)):
        datafile.write(f'{candidates_unique[x]} : {percentage[x]}% ({candidate_votes[x]})\n')
    datafile.write('\n')
    datafile.write(f'ELECTION WINNER: {winner.upper()}\n')
    datafile.write('\n')
   
