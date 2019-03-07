import csv
import os
import pprint

pp = pprint.PrettyPrinter(indent=4)

pathToSearchIn = os.path.join("/Users")
csvpath = "Not found"
for root, dirs, files in os.walk(pathToSearchIn):
    if "budget_data.csv" in files:
            csvpath = os.path.join(root, "budget_data.csv")
            
rowCount = 0
maxValue = -1
max_Date = "NA"
minValue = 0
min_Date = "NA"
running_sum = 0 
running_difference = 0 
previous_value = 0 

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #rowCount = sum(1 for row in csvreader) 
    #print (rowCount)
    #printHelper = 0

    for row in csvreader:
        if int(row[1]) > int(maxValue)  :
            max_Date = row[0]
            maxValue = row[1]
        if int(row[1]) < int(minValue)  :
            min_Date = row[0]
            minValue = row[1]
        running_sum = running_sum + int(row[1])
        rowCount = rowCount + 1
        if(rowCount > 0) : # this is because the average change is not valid for the first data set , so we have only N-1 differences
            running_difference = running_difference + (int(row[1]) - previous_value)
        previous_value = int(row[1])

stringToOutput = ("\t\t\t Financial Analysis\t\t\t\n------------------------------------------------------------------------\n"
                    "Total Months:"+str(rowCount)+"\n"
                    "Total:"+str(running_sum)+"\n"
                     "Average  Change: $"+ str(running_difference/(rowCount-1) )+"\n"
                     "Average  : $"+ str(running_sum/rowCount )+"\n"
                      "Greatest Increase in Profits:"+max_Date+" ($)"+str(maxValue)+"\n"
                        "Greatest Decrease in Profits:"+min_Date+" ($)"+str(minValue)+"\n")
print(stringToOutput)
file = open("output_budget_data.txt","a")
file.write(stringToOutput)
file.close()  
        