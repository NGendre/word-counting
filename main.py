import csv
import os


#read file
location = os.path.join(os.path.dirname(__file__),'file.csv')

with open(location, newline='',encoding='utf-8') as file:
    reader = csv.reader(file)
    data = list(reader)

wordlist = []
print(data)
#lowercase list
for i in range(len(data)):
    data[i] = str(data[i]).lower()
    words = data[i].split()
    for j in range(len(words)):
        wordlist.append(words[j])

#remove characters from str (there might be a better way to do this
for i in range(len(wordlist)):
    if '[' in wordlist[i]:
        wordlist[i] = wordlist[i].replace("[","")
    if "'" in wordlist[i]:
        wordlist[i] = wordlist[i].replace("'","")
    if '.' in wordlist[i]:
        wordlist[i] = wordlist[i].replace(".","")
    if "]" in wordlist[i]:
        wordlist[i] = wordlist[i].replace("]","")
    if ',' in wordlist[i]:
        wordlist[i] = wordlist[i].replace(",","")


#creates a dict
wordcounter = dict()

for word in wordlist:
    if word in wordcounter:
        wordcounter[word] += 1
    else:
        wordcounter[word] = 1


result = dict(sorted(wordcounter.items(),key=lambda item: item[1]))


#TODO sort by decreasing order
print("Writing Results")
writeLocation = os.path.join(os.path.dirname(__file__), 'result.csv')

with open(writeLocation,'w', newline='',encoding='utf-8') as file:
    writer = csv.writer(file)
    for key, value in result.items():
        writer.writerow([key, value])
    file.close()
