import csv
import pandas as pd

inputcsv = open('C:\\Users\Castiel\Desktop\inputcsv.csv', 'w', encoding = 'utf-8')
with open("C:\\Users\Castiel\Desktop\inputs.txt", 'r') as inputfile:
    input = inputfile.readlines()
    #print(input)
    list = []
    for line in input:
        listline= line.replace('\n\n','\n').split()
        if not line.isspace():
            list.append(line.split())
    for eachval in list:
        csvline = ','.join(eachval)
        inputcsv.write(csvline + '\n')
inputfile.close()
inputcsv.close()
df = pd.read_csv('C:\\Users\Castiel\Desktop\inputcsv.csv')
df2 = df.groupby(['Date', 'IP', 'State']).size()
df2.to_csv('C:\\Users\Castiel\Desktop\output.csv', header=["Count"])
with open('C:\\Users\Castiel\Desktop\output.csv', newline='') as File:
   print(File.read().replace(',', '\t'))

    




