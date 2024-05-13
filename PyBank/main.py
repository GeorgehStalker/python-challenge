import csv

# File path to the CSV data
csv_file_path = "C:/Users/georg/git repositories/Module 3/python-challenge/PyBank/Resources/budget_data.csv"

# Initializing variables for financial analysis
num_months = 0
net_profit_loss = 0
total_change = 0
max_increase = 0
max_increase_date = ""
max_decrease = 0
max_decrease_date = ""

# Counting the total number of months in the dataset
with open(csv_file_path, 'r', newline='') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skipping the header row
    for row in csv_reader:
        num_months += 1

print("Total number of months included in the dataset:", num_months)

# Calculating the net total amount of Profit/Losses over the entire period
with open(csv_file_path, 'r', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        net_profit_loss += int(row['Profit/Losses'])

print("Net total amount of Profit/Losses over the entire period:", net_profit_loss)

# Calculating changes in Profit/Losses over the entire period and the average change
with open(csv_file_path, 'r', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    first_row = next(csv_reader)
    previous_profit_loss = int(first_row['Profit/Losses'])
    num_months += 1
    for row in csv_reader:
        current_profit_loss = int(row['Profit/Losses'])
        change = current_profit_loss - previous_profit_loss
        total_change += change
        previous_profit_loss = current_profit_loss

average_change = total_change / (num_months - 1)
print("Average of the changes in Profit/Losses over the entire period:", average_change)

# Finding the greatest increase in profits (date and amount) over the entire period
with open(csv_file_path, 'r', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    first_row = next(csv_reader)
    previous_profit_loss = int(first_row['Profit/Losses'])
    max_increase_date = first_row['Date']
    for row in csv_reader:
        current_profit_loss = int(row['Profit/Losses'])
        increase = current_profit_loss - previous_profit_loss
        if increase > max_increase:
            max_increase = increase
            max_increase_date = row['Date']
        previous_profit_loss = current_profit_loss

print("The greatest increase in profits occurred on", max_increase_date, "with an amount of", max_increase)

# Finding the greatest decrease in profits (date and amount) over the entire period
with open(csv_file_path, 'r', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    first_row = next(csv_reader)
    previous_profit_loss = int(first_row['Profit/Losses'])
    max_decrease_date = first_row['Date']
    for row in csv_reader:
        current_profit_loss = int(row['Profit/Losses'])
        decrease = current_profit_loss - previous_profit_loss
        if decrease < max_decrease:
            max_decrease = decrease
            max_decrease_date = row['Date']
        previous_profit_loss = current_profit_loss

print("The greatest decrease in profits occurred on", max_decrease_date, "with an amount of", max_decrease)
def calculate_statistics(data):
    total_months = len(data)
    total = sum(data.values())
    average_change = sum(data.values()) / len(data)
    greatest_increase = max(data.values())
    greatest_decrease = min(data.values())

    return total_months, total, average_change, greatest_increase, greatest_decrease

def write_to_file(file_path, total_months, total, average_change, greatest_increase, greatest_decrease):
    with open(file_path, 'w') as file:
        file.write("Financial Analysis\n")
        file.write("-----------------------------\n")
        file.write(f"Total Months: {total_months}\n")
        file.write(f"Total: ${total}\n")
        file.write(f"Average Change: ${average_change:.2f}\n")
        file.write(f"Greatest Increase in Profits: ${greatest_increase}\n")
        file.write(f"Greatest Decrease in Profits: ${greatest_decrease}\n")

def main():
    # Path to the CSV file
    csv_file_path = "C:/Users/georg/git repositories/Module 3/python-challenge/PyBank/Resources/budget_data.csv"
    # Perform your calculations to get the required statistics
    # Here, assuming 'data' contains the necessary information
    data = {'Jan': 867884, 'Feb': 984655, 'Mar': 322013, 'Apr': -69417, 'May': 310503, 'Jun': 522857, 'Jul': 1033096, 'Aug': 604885, 'Sep': -216386, 'Oct': 477532, 'Nov': 893810, 'Dec': -80353}
    total_months, total, average_change, greatest_increase, greatest_decrease = calculate_statistics(data)
    
    # Path to the text file
    text_file_path = "C:/Users/georg/git repositories/Module 3/python-challenge/PyBank/Analysis/financial_analysis.txt"
    write_to_file(text_file_path, total_months, total, average_change, greatest_increase, greatest_decrease)

if __name__ == "__main__":
    main()
