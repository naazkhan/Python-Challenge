import csv

file_to_load = "/Users/naaz.27khan/Desktop/python/budget_data.csv"
file_to_output = "Resources/budget_analysis.txt"

total_months = 0
total_Profit/Loss = 0

prev_Profit/Loss = 0
Profit/Loss_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999999]

Profit/Loss_changes = []

with open(file_to_load) as budget_data:
    reader = csv.DictReader(budget_data)

    
    for row in reader:

        total_months = total_months + 1
        total_Profit/Loss = total_Profit/Loss + int(row["Profit/Loss"])
        # print(row)

        Profit/Loss_change = int(row["Profit/Loss"]) - prev_Profit/Loss
      
        prev_Profit/Loss = int(row["Profit/Loss"])

        if (Profit/Loss_change > greatest_increase[1]):
            greatest_increase[1] = profit/losses_change
            greatest_increase[0] = row["Date"]

        if (Profit/Loss_change < greatest_decrease[1]):
            greatest_decrease[1] = profit/losses_change
            greatest_decrease[0] = row["Date"]

        Profit/Loss_changes.append(int(row["Profit/Loss"]))

    Profit/Loss_avg = sum(Profit/Loss_changes) / len(Profit/Loss_changes)
    
    print()
    print()
    print()
    print("Financial Analysis")
    print("-------------------------")
    print("Total Months: " + str(total_months))
    print("Total Profit/Loss: " + "$" + str(total_Profit/Loss))
    print("Average Change: " + "$" + str(round(sum(Profit/Loss_changes) / len(Profit/Loss_changes),2)))
    print("Greatest Increase: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")") 
    print("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")
    


with open(file_to_output, "w") as txt_file:
    txt_file.write("Total Months: " + str(total_months))
    txt_file.write("\n")
    txt_file.write("Total Profit/Loss: " + "$" + str(total_Profit/Loss))
    txt_file.write("\n")
    txt_file.write("Average Change: " + "$" + str(round(sum(Profit/Loss_changes) / len(Profit/Loss_changes),2)))
    txt_file.write("\n")
    txt_file.write("Greatest Increase: " + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) + ")") 
    txt_file.write("\n")
    txt_file.write("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) + ")")
