import os
import csv

# Declaring Variables
total_votes = {}
candidate_map = {}
max_votes = 0
results = []
winner = ""
output_file = ""
report_topic = "Election Results"
report_separator = "--------------------------"

# Function to process data file
def processDataFile(file_name):
    data_file_path = os.path.join('.', 'input', file_name)
    with open(data_file_path, newline='') as data_file:

        # Skip header row
        next(data_file)

        # Read Data
        csv_data = csv.reader(data_file, delimiter=',')
        count = 0

        #  Each row is read as a row
        for row in csv_data:
            count = count + 1
            candiate = row[2]
            votes = candidate_map.get(candiate)
            if votes is not None:
                voteCount = int(str(votes))
                voteCount = voteCount + 1
                candidate_map[candiate] =  voteCount
            else:
                candidate_map[candiate] =  1
        total_votes['count'] = count

# Function to print results to screen
def printToTerminal():
    print(report_topic)
    print(report_separator)
    print("Total Votes: " + str(total_votes['count']))
    print(report_separator)
    for result in results:
        print(result)
    print(report_separator)
    print("Winner: " + winner)
    print(report_separator)

# Function to write results to file
def printToFile():

    # Set variable for output file
    output_file = os.path.join('.', 'output', 'election_results_2.txt')

    #  Open the output file
    with open(output_file, "w", newline="") as datafile:
        writer = csv.writer(datafile)

        # Write the Results
        writer.writerow([report_topic])
        writer.writerow([report_separator])
        writer.writerow(["Total Votes: " + str(total_votes['count'])])
        writer.writerow([report_separator])
        for result in results:
            writer.writerow([result])
        writer.writerow([report_separator])
        writer.writerow(["Winner: " + winner])
        writer.writerow([report_separator])


# Process first data file
# processDataFile('election_data_1.csv')

# Process Second data file
processDataFile('election_data_2.csv')

# Process Election Results
for key, value in candidate_map.items():
    if (value > max_votes):
        max_votes = value
        winner = key
    str_percent_count = "{0:.2f}".format(value / total_votes['count'] * 100) + "%"
    results.append(key + ": " + str_percent_count + " (" + str(value) + ")")

# Print Results to File
printToFile()

# Print Results to Terminal
printToTerminal()

print("Process Completed.")


