# python-challenge

Testing clone in repos folder
added 'resources' and 'analysis' folder

### PyBank ----------------------------------------------------------------

### What does this program do?

This project serves a means of calculating changes in data over time for a small company with simple accounting pratices, then
write that data out to a .txt file named budget analysis.
This file can then be used elsewhere ultimately utilizing python as a means of cleaning the data set and provifing a compacct, easy-to-ingest set of data points.
### example of output:
  Financial Analysis
  ----------------------------
  Total Months: XX
  Total: $XXX
  Average Change: $XX.XX
  Greatest Increase in Profits: Month-Year ($ XXXX)
  Greatest Decrease in Profits: Month-Year ($-XXXX)

### What was learned? - Where there Challenges?

* I learned a fair bit about how to structure the code in python to read the data that I wanted the program to execute, alongside more practice into correctly nestingblocks of code.

* Navigating to the correct folder with os.path is still a bit new and has provided a few issues with not pathing where I desire, but it's usually a small bit of syntax that trips up the code for spell before some checking takes place to fix a Quote or Comma.
* Designating the correct row to start was an issue for more time than I care to admit. I had too few desgnators for the header row meaning the loop kept starting on the header row and attempting to drop Strings into equations meant for Integers. I found out that I needed to skip the first row before the loop to avoid this issue, then set the second row as a variable start_row.

### Features to add?
I think it would be neat to be able to expand the data set to contain/display the changes occured across Quarters of the year, providing a more detailed breakdown of
how profits are changing across a year.

### PyPoll ----------------------------------------------------------------

### What does this program do?
This program reads the data from a CSV document, organizes its contents, and runs values through a series of equations to calculate and compare to find the winner of an election. PyPoll also displays the percentage of the popular votes and writes the data to a text file for future use.

### What was learned? - Were there challenges?
Cleaning up code is very important and definitely needed for a person like myself, someone that appraoches things in a sporadic fashion. For a time I was unable to export the data to the text file correctly as some pieces of code were outside of the "with open" statement in the second half of the program code becuae i thought of how to make them cofre considering that I would need to export them. After reorganization, things seemed to work well.

Empty strings are just as useful as lists when needing to store string-based data. I seem to think in lists and it was fun to consider a more specialized format for a data type.

I learned a new bit of information while researching condtional operators for python. Originally, I attempted to tackle the operations with an "If And" statement and it proved unsuccessful. Thankfully there is an " If Not In" condition that can allow you to decide operation based on what is and isnot present in a data set without having to justify an else-statement. 

### Challenges present in this exercise

* Indentation was a bugger; I'll tell you that. For a good while there were a few lines with an extra space in the front that were messing up the loops I was trying to formulate, causing the data to dislay incompletely. One example was when attempting to print the results to terminal, I wanted to have the print functions at the bottom, stacked all nice to mimic the Homework README and by doing so I was only able to display the statistics of the last Candidate because the print funtion wasnt looping with the data it needed to represent.

