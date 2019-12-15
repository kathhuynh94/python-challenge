import os
import csv

month_count = 0
total_profit_loss = 0
minimum = 0
minimum_date = None

maximum = 0
maximum_date = None


# Set path for file
text_path = "C:/Users/Admin/Documents/UofA-PHX-DATA-PT-11-2019-U-C/03-Python/Homework/Instructions/HW_complete"
text_name = "pybank_answer.txt"
text_file_path = os.path.join (text_path, text_name)
path = "C:/Users/Admin/Documents/UofA-PHX-DATA-PT-11-2019-U-C/03-Python/Homework/Instructions/PyBank/Resources"
filename = "budget_data.csv"
csv_file_path = os.path.join(path, filename)

# loads into memory
with open(csv_file_path, 'r') as csv_file:
    # reads the binary/data screen; it opens the object
    csv_read = csv.reader(csv_file,delimiter=',')
    # takes the object and returns it as a list
    csv_list = list(csv_read)


## The total number of months included in the dataset
# length of list minus the header
month_count = len(csv_list) - 1

## The net total amount of "Profit/Losses" over the entire period
# removing the header
for row in csv_list[1:]:
    # starting at second item in each row 
    profit_loss = int(row[1])
    # adding the profit_loss to the total 
    total_profit_loss = total_profit_loss + profit_loss

    # looking for minimum value
    if profit_loss < minimum:
        minimum = profit_loss
        minimum_date = row[0]    

    # looking for maximum value 
    if profit_loss > maximum:
        maximum = profit_loss
        maximum_date = row[0]

## The average of the changes in "Profit/Losses" over the entire period
avg_profit_loss = total_profit_loss / month_count

## The greatest increase in profits (date and amount) over the entire period


print('Financial Analysis')
print('----------------------')
print('Total Months: ' + str(month_count))
print('Total: $' + str(total_profit_loss))
print('Average Change: $' + str(avg_profit_loss))
print('Greatest Increase in Profits: ' + maximum_date + ' $' + str(maximum))
print('Greatest Increase in Profits: ' + minimum_date + ' $' + str(minimum))

    

with open(text_file_path, 'w') as text_file:
    text_file.write('Financial Analysis\n')
    text_file.write('----------------------\n')
    text_file.write('Total Months: ' + str(month_count) + '\n')
    text_file.write('Total: $' + str(total_profit_loss) + '\n')
    text_file.write('Average Change: $' + str(avg_profit_loss) + '\n')
    text_file.write('Greatest Increase in Profits: ' + maximum_date + ' $' + str(maximum) + '\n')
    text_file.write('Greatest Increase in Profits: ' + minimum_date + ' $' + str(minimum) + '\n')
