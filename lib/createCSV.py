import csv

def createCSV(arr, fileName):
  csvFile = csv.writer(open(fileName+".csv", 'wb'))

  csvFile.writerow(["Elements,Bubble", "Quick", "Counting(3)", "Counting(10)", "Radix(10)"])
  for i in arr:
    csvFile.writerow(i)

