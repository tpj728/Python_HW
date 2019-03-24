import os
import csv

csvpath = '03-Python_Instructions_PyPoll_Resources_election_data.csv'

#voterList=[]
candidateList=[]
#countyList=[]
votesTotalCast = 0
candidateTotalCast = [0,0,0,0]
winPercent = []
electionWinner = 0
electionName ="blank"


with open (csvpath, newline = "") as handler:
	pollData = csv.reader(handler)
	#lines = handler.read() 
	#print(lines)

	for row in pollData:
		for row in pollData:
			votesTotalCast = votesTotalCast + 1
			candidateList.append(row[2])
			candidateList = list(set(candidateList))

#print(candidateList)

with open (csvpath, newline = "") as handler:
	pollData = csv.reader(handler)
	for row in pollData:
		for row in pollData:
			picked = row[2]
			picked = candidateList.index(picked)
			candidateTotalCast[picked] += 1

for row in candidateTotalCast:
	winPercent.append(round(row/votesTotalCast,4))
	#print(winPercent)

for x in range(len(candidateTotalCast)):
	print(str(candidateList[x])+": "+str(winPercent[x])+" ("+str(candidateTotalCast[x])+")")
	if electionWinner < candidateTotalCast[x]:
		electionWinner = candidateTotalCast[x]
electionWinner = candidateTotalCast.index(electionWinner)
	

finalResult = zip(candidateList,winPercent,candidateTotalCast)
finalResult = list(finalResult)


Line0 = ("\n")
Line1 = ("Election Results")
#print("\n")
Line2 = ("Total Votes: "+ str(votesTotalCast))
#print("\n")
print = (str(finalResult))

#print("\n")
Line3 = ("Winner: "+ candidateList[electionWinner])

#electionName = name
#print(electionName)

textList = [Line0, Line1, Line2, Line3]
with open("pypoll.txt", "w", newline="") as newfile:
	for x in range(len(textList)):
		newfile.write(textList[x])
	for x in range(len(textList)):
		newfile.write('\n')
		newfile.write(str(candidateList[x])+": "+str(winPercent[x])+" ("+str(candidateTotalCast[x])+")")

