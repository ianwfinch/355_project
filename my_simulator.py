#!/usr/bin/python

#opens the specified file
sim = open("simulator.txt", "r")

#sets number of possible states, strips leading characters
numStates = sim.readline().rstrip('\n')
numStates = numStates[18:]
numStates = int(numStates)
print(numStates)

#sets number of accepted states, read as a dict (unordered list)
accStates = sim.readline().rstrip('\n')
accStates = accStates[18:]
accStates = accStates.split(' ')
print(accStates)

#sets alphabet of characters, read as a string
alphabet = sim.readline().rstrip('\n')
alphabet = alphabet[10:]
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
        thisNode.append(foo[j])
    nodeList.append(thisNode)

print(nodeList)
        

