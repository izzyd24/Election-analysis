# data we need to retrieve
# 1. total # of votes cast
# 2. complete list of candidates who recieved votes
# 3. % votes each candidate recieved
# 4. total # of votes each candidate recieved 
# 5. winner of election based on popular vote

# Import the datetime class from the datetime module. This is standard with our version of python 
# dt is used to help datetime less confusing name 
#import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
# datetime 1 is the module (doll 1)
# datetime 2 is the class (doll 2)
# .now is the datetime attribute (doll 3)
#now = dt.datetime.now()
# Print the present time.
#print("The time right now is ", now)
# expected output: The time right is now 2022-04-18 12:30:06.870140

# this will help us assign a variable to the current path
# this is using a directpath
#file_to_load = 'Resources/election_results.csv'

# Open the election results and read the file
# with statement here lets us open and close all in one stop
#with open(file_to_load) as election_data:

     # To do: perform analysis.
     #print(election_data)

# Expected output: 
# _io.TextIOWrapper name='Resources/election_results.csv' mode='r' encoding='cp1252'>
# io here refers to python class that will let us read/write
# name is the path of the file object
# UTF-8 is telling it to read the file

#import csv
#import os
# Assign a variable for the file to load and the path.
#file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
#with open(file_to_load) as election_data:

    # Print the file object.
     #print(election_data)

# expected output of open file 'Resources/election_results.csv', mode 'r' at 0x10479c780>

# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
#open(file_to_save, "w")


########

# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")

# Use the open statement to open the file as a text file.
#outfile = open(file_to_save, "w")
# Write some data to the file.
#outfile.write("Hello World")

# Close the file
#outfile.close()

# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    #txt_file.write("Hello World")

   # Write three counties to the file.
   # we use the n function to use a newline escape sequence 
   # the n will create a newline
     #txt_file.write("Arapahoe\nDenver\nJefferson")
#####
# Start of reading election results

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
# Read the file object with the reader function.
    file_reader = csv.reader(election_data)

 # Print each row in the CSV file.
 # prints out as a list
 # runs all rows from the CSV data
    #for row in file_reader:
        #print(row)   
        # will bring back first item in each row or in this case our ballot ID 
        #print(row[0])

    # Print the header row and skip it!
    headers = next(file_reader)
    print(headers)
    