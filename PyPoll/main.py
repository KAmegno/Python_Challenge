import os

import csv

#To read csvfile 
py_poll_csv_path = os.path.join(os.path.dirname(__file__), 'Resources', 'election_data.csv')

#to write textfile
py_poll_txt_path = os.path.join(os.path.dirname(__file__), 'analysis', ' Pypoll_results.txt')

#Define function and have it accept the election data as its sole parameter knowing that 
#ballot = int(csvreader[0]), county name = str(csvreader[1])and candidate name = str(csvreader[2])
ballots = 0
number_ballots = []
candidate = []
percent_ballots = []

#open data_budget file and read header. 
with open(py_poll_csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")  
    csv_header = next(csvreader)
      
    #Augmented count of total ballots
    for row in csvreader:
      ballots +=1  

        #Total candidates votes per name 
      if row [2] not in candidate:
         candidate.append(row[2])
         index = candidate.index(row[2])
         number_ballots.append(1)
      else:
        index = candidate.index(row[2]) 
        number_ballots[index] +=1    

#determine candidates ballots percentage 
for ballot in number_ballots:
         percentage = (ballot/ballots) * 100
         percentage = round(percentage,2)
         percent_ballots.append(percentage)

#Find winner by looking for max votes
winnercount = max(percent_ballots)
winnerindex = percent_ballots.index(winnercount) 

#Printing poll results 
print("Election Results")
print("______________________________")
print(f"Total Votes:{str(ballots)}")  
print("______________________________")
#For each candidate,print their name, vote count, and percent of votes received. 
for i in range(0,3): 
 print(f"{str(candidate[i])}: {(percent_ballots[i])}% ({number_ballots[i]})")
print("______________________________")
print(f"Winner: {candidate[winnerindex]}")

#Printing results to a text file
with open(py_poll_txt_path, 'w') as txtfile:
    txtfile.write("Election Results \n")
    txtfile.write("______________________________\n")
    txtfile.write(f"Total Votes: {str(ballots)}\n")  
    txtfile.write("______________________________\n")
    for i in range(0,3):
      txtfile.write(f"{str(candidate[i])}: {(percent_ballots[i])}% ({number_ballots[i]})\n")
    txtfile.write("______________________________\n")
    txtfile.write(f"Winner: {candidate[winnerindex]}\n")