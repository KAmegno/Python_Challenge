import os 

import csv

py_bank_csv_path = os.path.join(os.path.dirname(__file__), 'Resources', 'budget_data.csv')

#Define function and have it accept the budget data as its sole parameter knowing that #month = str(csvreader[0]) and profit_losses = int(csvreader[1]) 
count = 0 
net_amount = 0
previous_row = 0
changes = []
dates = []

#open data_budget file and read header. 
with open(py_bank_csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")  
    csv_header = next(csvreader)

    #Create a loop and have all calculation within 
    for row in csvreader:
        count += 1 #Augmented count of months 
        net_amount += int(row[1]) #Augmented profit_loss net 
        avg = int(row[1]) - previous_row 
        previous_row = int(row[1])
        changes.append(avg)
       
        # to keep track of the date
        dates.append(row[0]) 

    #Find greatest increase in profit 
    greatest_increase = max (changes)
    greatest_index = changes.index (greatest_increase)
    greatest_date = dates[greatest_index]

    #Find greatest decrease in profit
    greatest_decrease = min (changes)
    greatest_decrease_index = changes.index (greatest_decrease)
    greatest_decrease_date = dates[greatest_decrease_index]
    
    changes.pop(0)
    
    #Print each result of the analysis 
    print("_________________________________________________")
    print("Financial Analysis")
    #changes.pop(0)
    print("Total Months:", count)
    print(f"Total:  ${net_amount}")
    print(f"Average change: ${round(sum(changes)/(count -1),2)}")
    print(f"Greatest increase in profits: {greatest_date}, (${greatest_increase})")
    print(f"Greatest decrease in profits: {greatest_decrease_date}, (${greatest_decrease})")
    print("_________________________________________________")


#Writing the results into analysis text file 
#file = open(Financial_Analysis.text, "w") 

#file.write(
#file.write 'Financial Analysis\n'

#)









#csvpath = "C:\Users\v.k.a\um\homework\03-python\Python_Challenge\PyBank\Resources\budget_data.csv))"
#csvpath = os.path.join("C:\\Users\\v.k.a\\um\\homework\\03-python\\Python_Challenge\\PyBank\\Resources\\budget_data.csv")
#with open(csvpath, encoding='utf') as csvfile: