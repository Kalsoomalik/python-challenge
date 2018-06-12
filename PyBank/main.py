import os
import csv

# Declaring Variables
months = []
revenue = []
revenue_change = []


# Define month count variable
def incrementCount(count):
    count += 1
    return count


# Function to process data file
def processDataFile(file_name):
    data_file_path = os.path.join('.', 'input', file_name)
    with open(data_file_path, newline='') as data_file:
        # Skip header row
        next(data_file)

        # Read Data
        csv_data = csv.reader(data_file, delimiter=',')
        count = 0;
        previous_month_revenue = 0;

        #  Each row is read as a row
        for row in csv_data:
            count += count

            # list months
            months.append(row[0])

            # list revenues
            revenue.append(int(row[1]))

            # list of revenue changes
            revenue_change.append(int(row[1]) - previous_month_revenue)
            previous_month_revenue = int(row[1])


# Process first data file
processDataFile('budget_data_1.csv')

# Process Second data file
# processDataFile('budget_data_2.csv')

# Set variable for output file
output_file = os.path.join('.', 'output', 'budget_data.txt')

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Financial Analysis"])
    writer.writerow(["-------------------------"])

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

    # Write the header row
    writer.writerow([strMonths])
    writer.writerow([strRevenue])
    writer.writerow([strAvgRevenueChange])
    writer.writerow([strGreatestIncrease])
    writer.writerow([strGreatestDecrease])

print("Output File: " + output_file)
print("Process Completed.")
