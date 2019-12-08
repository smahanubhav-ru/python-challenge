#PyBank
import os
import csv

# Get file path
os.chdir(os.path.dirname(os.path.abspath(__file__)))
csvpath = os.path.join('.', 'Resources', 'budget_data.csv')
txtpath = os.path.join('.', 'Resources', 'pybank.txt')

# Declare variables, set default values
total_months = 0        #Total Months
total_revenue = 0       #Total $$

average_change = 0      #Average Change $$
revenue_change = 0
previous_revenue = 0
change_list = []

gip_value = 0           #Greatest Increase in Profits (Value $$)
gip_month = ""          #Greatest Increase in Profits (Month)
gdp_value = 0           #Greatest Decrease in Profits (Value $$)
gdp_month = ""          #Greatest Decrease in Profits (Month)

# Read file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    # Loop through each row
    for row in csvreader:
        # Calculate Totals
        total_months = total_months + 1
        total_revenue = total_revenue + int(row[1])
        
        # Populate change list
        revenue_change = int(row[1]) - previous_revenue
        change_list.append(revenue_change)
        previous_revenue = int(row[1])
        
        if revenue_change >= gip_value:
            gip_value = revenue_change
            gip_month = row[0]
        elif revenue_change <= gdp_value:
            gdp_value = revenue_change
            gdp_month = row[0]
        
# Calculate Average Change
average_change = (sum(change_list)-change_list[0])/(len(change_list)-1)

# Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(total_months))
print("Total: $" + str(total_revenue))
print("Average  Change: $" + str(round(average_change,2)))
print("Greatest Increase in Profits: " + str(gip_month) + " ($" + str(gip_value) + ")")
print("Greatest Decrease in Profits: " + str(gdp_month) + " ($" + str(gdp_value) + ")")

# Export results to text file
with open(txtpath, mode='w', newline='') as txtfile:
    txtfile.writelines("Financial Analysis"+"\n")
    txtfile.writelines("----------------------------"+"\n")
    txtfile.writelines("Total Months: " + str(total_months)+"\n")
    txtfile.writelines("Total: $" + str(total_revenue)+"\n")
    txtfile.writelines("Average  Change: $" + str(round(average_change,2))+"\n")
    txtfile.writelines("Greatest Increase in Profits: " + str(gip_month) + " ($" + str(gip_value) + ")"+"\n")
    txtfile.writelines("Greatest Decrease in Profits: " + str(gdp_month) + " ($" + str(gdp_value) + ")")