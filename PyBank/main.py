import csv, os


csvpath = os.path.join( "budget_data.csv")
Total = 0
MonthCounter = 0
FirstRow = True
CurrTotal = 0
PrevTotal = 0
Change = 0
ChangeSum = 0
AverageChange = 0
AverageChangePeriods = 0
GreatestInc = 0
GreatestIncMonth = ''
GreatestDec = 0
GrestestDecMonth = ''
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        CurrTotal = int(row[1])
        Total += CurrTotal
        MonthCounter += 1
        
        if FirstRow == False:
            Change = CurrTotal - PrevTotal
            ChangeSum += Change

        #Reset variables for next row
        FirstRow = False
        PrevTotal = CurrTotal

AverageChange = round(ChangeSum/(MonthCounter-1),2)
print(f"Total Months: {MonthCounter}") 
print(f"Total: ${Total}")   
#print(f"Total Change: ${ChangeSum}")     
print(f"Average Change: ${AverageChange}")    