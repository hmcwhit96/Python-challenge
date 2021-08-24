<<<<<<< HEAD
# import modules

import os
import csv



# establish file path
file = r"C:\Users\hmwhi\OneDrive\Documents\GitHub\Python-challenge\PyPoll\Resources\election_data.csv"

# define columns
voter_id = []
candidate = []

# open & read csv, dictate column indexes
with open(file, newline="",encoding="utf-8") as csvfile:

    csvreader = csv.reader(csvfile,delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        voter_id.append(row[0])
        candidate.append(row[2])
        



# count number of voters

total_votes = len(voter_id)
#print(total_votes)



# establish variables for each candidate

khan = []
correy = []
li = []
otooley = []

for i in range(0,len(candidate)):
    if candidate[i] == "Khan":
        khan.append(i)
    elif candidate[i] == "Correy":
        correy.append(i)
    elif candidate[i] == "Li":
        li.append(i)
    elif candidate[i] == "O'Tooley":
        otooley.append(i)



# calculate each candidates' vote percentage
khan_percent = (len(khan)/total_votes) * 100
print(khan_percent)
correy_percent = (len(correy)/total_votes) * 100
print(correy_percent)
li_percent = (len(li)/total_votes) * 100
print(li_percent)
otooley_percent = (len(otooley)/total_votes) * 100
#print(otooley_percent)



# clean up values
khan_votes = (len(khan))
correy_votes = (len(correy))
li_votes = (len(li))
otooley_votes = (len(otooley))

khan_percent = "{:.2f}".format(khan_percent)
correy_percent = "{:.2f}".format(correy_percent)
li_percent = "{:.2f}".format(li_percent)
otooley_percent = "{:.2f}".format(otooley_percent)

#print(khan_percent,correy_percent,li_percent,otooley_percent)



# calculate the winner
candidates_dict = dict()

candidates_dict = {
    "Khan":{khan_percent},
    "Correy":{correy_percent},
    "Li":{li_percent},
    "O'Tooley":{otooley_percent}
}

winner = max(candidates_dict, key=candidates_dict.get)
#print(winner)



# final print
l1 = ("Election Results")
l2 = ("--------------------------")
l3 = (f"Total Votes: {total_votes}")
l4 = ("--------------------------")
l5 = (f"Khan: {khan_percent}% ({khan_votes})")
l6 = (f"Correy: {correy_percent}% ({correy_votes})")
l7 = (f"Li: {li_percent}% ({li_votes})")
l8 = (f"O'Tooley: {otooley_percent}% ({otooley_votes})")
l9 = ("--------------------------")
l10 = (f"Winner: {winner}")
l11 = ("--------------------------")

election_results = open(r"C:\Users\hmwhi\OneDrive\Documents\GitHub\Python-challenge\PyPoll\Analysis\election_results.txt","w")
election_results.write(("%s \n %s \n %s \n %s \n %s \n %s \n %s \n %s \n %s \n %s \n %s \n" % (l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11)))

print_analysis = [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11]
for line in print_analysis:
    print(line)


=======
# import modules

import os
import csv



# establish file path
file = r"C:\Users\hmwhi\OneDrive\Documents\GitHub\Python-challenge\PyPoll\Resources\election_data.csv"

# define columns
voter_id = []
candidate = []

# open & read csv, dictate column indexes
with open(file, newline="",encoding="utf-8") as csvfile:

    csvreader = csv.reader(csvfile,delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        voter_id.append(row[0])
        candidate.append(row[2])
        



# count number of voters

total_votes = len(voter_id)
#print(total_votes)



# establish variables for each candidate

khan = []
correy = []
li = []
otooley = []

for i in range(0,len(candidate)):
    if candidate[i] == "Khan":
        khan.append(i)
    elif candidate[i] == "Correy":
        correy.append(i)
    elif candidate[i] == "Li":
        li.append(i)
    elif candidate[i] == "O'Tooley":
        otooley.append(i)



# calculate each candidates' vote percentage
khan_percent = (len(khan)/total_votes) * 100
print(khan_percent)
correy_percent = (len(correy)/total_votes) * 100
print(correy_percent)
li_percent = (len(li)/total_votes) * 100
print(li_percent)
otooley_percent = (len(otooley)/total_votes) * 100
#print(otooley_percent)



# clean up values
khan_votes = (len(khan))
correy_votes = (len(correy))
li_votes = (len(li))
otooley_votes = (len(otooley))

khan_percent = "{:.2f}".format(khan_percent)
correy_percent = "{:.2f}".format(correy_percent)
li_percent = "{:.2f}".format(li_percent)
otooley_percent = "{:.2f}".format(otooley_percent)

#print(khan_percent,correy_percent,li_percent,otooley_percent)



# calculate the winner
candidates_dict = dict()

candidates_dict = {
    "Khan":{khan_percent},
    "Correy":{correy_percent},
    "Li":{li_percent},
    "O'Tooley":{otooley_percent}
}

winner = max(candidates_dict, key=candidates_dict.get)
#print(winner)



# final print
l1 = ("Election Results")
l2 = ("--------------------------")
l3 = (f"Total Votes: {total_votes}")
l4 = ("--------------------------")
l5 = (f"Khan: {khan_percent}% ({khan_votes})")
l6 = (f"Correy: {correy_percent}% ({correy_votes})")
l7 = (f"Li: {li_percent}% ({li_votes})")
l8 = (f"O'Tooley: {otooley_percent}% ({otooley_votes})")
l9 = ("--------------------------")
l10 = (f"Winner: {winner}")
l11 = ("--------------------------")

election_results = open(r"C:\Users\hmwhi\OneDrive\Documents\GitHub\Python-challenge\PyPoll\Analysis\election_results.txt","w")
election_results.write(("%s \n %s \n %s \n %s \n %s \n %s \n %s \n %s \n %s \n %s \n %s \n" % (l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11)))

print_analysis = [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11]
for line in print_analysis:
    print(line)


>>>>>>> 6c95cd80d1805e886a28dbb5d90cb4d98f2ad72a
