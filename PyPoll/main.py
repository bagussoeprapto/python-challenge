import os
import csv

#set counter
khan = 0
correy = 0
li = 0
tool = 0

#import csv file
with open('election_data.csv', 'r') as csv_file:
    data = csv.reader(csv_file, delimiter=",")
    
    #count candidates
    for row in data:
        if row[2] == "Khan":
            khan += 1

        if row[2] == "Correy":
            correy += 1

        if row[2] == "Li":
            li += 1
    
        if row[2] == "O'Tooley":
            tool += 1

print(khan)
print(correy)
print(li)
print(tool)

votes = [(khan),(correy),(li),(tool)]
print(max(votes))

#determine count of votes in rows (total_votes)
total_votes = sum(1 for line in open('election_data.csv')) - 1
print(total_votes)

#determine percentages
khan_percent = khan/total_votes
correy_percent = correy/total_votes
li_percent = li/total_votes
tool_percent = tool/total_votes

#print result
print("Election Results")
print("-------------------------")
print("Total Votes: " + "{:,}".format(total_votes))
print("-------------------------")
print("Khan: " + "{:.0%}".format(khan_percent) +" (" + "{:,}".format(khan) + ")")
print("Correy: " + "{:.0%}".format(correy_percent) +" (" + "{:,}".format(correy) + ")")
print("Li: " + "{:.0%}".format(li_percent) +" (" + "{:,}".format(li) + ")")
print("O'Tooley: " + "{:.0%}".format(tool_percent) +" (" + "{:,}".format(tool) + ")")
print("-------------------------")
print("Winner: Khan")
print("-------------------------")     