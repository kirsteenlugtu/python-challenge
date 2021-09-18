# Python script that analyzes the records to calculate each of the following:
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period
# K Lugtu 18-Sep-2021


import os
import csv

bank_csv = os.path.join("Resources", "budget_data.csv")

with open(bank_csv, encoding='utf-8-sig') as csv_file:

    #instantiate a csv reader
    csv_reader = csv.reader(csv_file, delimiter = ',')

    header=next(csv_reader)

    totalMos = 0
    netTot = 0
    maxProf = 0
    maxLoss = 0

    for row in csv_reader:
        totalMos += 1
        
        profLoss = row[1]
        profLoss = int(profLoss)

        # calculate net total profit/losses
        netTot += profLoss

        # find max
        if profLoss > maxProf:
            maxProf = profLoss
            maxProfDate = row[0]
        
        #find min
        if profLoss < maxLoss:
            maxLoss = profLoss
            maxLossDate = row[0]

    # average
    avgChange = int(netTot/totalMos)

# Print to terminal
print(f'Financial Analysis')
print(f'----------------------------')
print(f'Total Months: {totalMos}')
print(f'Total: ${netTot}')
print(f'Average Change: $ {avgChange}')
print(f'Greatest Increase in profits: {maxProfDate} $({maxProf})')
print(f'Greatest Decrease in profits: {maxLossDate} $({maxLoss})')

# Specify the file to write to
output_path = os.path.join("analysis", "PyBankOutput.txt")

with open(output_path, 'w') as txtfile:

    txtfile.write('Financial Analysis \n')
    txtfile.write(f'---------------------------- \n')
    txtfile.write(f'Total Months: {totalMos} \n')
    txtfile.write(f'Total: ${netTot} \n')
    txtfile.write(f'Average Change: $ {avgChange} \n')
    txtfile.write(f'Greatest Increase in profits: {maxProfDate} $({maxProf}) \n')
    txtfile.write(f'Greatest Decrease in profits: {maxLossDate} $({maxLoss}) \n')






