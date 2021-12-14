import csv
import os

location = os.path.join(os.path.dirname(__file__),'file.csv')

with open(location, newline='',encoding='utf-8') as file:
    reader = csv.reader(file)
    data = list(reader)

wordlist = []

#lowercase list
for i in range(len(data)):
    data[i] = str(data[i]).lower()
    words = data[i].split()
    for j in range(len(words)):
        wordlist.append(words[j])


for i in range(len(wordlist)):
    if '[' in wordlist[i]:
        wordlist[i] = wordlist[i].replace("[","")
    if "'" in wordlist[i]:
        wordlist[i] = wordlist[i].replace("'","")
    if '.' in wordlist[i]:
        wordlist[i] = wordlist[i].replace(".","")
    if "]" in wordlist[i]:
        wordlist[i] = wordlist[i].replace("]","")


print(wordlist)
wordcounter = dict()

for word in wordlist:
    if word in wordcounter:
        wordcounter[word] += 1
    else:
        wordcounter[word] = 1

result = dict(sorted(wordcounter.items(),key=lambda item: item[1]))


writeLocation = os.path.join(os.path.dirname(__file__),'results.csv')

with open(writeLocation,'w', newline='',encoding='utf-8') as file:
    writer = csv.writer(file)
    for key, value in result.items():
        writer.writerow([key, value])
    file.close()
