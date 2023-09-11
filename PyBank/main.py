import os
import csv

budget_path= "Resources\\budget_data.csv"

with open(budget_path, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csvheader = next(csvreader)

    rowcount = 0

    sum_total = 0

    total_change = 0

    previous_row = None

    greatest_increase = 0

    greatest_increase_month = None

    greatest_decrease = 0

    greatest_decrease_month = None

    for r in csvreader:
        rowcount = rowcount + 1

        sum_total = int(sum_total) + int(r[1])

        if previous_row != None:
            
            this_month_value = int(r[1])
            last_month_value = int(previous_row[1])
            
            change = this_month_value - last_month_value

            total_change = total_change + change

            if change > 0 and change > greatest_increase:
                greatest_increase = change
                greatest_increase_month = r[0]

            elif change < 0 and change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_month = r[0]

        previous_row = r

        avg_change = round(total_change / 85, 2)
       
    print(f"Total Months: ", rowcount)
    print(f"Total: ", sum_total)
    print(f"Average Change: ", avg_change)
    print(f"Greatest Increase in Profits: " + str(greatest_increase_month) + "    $" + str(greatest_increase))
    print(f"Greatest Decrease in Profits: " + str(greatest_decrease_month) + "    $" + str(greatest_decrease))




# Open the output file
budget_final_path = "analysis\budget_analysis.txt"
budget_analysis = zip(rowcount, sum_total, avg_change, greatest_increase, greatest_decrease)

with open(budget_final_path, "w") as budget_analysis:
    writer = csv.writer(budget_analysis)

# Write the Contents
    budget_analysis.writerow(["Total Months", "Total", "Average Change", "Greatest Increase in Profits", "Greatest Decrease in Profits"])

    writer.writerows(budget_analysis)

