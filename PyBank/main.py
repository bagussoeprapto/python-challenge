import os
import csv

#import csv file
csvpath = os.path.join('budget_data.csv')
with open(csvpath,newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')

#determine count of months in rows (total_months)
total_months = sum(1 for line in open('budget_data.csv')) - 1


#determine variables to run loops
first = 0
variance = []

total_profit = 0.
profit_losses = []

#import csv file
with open(csvpath,newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    header = next(csvreader)

    #determine total profit by appending the rows (total_profit)
    #determine % variance of values in rows (average_change) 
    for row in csvreader:
        total_profit += float(row[1])
        profit_losses.append(float(row[1]))

for i in range(0, len(profit_losses)):
    
    variance.append((profit_losses[i] - first)/profit_losses[i])
    first = profit_losses[i]

average_change = ((sum(variance)/(len(variance))))*100

#determine max and min from the list (max_profit & min_profit)
max_profit = max(profit_losses)
min_profit = min(profit_losses)

#print result
print("-----------------------------------------")
print("Financial Analysis")
print("-----------------------------------------")

print("Total Months: "+ str(total_months))
print("Total Profits: "+ "${:,.0f}".format(total_profit))
print("Average Change: "+ "{:.2f}%".format(average_change))
print("Greatest Increase in Profits: "+ "${:,.0f}".format(max_profit))
print("Greatest Decrease in Profits: "+ "${:,.0f}".format(min_profit))
