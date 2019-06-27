# '''f=open("F:\data analytics\iris.data","r")
# print(f.read())
# '''
# import csv
# import random
# import math
# import operator
# split =0.67
# trainingSet=[]
# testSet=[]
# with open("F:\data analytics\iris.data", "r") as csvfile:
#     # print(f.read())
#     lines = csv.reader(csvfile)
#     dataset = list(lines)
#     # print(dataset)
#     for x in range(len(dataset)-1):
#     # for x in range(1):
#         for y in range(4):
#             dataset[x][y] = (dataset[x][y])
#         # print(dataset)
#         if random.random() < split:
#             trainingSet.append(dataset[x])
#         else:
#             testSet.append(dataset[x])
#     print(trainingSet)
#     print(testSet)

import operator
def getResponse(neighbors):
    classVotes = {}
    # print("here")
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        print("knock")
        if response in classVotes:
            classVotes[response] += 1
            print("count")
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    print("here")
    return sortedVotes[0][0]

def main():
    neighbors = [[1,1,1,'a'], [2,2,2,'a'], [3,3,3,'b']]
    response = getResponse(neighbors)
    print(response)
    print("hello")

main()
