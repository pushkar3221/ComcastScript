import csv
import pandas as pd

inputcsv = open('C:\\PycharmProjects\ComcastScript\inputcsv.csv', 'w', encoding = 'utf-8') #Cleaning raw_txt to input csv for analysis
with open("C:\\PycharmProjects\ComcastScript\inputs.txt", 'r') as inputfile:
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
df = pd.read_csv('C:\\PycharmProjects\ComcastScript\inputcsv.csv') #Using pandas for analysis of Data
df2 = df.groupby(['Date', 'IP', 'State']).size()
#print(df2)
df2.to_csv('C:\\PycharmProjects\ComcastScript\output.csv', header=["Count"]) #Generating outputfile
with open('C:\\PycharmProjects\ComcastScript\output.csv', newline='') as File:
   print(File.read().replace(',', '\t'))
File.close()

    




