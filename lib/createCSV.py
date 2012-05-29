import csv

def createCSV(arr, fileName):
  csvFile = csv.writer(open(fileName+".csv", 'wb'))

  csvFile.writerow(["elements", "1st", "2nd", "3rd", "4th", "5th"])
  for i in arr:
    csvFile.writerow(i)

