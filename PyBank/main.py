import os
import csv

# Declaring Variables
months = []
revenue = []
revenue_change = []
output_file = ""
report_topic = "Financial Analysis"
report_separator = "------------------"

# Function to process data file
def processDataFile(file_name):
    data_file_path = os.path.join('.', 'input', file_name)
    with open(data_file_path, newline='') as data_file:

        # Skip header row
        next(data_file)

        # Read Data
        csv_data = csv.reader(data_file, delimiter=',')
        previous_month_revenue = 0;

        #  Each row is read as a row
        for row in csv_data:

            # list months
            months.append(row[0])

            # list revenues
            revenue.append(int(row[1]))

            # list of revenue changes
            revenue_change.append(int(row[1]) - previous_month_revenue)
            previous_month_revenue = int(row[1])

# Function to print results to screen
def printToTerminal():
    print(report_topic)
    print(report_separator)
    print(strMonths)
    print(strRevenue)
    print(strAvgRevenueChange)
    print(strGreatestIncrease)
    print(strGreatestDecrease)
    print(report_separator)


# Function to write results to file
def printToFile():

    # Set variable for output file
    output_file = os.path.join('.', 'output', 'budget_data_2.txt')

    #  Open the output file
    with open(output_file, "w", newline="") as datafile:
        writer = csv.writer(datafile)

        # Write the header row
        writer.writerow(["Financial Analysis"])
        writer.writerow(["-------------------------"])

        # Write results
        writer.writerow([strMonths])
        writer.writerow([strRevenue])
        writer.writerow([strAvgRevenueChange])
        writer.writerow([strGreatestIncrease])
        writer.writerow([strGreatestDecrease])

# Process first data file
# processDataFile('budget_data_1.csv')

# Process Second data file
processDataFile('budget_data_2.csv')


# Perform Calculations

strMonths = "Total Months: " + str(len(months))
strRevenue = "Total Revenue: $" + str(sum(revenue))
strAvgRevenueChange = "Average Revenue Change: $" + \
                      "{0:.2f}".format(sum(revenue_change) / len(revenue_change))
# Greatest Increase in Revenue
max_revenue = max(revenue)
max_revenue_month = months[revenue.index(max_revenue)]
strGreatestIncrease = "Greatest Increase in Revenue: " + max_revenue_month + " ($" + str(max_revenue) + ")"

# Greatest Decrease in Revenue
min_revenue = min(revenue)
min_revenue_month = months[revenue.index(min_revenue)]
strGreatestDecrease = "Greatest Decrease in Revenue: " + min_revenue_month + " ($" + str(min_revenue) + ")"


# Print Results to File
printToFile()

# Print Results to Terminal
printToTerminal()

print("Process Completed.")


