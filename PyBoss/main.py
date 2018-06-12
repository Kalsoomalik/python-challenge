# Import required libraries
import csv
import datetime as dt
import os

# Lists to store data
emp_id = []
first_name = []
last_name = []
dob = []
ssn = []
state = []

# Sate abbreviation dictionary
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


# Function to return First Name
def getFirstName(name_list):
    if len(name_list) > 0:
        return name_list[0]
    else:
        return ""


# Function to return Last Name
def getLastName(name_list):
    if len(name_list) > 1:
        return name_list[1]
    else:
        return ""


# Function to format DOB
def formatDOB(dob):
    dob_db = dt.datetime.strptime(dob, '%Y-%m-%d').date()
    return dob_db.strftime("%m/%d/%Y")


# Function to hide SSN information
def maskSSN(ssn):
    return "***-**-" + ssn.split("-")[2]


# Function to process data file
def processDataFile(file_name):
    data_file_path = os.path.join('.', 'input', file_name)
    with open(data_file_path, newline='') as data_file:
        # Skip header row
        next(data_file)

        # Read Data
        csv_data = csv.reader(data_file, delimiter=',')

        #  Each row is read as a row
        for row in csv_data:
            # Add Emp ID
            emp_id.append(row[0])

            # Split full name
            full_name = row[1].split()
            first_name.append(getFirstName(full_name))
            last_name.append(getLastName(full_name))

            # format DOB
            dob.append(formatDOB(row[2]))

            # Mask SSN
            ssn.append(maskSSN(row[3]))

            # Abbreviate State
            state.append(us_state_abbrev[row[4]])


# Process first data file
# processDataFile('employee_data1.csv')

# Process Second data file
processDataFile('employee_data2.csv')

# Zip lists together
processed_csv = zip(emp_id, first_name, last_name, dob, ssn, state)

# Set variable for output file
output_file = os.path.join('.', 'output', 'employee_data_converted_2.csv')

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Emp ID", "First Name", "Last Name", "DOB",
                     "SSN", "State"])

    # Write in zipped rows
    writer.writerows(processed_csv)

print("Output File: " + output_file)
print("Process Completed.")
