#Import necessary modules and establish file path

import os
import csv
import math
#import numpy as np
import itertools as it
#import operator as op



pybank_csv = r"C:\Users\hmwhi\OneDrive\Documents\GitHub\Python-challenge\Pybank\Resources\budget_data.csv"


#clean_csv = "C:\\Users\\hmwhi\\OneDrive\\Desktop\\Bootcamp Files\\Homework Files\\python-challenge\\Pybank\\Analysis\\clean_csv.csv"
date = []
profit_loss = []

with open(pybank_csv, newline='', encoding='utf-8') as csvfile:
    
    csvreader = csv.reader(csvfile,delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        #rows = [header] + [[row[0], int(row[1]])]
        date.append(row[0])
        profit_loss.append(row[1])



no_of_months = len(date)
#run more than once doubles the list and sum

#Clean the CSV file
cleaned_csv = zip(date,profit_loss)
output_file = "C:\\Users\\hmwhi\\OneDrive\\Documents\\GitHub\\python-challenge\\Pybank\\Analysis\\clean_csv.csv"
with open(output_file, 'w',newline='') as datafile:
   
    writer = csv.writer(datafile)
    writer.writerows(cleaned_csv)


#find the total amount
profit_loss = [int(i)for i in profit_loss]

# print(profit_loss)
total_sum = math.fsum(profit_loss)
finsum = (f'${total_sum}0')
#print(finsum)

#print(no_of_months)

#find min and max
max_profit = max(profit_loss)
min_loss = min(profit_loss)

#no need to index "row[0]", because it is already indexed as "date"
max_date = []
for i in range(0,len(profit_loss)):
    if profit_loss[i] == max_profit:
        max_date = date[i]


min_date = []
for i in range(0,len(profit_loss)):
    if profit_loss[i] == min_loss:
        min_date.append(i)
        min_date = date[i]


max_profit = (f'${max_profit}.00')
min_loss = (f'${min_loss}.00')

max_ = (max_date,max_profit)
min_ = (min_date,min_loss)

#print(max_)
#print(min_)

# https://www.geeksforgeeks.org/python-ways-to-find-indices-of-value-in-list/

#make list for average difference in values

# referenced <https://stackoverflow.com/questions/2400840/python-finding-differences-between-elements-of-a-list>
# ...for this code

#diff = profit_loss(map(operator.sub, profit_loss[1:], profit_loss[:-1])) X

diff_list = [j-i for i, j in zip(profit_loss[:-1], profit_loss[1:])]

#print(diff_list)

#find average of diff_list
n = len(diff_list)
tot = sum(diff_list)
avg = tot/n
avg_change = round(avg,2)
#print(n,tot,avg_change)

#Final Print
line1 = ("Finacial Analysis")
line2 = ("--------------------------------")
line3 = (f"Total Months: {no_of_months}")
line4 = (f"Total: {finsum}")
line5 = (f"Average Change: ${avg_change}")
line6 = (f"Greatest Increase in Profits: {max_}")
line7 = (f"Greatest Decrease in Profits: {min_}")

financial_analysis = open(r"C:\Users\hmwhi\OneDrive\Documents\GitHub\python-challenge\Pybank\Analysis\financial_analysis.txt","w")
financial_analysis.write(("%s \n %s \n %s \n %s \n %s \n %s \n %s \n" % (line1,line2,line3,line4,line5,line6,line7)))

finalaysis = [line1,line2,line3,line4,line5,line6,line7]
for line in finalaysis:
    print(line)