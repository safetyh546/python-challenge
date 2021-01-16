import csv, os, sys

# Specify the file to Read From
csvpath = os.path.join("Resources","election_data.csv")
# Specify the file to write to
output_path = os.path.join("analysis", "Results.txt")

#Set Variables
Total = 0
KhanVotes = 0
CorreyVotes = 0
LiVotes = 0
OTooleyVotes = 0
VotesLst=[]
Winner = ""


#Open file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    #Start looping through rows
    for row in csvreader:
        Total += 1
        if row[2]=="Khan":
            KhanVotes += 1
        if row[2]=="Correy":
            CorreyVotes += 1
        if row[2]=="Li":
            LiVotes += 1
        if row[2]=="O'Tooley":
            OTooleyVotes += 1

if KhanVotes > CorreyVotes and KhanVotes > LiVotes and KhanVotes > OTooleyVotes:
    Winner = "Khan"
if CorreyVotes > LiVotes and CorreyVotes > KhanVotes and CorreyVotes > OTooleyVotes:
    Winner = "Correy"
if LiVotes > CorreyVotes and LiVotes > KhanVotes and LiVotes > OTooleyVotes:
    Winner = "Li"
if OTooleyVotes > CorreyVotes and OTooleyVotes > KhanVotes and OTooleyVotes > LiVotes:
    Winner = "O'Tooley"

#Print to terminal
print('Election Results')
print("-------------------------------------")
print(f"Total Votes: {Total}") 
print("-------------------------------------")      
print(f"Khan: {round(KhanVotes/Total*100,4)}00% ({KhanVotes})") 
print(f"Correy: {round(CorreyVotes/Total*100,4)}00% ({CorreyVotes})") 
print(f"Li: {round(LiVotes/Total*100,4)}00% ({LiVotes})") 
print(f"O'Tooley: {round(OTooleyVotes/Total*100,4)}00% ({OTooleyVotes})") 
print("-------------------------------------")
print(f"Winner: {Winner}") 
print("-------------------------------------")  

#Export to analysis.txt file
sys.stdout = open(output_path, "w")

print('Election Results')
print("-------------------------------------")
print(f"Total Votes: {Total}") 
print("-------------------------------------")      
print(f"Khan: {round(KhanVotes/Total*100,4)}00% ({KhanVotes})") 
print(f"Correy: {round(CorreyVotes/Total*100,4)}00% ({CorreyVotes})") 
print(f"Li: {round(LiVotes/Total*100,4)}00% ({LiVotes})") 
print(f"O'Tooley: {round(OTooleyVotes/Total*100,4)}00% ({OTooleyVotes})") 
print("-------------------------------------")
print(f"Winner: {Winner}") 
print("-------------------------------------")    
 
sys.stdout.close()