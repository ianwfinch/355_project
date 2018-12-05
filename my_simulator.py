#!/usr/bin/python
import sys
import re

#opens the specified file
args = sys.argv
sim = args[1]
debug = 0

#inputfile = open(args[2], "r")

sim = open(sim, "r")

#sets number of possible states, strips leading characters

numStates = sim.readline().rstrip('\n')
numStates = numStates[18:]
numStates = int(numStates)

if debug:
    print(numStates)

#sets number of accepted states, read as a dict (unordered list)

accStates = sim.readline().rstrip('\n')
accStates = accStates[18:]
accStates = accStates.split(' ')
accStates = map(int, accStates)

if debug:
    print(accStates)

#sets alphabet of characters, read as a string

alphabet = sim.readline().rstrip('\n')
alphabet = alphabet[10:]
if debug:
    print(alphabet)

#add a node for each new line in the file
#must add a head for each character in alphabet

i = 1
nodeList = []
for i in range(numStates):
    foo = sim.readline().rstrip('\n')
    foo = foo.split(' ')
    thisNode = []
    j = 1
    for j in range(len(alphabet)):
        thisNode.append(int(foo[j]))
    nodeList.append(thisNode)
if debug:
    print(nodeList)

sim.close

strings = args[2]
strings = open(strings, "r")
i = 1
while True:
    currString = strings.readline().rstrip('\n')
    if currString == '':
        break
    currState = nodeList[0]
    if debug:         
        print('current string is '+ currString)
    for k in currString:
        if debug:
            print("char "+ k)
        
        for i in range(len(alphabet)):
            if alphabet[i]==k:
                currStateNum = currState[i]
                if debug:
                    print("Go to state "+ str(currStateNum))
                currState = nodeList[currStateNum]
            #else:
                #print("char doesn't exist"
    if any(currStateNum in accStates for i in accStates):
        if debug:
            print("string " + currString + " accepts")
        else:
            print("accept")
    else:
        if debug:
            print("string " + currString + " rejects")
        else:
            print("rejects")

        
