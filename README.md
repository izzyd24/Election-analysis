# Election-analysis
repo to help Tom with Colorado state election results

## Project Overview 
A Colorado elections employee gave me the following tasks to conduct an election audit for a local congressional election

1. Calculate the total number of votes cast
2. Get a complete list of candidates who recieved any votes
3. Calculate the total number of votes each candidate recieved
4. Calculate the % of votes each canddiate won 
5. Determine the winner of the election 

## Resources 
- Data source: election_results.csv
- Software: Python, VS Code

## Summary 
The analysis of the election shows: 
- There were 369,711 votes cast in the election 
- The candidates were: 
  - Charles Casper Stockham 
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were: 
  - Charles recieved 23% of the votes (85,213 votes)
  - Diana reiceved 73.8% of the votes (272,892 votes)
  - Raymon recieved 3.1% of the votes (11,606 votes) 
- The winner of election was: 
  - Diana DeGette who reiceved 73.8% of the votes with over 270,000 votes!

## Challenge 
New objectives were tasked by Seth and Tom 
1. Find the voter turnout by county 
2. Calcualte the % of votes from each county vs the total count 
3. Identify the county with the highest turnout!

## Specific Results
Use the same CSV, and leverage for loops + conditionals + logical operators to filter through their requests. 
Upon completion, make sure to save to the txt file. 
- Deliverable 1: Election results printed to the command line 
- Deliverable 2: Election results saved to the txt file
- Deliverable 3: Place all analysis of the election audit below!

## Analysis
Overview of Election audit: 
- Explain the purpose of the audit analysis w/ new requests
- The purpose of the audit analysis was to take Seth and Tom's request a step further. 
- Intially, we conducted a state (Colorado) election audit for the candidates mentioned above. 
- After our developing our first script, we were pleased to find each candidate's name, vote count, and ultimatley their percentage towards the popular vote. 
- We found Diana DeGette to be our winner by popular vote, at 73.8% of the votes recieved (272,892 votes). 
- Yet, we also wanted to better understand the underlying trends in out voter populus. 
- Seth and Tom questioned if our script could be adjusted to find the following: 
  - 1. Find the voter turnout by county; for instance, in Jefferson county do we expect a high or low voter turnout (assuming past yearly trends, we would conclude otherwise). 
  - 2. Calculate the % of votes from each county against the total count. In this step, we want to take our high/low turnout amounts and map with % similar to the candidate popular vote. 
  - 3. Finally, we aimed to find the county with the largest turnout. We suspect that once we identify this county, Denver, for instance---we may question what barriers to voting where placed in other counties or if our turnout logic is sound. (i.e. does the largest turnout as Denver make sense, as it is the biggest county of the three in our dataset?)
  - Below you will find our results. 

Election audit results: 
- Votes cast in this congressional election: 
  - 369,711 votes were cast this year. Observing past congressional data, this seems to be a comporable figure (each district averages 330,000 votes/cycle).
  - One intersting note, with Diane Degette's win at 73.8%, we saw a jump from her previous cycle in voting percentage (67% 2016). 
  - We may need to consider each candidate and district with recent historical data to understand voting trends. 
- Number of votes and % total votes by county: 
  - Jefferson: 
  - Denver: 
  - Arapahoe: 
- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
- Which county had the largest number of votes?
- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

Election audit summary: 
- provide business proposal to the commission on how this script can be used 
- provide any modifications for the election itself 
- give 2 examples total



