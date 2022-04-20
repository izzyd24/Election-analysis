# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize total_votes to zero before the for loop
total_votes = 0 
# create a new list that is empty, initalized before the for loop
candidate_options = []
# create a new dictionary before the for loop
candidate_votes = {}
#initialize our new variables to track 
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
         #print(row) 
         # when we use print (row), and do not augment by +1, we get all CSV rows
         # since we only want the final row, we use our total_votes variable
         # Augment by +1 for total_votes 
         total_votes += 1
         # column 3 = index 2, we want to reference this
         # this will print the candidates names from each row
         candidate_name = row[2]
         # to get specific names, use an if statement
         # 'not in' to exclude if it was added to the list 
         if candidate_name not in candidate_options: 
              # add it to the list!
               candidate_options.append(candidate_name)
         # use dictionary    
         # set to zero for count, then add from there  
               candidate_votes[candidate_name] = 0
          # Add a vote to that candidate's count
          # by placing outside if, but within our for loop... 
          # we can then increment each vote every time their name appears in a row    
         candidate_votes[candidate_name] += 1
# save the results to this point as a text file
with open(file_to_save, "w") as txt_file:         
# print the final vote count to the terminal 
     election_results = (
          f"\nElection Results\n"
          f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
     print(election_results, end="")
    # Save the final vote count to the text file.
     txt_file.write(election_results)
     # for loop to iterate through candidate_option[] list (get the name)
     for candidate_name in candidate_votes:
          # use for loop to get candidate_votes = {} dictionary 
          votes = candidate_votes[candidate_name]
          # calculate percentage = (votes/total_votes) *100
          vote_percentage = float(votes) / float (total_votes) * 100
          # created a variable candidate_results
          # by doing so, we add each candidate's results to the txt file
          candidate_results =(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
          # print each candidate result to output terminal
          print(candidate_results)
          # saves the candidate results to the txt file 
          txt_file.write(candidate_results)
          # Determine if the votes are greater than the winning count.
          if (votes > winning_count) and (vote_percentage > winning_percentage):
               winning_count = votes
               winning_percentage = vote_percentage
               winning_candidate = candidate_name

     # print and declare winner within the terminal
     winning_candidate_summary = (
          f"-------------------------\n"
          f"Winner: {winning_candidate}\n"
          f"Winning Vote Count: {winning_count:,}\n"
          f"Winning Percentage: {winning_percentage:.1f}%\n"
          f"-------------------------\n")
     print(winning_candidate_summary)
     # save winning candidate's name to the txt file 
     txt_file.write(winning_candidate_summary)





















