import csv

with open('tweetsData.csv', 'r') as f:
    reader = csv.reader(f) 
    for row in reader:
        print(row)