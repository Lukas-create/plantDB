import csv

def searchByHabitat():
    Habitat=input('Enter name of habitat\n')
    csv_file=csv.reader(open('Pflanzendaten.csv','r'))

    for row in csv_file:
        if Habitat==row[5]:
            print(row)

print('Enter 1 to seach by Habitat')

src=int(input('Enter here:'))

if src==1:
    searchByHabitat()
else:
    print('no data')