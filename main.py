import os
import csv
from myDict import us_state_abbrev
new_employee_data = []
"Setting the path for input csv file"
filepath = os.path.join("employee_data1.csv")
"Setting the path for output csv file"
new_file = os.path.join("employee_data2.csv")

# Read data into dictionary and edit the format of the fields 
with open(filepath) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        emp_id = row["Emp ID"]
        name = row["Name"]
        dob = row["DOB"]
        ssn = row["SSN"]
        state = row["State"]

        # Reformatting Name into Last Name and First Name
        first_name = name.split()[0]
        last_name = name.split()[1]
        #Reformatting DOB into MM/DD/YYYY format 
        dob_parts = dob.split('-')
        new_dob = dob_parts[1]+"/"+dob_parts[2]+"/"+dob_parts[0]
        #Reformatting SSN into ***-**-1234 format 
        ssn_parts = ssn.split('-')
        new_ssn = "***-**-"+ssn_parts[2]
        if state in us_state_abbrev.keys():
            new_state = us_state_abbrev[state]

        new_employee_data.append(
            {
                "Emp ID" : row["Emp ID"],
                "First Name": first_name,
                "Last Name": last_name,
                "DOB": new_dob,
                "SSN": new_ssn,
                "State": new_state
            }
        )
# Grab the filename from the original path
_, filename = os.path.split(new_file)

# Write updated data to csv file
csvpath = os.path.join(filename)
with open(csvpath, "w") as csvfile:
    fieldnames = ["Emp ID","First Name", "Last Name", "DOB", "SSN","State"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(new_employee_data)


