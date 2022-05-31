import csv
from itertools import combinations

def joinsets(set1,set2):
    set1 = list(set1)
    set2 = list(set2)
    l = len(set1)
    for i in range(0,l-1):
        if set1[i]!=set2[i]:
            return -1
    res = set1[0:l-1]
    if set1[-1]<set2[-1]:
        res.append(set1[-1])
        res.append(set2[-1])
    else:
        res.append(set2[-1])
        res.append(set1[-1])
    return res


def getcandidate(freqsets):
    final = []
    for i in range (0,len(freqsets)):
        for j in range (i+1,len(freqsets)):
            res = joinsets(freqsets[i],freqsets[j])
            if res != -1:
                final.append(res)
    return final

def prune(curset,prevfreq,len):
    final = curset.copy()
    for c in curset:
        subsets = combinations(c,len)
        for subset in subsets:
            if subset not in prevfreq:
                final.remove(c)
                break
    return final



def checkFrequent(sets,records,min_sup):
    freq = {}
    for s in sets:
        for record in records:
            if set(s).issubset(set(record)):
                if tuple(s) not in freq:
                    freq[tuple(s)] = 1
                else:
                    freq[tuple(s)] += 1 
    final = []
    for i in freq:
        if freq[i] >= min_sup:
            final.append((i))
    return final


 

# fileName = 'Test1.csv'
f = csv.reader(open('Test1.csv'))
records = list(f)
min_support = int(input("Enter minimimum support: "))

for i in records:
    while ' ' in i:
        i.remove(' ')
    while '' in i:
        i.remove('')

# print(records)    

initial_set = [
    ['I1'],
    ['I2'],
    ['I3'],
    ['I4'],
    ['I5'],
]

frequent_set = checkFrequent(initial_set,records,min_support)
k=1
print(k, "th L",frequent_set)
k=k+1

while(True):
    candidate = getcandidate(frequent_set)
    candidate = prune(candidate, frequent_set, k-1)

    frequent_set = checkFrequent(candidate, records, min_support)
    if len(frequent_set)==0:
        break
    print(k,"th L",frequent_set)
    k=k+1

