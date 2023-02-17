#___________________________<-- Siddharth Singh Chouhan -- M15117156 -->___________________________
import socket
import collections
import os
import string

result= open("/home/output/result.txt", "w+")
path = "/home/data"
dir_list = os.listdir(path)
print(dir_list)
result.write(" \n")
result.write(str(dir_list))

file1 = open("/home/data/Limerick.txt","r")
file2 = open("/home/data/IF.txt","r")

data1 = file1.read()
words1 = data1.split()
result.write(" \n")
result.write("Total number of words in Limerick-3.txt:")
result.write(str(len(words1)))

data2 = file2.read()
words2 = data2.split()
result.write(" \n")
result.write("Total number of words in IF.txt:")
result.write(str(len(words2)))

total=len(words1)+len(words2)
result.write(" \n")
result.write("Total number of words in both files:",)
result.write(str(total))

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
result.write("\n")
result.write("Your Computer's IP Address is:" )
result.write(str(IPAddr))

def word_count(str):
    counts = dict()
    words = str.split()
    for word in words:
        word = word.translate(str.maketrans('', '', string.punctuation))
        word = word.capitalize()
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    x=dict(sorted(counts.items(), key=lambda item: item[1],reverse=True))
    out = dict(list(x.items())[0: 3])
    return out

result.write(" \n")
result.write("Top 3 words with maximum number of counts in IF.txt")
result.write(str(word_count(data2)))
result.close()
result_file = open('/home/output/result.txt','r')
data_result = result_file.read()
print(data_result)