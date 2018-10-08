# Modules
import os
import csv

#set path for file
csvpath = os.path.join("..", "PyBank", "Resources","budget_data.csv")

#set variales
total_months = 0
total_profit_loss = 0
prev_profit_loss = 0
month_change =0
total_month_change = 0
average_month_change = 0
greatest_increase = 0
greatest increast month = ""
greatest_decrease_month =  0
greatest_decrease = 0
greatest_increase_month""

# open csv
with open(csvpath, newline = "") as csvfile
csvreader = csv.reader(csvfile, delimiter=",")

#read the header row first
csv_header = next(csvreader)

#read each row of data after the header
for row in csvreader:
# count the total number of months
totals_months += 1

# add up the total net profit/loss
total_profit_loss += int(row[1])

calculate the change in profit/loss between months
if total_months > 1:
  month_change = int(row[1]) - prev_profit_loss

  # add up the total montly change, user later to calculate average
  total_month_change += month_change

  # set profit/loss value for previous month
  prev_profit_loss = int(row[1])

  # calculte greatest increase in profit
  if month_change > greatest_increase:
      greatest_increase = month_change
      greates_increase-month = row[0]

      #calculate greatest decrease in losses
      if month_change < greatest_decrease:
          greatest_decrease =month_change
          greatest_decrease_month = row[0]

          # calculate average change between months
          average_month_change = total_month_change / (total_months - 1)

          # print the analysis to terminal
          print"Financial Analysis")
          print("------------------------")
          print("Total Months: " + str(total_months))
          print("Total: $" + str(total_profit_loss))
          print("Average Change: $" + str(format(average_month_change, '.2f')))
          print("Greatest Increase in Pofits: " + greatest_increase_month + 
          " ($" + str(greatest_increase) +")")
          print("Greatest Decrease in profits: " + greatest_decrease_month + " ($" + str(greatest_decrease) +")")

# write to text file
f = open(analysis.txt" , "w")
f.write("Financial Analysis\n")
f.write("--------------------\n")
f.write("Total Months: " + str(total_months) + "\n")
f.write("Total: $" + str(total_profit_loss) + "\n")
f.write("Average Change: $" + str(format(average_month_change, '.2f')) + "\n")
f.wrie("Greatest Increase in Profits: " + greatest_increase_month + " ($" + str(greatest_increase) + ")\n")
f.write("Greatest Decrease in Profits: " + greatest_decrease_month + " ($" + str(greatest_decrease) + ")\n")
f.close()



