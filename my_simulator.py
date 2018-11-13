#!/usr/bin/python
import sys

#opens the specified file
args = sys.argv
sim = open(args[1], "r")

#sets number of possible states, strips leading characters
numStates = sim.readline().rstrip('\n')
numStates = numStates[18:]
numStates = int(numStates)
#print(f'number of states: {numStates}')

#sets number of accepted states, read as a list
accStates = sim.readline().rstrip('\n')
accStates = accStates[18:]
accStates = accStates.split(' ')
accStates = map(int, accStates)
#print(f'accepted states: {accStates}')

#sets alphabet of characters, read as a string
alphabet = sim.readline().rstrip('\n')
alphabet = alphabet[10:]
#print(f'alphabet: {alphabet}')

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

#print(f'table: {nodeList}')
sim.close()
        

#inputfile = open(args[2], "r")
