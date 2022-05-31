import csv

f = csv.reader(open('Test1.csv'))
records = list(f)

def getcount(item):
    count = 0
    for record in records:
        if set(item).issubset(record):
            count += 1
    return count

item1 = ['I1']
item2 = ['I2']
union = ['I1','I2']

countitem1 = getcount(item1)
countitem2 = getcount(item2)
countunion = getcount(union)

confidence = (countunion/countitem1)*100
print ("confidence: ", confidence, "%")