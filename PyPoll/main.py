import csv
import os
import pprint

pp = pprint.PrettyPrinter(indent=4)
mapData = {}

pathToSearchIn = os.path.join("/Users")
csvpath = "Not found"
for root, dirs, files in os.walk(pathToSearchIn):
    if "election_data.csv" in files:
            csvpath = os.path.join(root, "election_data.csv")
            
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    
    countRows = 0 
    for row in csvreader:
        countRows = countRows+1
        if row[2] in mapData:
           mapData[row[2]] =  mapData[row[2]]+1 
        else :
           mapData[row[2]]= 1 

#pp.pprint(mapData)
#pp.pprint(countRows)
                        
keysSorted = sorted(mapData, key=mapData.get, reverse=True)
stringVotesForEach = ""

for keyData in keysSorted:
    stringVotesForEach=stringVotesForEach+"\n"+keyData+" : %"+str(mapData.get(keyData)*100/countRows)+" ("+str(mapData.get(keyData))+")"
    
printableResult = ("Election Results \n-------------------------\n"
                    "Total Votes :"+ str(countRows)+"\n-------------------------\n"+stringVotesForEach+
                     "\n-------------------------\n Winner:"+keysSorted[0]+"\n-------------------------\n"
                     )
print(printableResult)

file = open("output_election_data.txt","a")
file.write(printableResult)
file.close()  