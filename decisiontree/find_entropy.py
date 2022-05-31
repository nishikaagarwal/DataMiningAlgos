import pandas as pd
import numpy as np

df = pd.read_csv('tennis.csv')

classa = df.keys()[-1]
entropymain = 0
values = df[classa].unique()
for value in values:
    fraction = df[classa].value_counts()[value]/len(df[classa])
    entropymain += -fraction*np.log2(fraction)

print(entropymain)

def attribute_entropy(df,attribute):
    classa = df.keys()[-1]
    variables = df[attribute].unique()
    targets = df[classa].unique()
    finalentropy = 0
    for variable in variables:
        entropy = 0
        for target in targets:
            num=len(df[attribute][df[attribute]==variable][df[classa]==target])
            den = len(df[attribute][df[attribute]==variable])
            fraction = num/(den+eps)
            entropy += -fraction*np.log2(fraction+eps)
        fraction2 = den/len(df)
        finalentropy += fraction2*entropy
    return finalentropy

eps = np.finfo(float).eps
info_gain = []
for key in df.keys()[:-1]:
    info_gain.append(entropymain - attribute_entropy(df,key))

print(info_gain)
max = df.keys()[:-1][np.argmax(info_gain)]
print(max)

