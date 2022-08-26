# Import the os module
import os
cwd = os.getcwd()
# os.chdir(cwd+"/python") # for debugpy
os.chdir(cwd)
maxNumberFrequency = 0
mostWordFrequency = ""
mydic = {}
with open("Alice.txt", "r") as f:
    lines = f.read()
    Words = lines.split()
    for word in Words:
        if word in mydic:
            mydic[word] += 1
        else:
            mydic[word] = 0
mostWordFrequency = max(mydic, key=mydic.get)
maxNumberFrequency = mydic[mostWordFrequency]
print(mostWordFrequency, maxNumberFrequency)
