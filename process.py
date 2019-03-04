import csv
field=[]
with open('EXCEL-MITS.csv') as csvfile:
    spamreader = csv.reader(csvfile, dialect='excel')
    for row in spamreader:
        strin = row[0] + ' ' + row[1] + 'τμ ' + row[2] + ' ' + row[3] + ' ' + row[4]
        if (row[5] != ''):
            strin = strin + ' (σύζυγος ' + row[5] + ')'
        if (row[7] != ''):
            strin = strin + ' (πατέρας ' + row[7] + ')'
        if (row[8] == 'ΝΑΙ'):
            strin = strin + ' (έχει συνιδιοκτήτες)'
        field.append(strin)

f = open("ANADASMOS-PETROKERASA.kml", "r")
input = f.read()
for i in range(1,587):
    search = '<name>'+str(i)+'</name>'
    input = input.replace(search, '<name>'+field[i-1]+'</name>')

f2 = open("new.kml", "w")
f2.write(input)
