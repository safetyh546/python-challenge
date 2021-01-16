import csv, os, sys

# Specify the file to Read From
csvpath = os.path.join("Resources","budget_data.csv")
# Specify the file to write to
output_path = os.path.join("analysis", "Results.txt")

#Set Variables
Total = 0
MonthCounter = 0
FirstRow = True
CurrTotal = 0
PrevTotal = 0
Change = 0
AverageChange = 0
AverageChangePeriods = 0
GreatestInc = 0
GreatestIncMonth = ''
GreatestDec = 0
GrestestDecMonth = ''
ChangeLst=[]

#Open file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    #Start looping through rows
    for row in csvreader:
        CurrTotal = int(row[1])
        Total += CurrTotal
        MonthCounter += 1
        
        #If not first row, calculate Change, Append to Change list, and set Greatest Inc/Dec variables
        if FirstRow == False:
            Change = CurrTotal - PrevTotal
            ChangeLst.append(Change)
            if Change < GreatestDec:
            	GreatestDec = Change
            	GreatestDecMonth = row[0]
            if Change > GreatestInc:
            	GreatestInc = Change
            	GreatestIncMonth = row[0]

        #Reset variables for next row
        FirstRow = False
        PrevTotal = CurrTotal

AverageChange = round(sum(ChangeLst)/len(ChangeLst),2)

#Print to terminal
print('Financial Analysis')
print("-------------------------------------")
print(f"Total Months: {MonthCounter}") 
print(f"Total: ${Total}")      
print(f"Average Change: ${AverageChange}")
print(f"Greatest Increase in Profits: {GreatestIncMonth[:4]}20{GreatestIncMonth[-2:]} (${GreatestInc})")
print(f"Greatest Decrease in Profits: {GreatestDecMonth[:4]}20{GreatestDecMonth[-2:]} (${GreatestDec})")     


#Export to analysis.txt file
sys.stdout = open(output_path, "w")

print('Financial Analysis')
print("-------------------------------------")
print(f"Total Months: {MonthCounter}") 
print(f"Total: ${Total}")      
print(f"Average Change: ${AverageChange}")
print(f"Greatest Increase in Profits: {GreatestIncMonth[:4]}20{GreatestIncMonth[-2:]} (${GreatestInc})")
print(f"Greatest Decrease in Profits: {GreatestDecMonth[:4]}20{GreatestDecMonth[-2:]} (${GreatestDec})")  

sys.stdout.close()