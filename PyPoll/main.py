# Reads election data from csv and outputs following: 
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.
#
# Kirsteen Lugtu 18-Sep-2021

import os
import csv

totalVotes = 0
totalCandList =[]
pollStat=[]
winnerCount = 0
winnerCand = ''

poll_csv = os.path.join("Resources", "election_data.csv")

with open(poll_csv, encoding='utf-8-sig') as csv_file:

    #instantiate a csv reader
    csv_reader = csv.reader(csv_file, delimiter = ',')

    # skip header
    header=next(csv_reader)

    # read in candidate column and put in list
    for row in csv_reader:

        totalVotes += 1
        candidate = row[2]
        totalCandList.append(candidate)

# find unique candidate names
uniqueList = set(totalCandList)

uniqueCand=[]
for i in uniqueList:
    uniqueCand.append(i)

# calculate poll stats
for cand in uniqueCand:
    
    # counts # of votes for each candidate
    voteCount=totalCandList.count(cand)
    
    # percent of votes for each candidate
    percent=round((voteCount/totalVotes*100), 2)

    # list of candidates and their corresponding vote count, percentage
    pollStat.append([cand,voteCount,percent])
    
    # find max count, winner
    if voteCount > winnerCount:
        winnerCount = voteCount
        winnerCand = cand

# print results
print('Election Results')
print('-------------------------')
print(f'Total Votes: {totalVotes}')
print('-------------------------')  

# print sorted list of candidates by vote count
pollStat.sort(key = lambda x:x[1])
for cnd in pollStat:
    print(f'{cnd[0]}: {cnd[2]}% ({cnd[1]})')

print('-------------------------')
print(f'Winner: {winnerCand}')
print('-------------------------')


# write output to text file
output_path = os.path.join("analysis", "PyPollOutput.txt")

with open(output_path, 'w') as txtfile:
    txtfile.write('Election Results \n')
    txtfile.write('------------------------- \n')
    txtfile.write(f'Total Votes: {totalVotes} \n')
    txtfile.write('------------------------- \n')  

    for cnd in pollStat:
        txtfile.write(f'{cnd[0]}: {cnd[2]}% ({cnd[1]}) \n')

    txtfile.write('------------------------- \n')
    txtfile.write(f'Winner: {winnerCand} \n')
    txtfile.write('------------------------- \n')