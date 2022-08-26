# Import the os module
import os
cwd = os.getcwd()
os.chdir(cwd)
# os.chdir(cwd+"/python")


maxNumberFrequency = 0
mostWordFrequency = ""
mydic = {}
with open("Alice.txt", "r") as f:
    for line in f:
        words = line.split()
        for word in words:
            if word in mydic:
                mydic[word] += 1
            else:
                mydic[word] = 0
mostWordFrequency = max(mydic, key=mydic.get)
maxNumberFrequency = mydic[mostWordFrequency]
print(mostWordFrequency, maxNumberFrequency)
