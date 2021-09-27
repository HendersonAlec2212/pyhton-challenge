# pyhton-challenge

Testing clone in repos folder
added 'resources' and 'analysis' folder

### PyBank ----------------------------------------------------------------


### What doe sthis program do?

This project serves a means of calculating changes in data over time for a small company with simple accounting pratices, then
write that data out to a .txt file named budget_analysis.
This file can then be used elsewhere ultimately utilizing python as a means of cleaning the data set and provifing a compacct, easy-to-ingest set of data points.
### example of output:
  Financial Analysis
  ----------------------------
  Total Months: XX
  Total: $XXX
  Average  Change: $XX.XX
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
What was your motivation?
Why did you build this project?
What problem does it solve?
What did you learn?
What makes your project stand out? If your project has a lot of features, consider adding a "Features" section and listing them here.