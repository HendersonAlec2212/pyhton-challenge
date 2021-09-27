import os
import csv

# files to read from
budget_data = os.path.join("Resources_PyBank", "budget_data.csv")
# files to write to
budget_analysis = os.path.join("Analysis", "budget_analysis.csv")


# set the parameters for changes
total_months = 0
month_change_list = []
net_total = 0
# consider changing variable to something shorter
net_profit_loss_change_list = []
# -------------------------------
greatest_increase = ["", 0]
greatest_decrease = ["", 1000000000]


with open(budget_data, 'r') as infile:
    csv_reader = csv.reader(infile)

    # start with next(header) before loop to skip
    header = next(csv_reader)

    # print(header) #<-- make sure you have the correct line

    # skip header row to avoid adding header data to net profit loss list
    start_row = next(csv_reader)
    total_months += 1
    # change = previous - current | x += 1 same as x = x + 1
    net_total += int(start_row[1])
    previous_net_total = int(start_row[1])

    # start loop
    for row in csv_reader:
        # track the months and total
        total_months += 1
        net_total += int(row[1])

        # track the changes in profit similar prev to current comparison as above, += to move through loop
        net_profit_loss_change = int(row[1]) - previous_net_total
        previous_net_total = int(row[1])
        net_profit_loss_change_list += [net_profit_loss_change]
        month_change_list += [row[0]]

        # set conditions for greatest increase and decrease
        if net_profit_loss_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_profit_loss_change

        if net_profit_loss_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_profit_loss_change

    # average net profit/loss change per month
    net_monthly_average = sum(net_profit_loss_change_list) / len(net_profit_loss_change_list)

    # create the output values for above data
    # \n = linebreak | \t = tab
    output_data = (
        f"Financial Analysis\n"
        f"----------------------------\n"
        f"Total Months Elapsed: {total_months}\n"
        f"Total Profit/Loss for Period: ${net_total}\n"
        f"Average Change per Month: ${net_monthly_average}\n"
        f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
        f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
    )

    print(output_data)

    with open(budget_analysis, 'w') as txt_file:
        txt_file.write(output_data)