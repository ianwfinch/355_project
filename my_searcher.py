#Ian Finch
#Started 12/5/18

#!/usr/bin/python
import sys

args = sys.argv
strFile = args[1]
strFile = open(strFile, "r")
myStr = strFile.readline().rstrip('\n')
alphabet = 'abcdefghijklmnopqrstuvwxyz'
nodeList = []

print("Number of states: " + str(len(myStr)+1))
print("Accepting states: " + str(len(myStr)))
print("Alphabet: " + alphabet)

for i in range(len(myStr)):
    currNode = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    myChar = myStr[i]

    for j in range(len(alphabet)):

        #this block finds patterns that match with the beginning of the string
        for k in range(len(myStr)-i):
            lookfor = myStr[i-k:i]+alphabet[j]
            if myStr.startswith(lookfor) and currNode[j] == 0:
                currNode[j] = len(lookfor)

        if myChar == alphabet[j]:
            currNode[j] = i+1
    
    #just prints the current node
    for k in currNode:
        print k,
    print
    
a = len(myStr)
finalnode = ([a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a])

#creates the loop on the final state so anything after the substring will accept

for x in finalnode:
    print x,
print