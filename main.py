#import csv file

import os
import csv

#Reference Python>2>Activities>11-Stu_UdemyZip

csvpath = '03-Python_Instructions_PyBank_Resources_budget_data (1).csv'  # When file you're reading  is saved in the same folder

months = []
totalGainsLosses = []
GainLosses = 0
MonthlyChangeTotal = 0
prevRow = 0
GreatestIncrease = 0
GreatestDecrease = 0

with open(csvpath, newline="") as handler:
	budgetData = csv.reader(handler, delimiter =",") #encoding =<"utf8",>
	#lines = handler.read()
	#print(lines) #prints all rows in file  #.info in pandas to get types

	for row in budgetData:  #ask Ahmed Why it skips and if there is a more efficient way???
		for row in budgetData:
			months.append(row[0])
			totalGainsLosses.append(row[1])
			MonthlyChange = int(row[1]) - prevRow
			#print ("This is my temp number : ", MonthlyChange)  From Ahmad to check values
			if MonthlyChange == 867884:
				MonthlyChange = 0
			else:
				MonthlyChange = MonthlyChange
			#print(MonthlyChange)
			MonthlyChangeTotal = MonthlyChangeTotal + int(MonthlyChange)
			#print(MonthlyChangeTotal)
			prevRow = int(row[1])
			#print(prevRow)
			GainLosses = GainLosses + int(row[1])
			if MonthlyChange > GreatestIncrease:
				GreatestIncrease = MonthlyChange
				IncreaseMonth = str(row[0])
			else:
				GreatestIncrease = GreatestIncrease
			if GreatestDecrease < MonthlyChange:
				GreatestDecrease = GreatestDecrease
			else:
				GreatestDecrease = MonthlyChange
				DecreaseMonth = str(row[0])
			
Header = "Financial Analysis"
Total_Months = "Total Months: "+str(len(months))
Total_Gain_Losses = "Total Gain/Losses: $"+str(GainLosses)
#Average_Gain_Losses = round(float(GainLosses)/float(len(months)),2)
Monthly_Change_Average = round(int(MonthlyChangeTotal)/int(len(months)),0)
#print(str(Average_Gain_Losses))
Average_Change = "Average Change: $ "+str(Monthly_Change_Average)
Greatest_Increase = "Greatest Increase in Profits: "+ str(IncreaseMonth) +"($"+str(GreatestIncrease)+")"
Greatest_Decrease = "Greatest Decrease in Profits: "+ str(DecreaseMonth) +"($"+str(GreatestDecrease)+")"
print (Total_Months)
print(Total_Gain_Losses)
print(Average_Change)
print(Greatest_Increase)
print(Greatest_Decrease)
            
textList = [Header, Total_Months,Total_Gain_Losses, str(Monthly_Change_Average), Average_Change, Greatest_Increase, Greatest_Decrease]

with open("myoutput.txt", "w", newline="") as newfile:
	for x in textList:
		newfile.write(str(x)+ '\n')
		
		# newfile.write("\n")
    #writer = csv.writer(newfile,delimiter=" ")
    #writer.writerow(["Index", "Employee", "Department"])
    #writer.writerows(roster)


'''totalMonths = int(csvpath[1])
print(totalMonths)'''
'''return("Financial Analysis")
return("---------------------------------------------------------------------")
return("Total number of months: ")
return("Net total amount of Profit/Losses: ")
return("Average of the changes in Profit/Losses: ")
return("Greatest Increase in Profits Dt/Amt: ")
return("Greatest Decrease in Losses Dt/Amt: ")'''

	