import csv
import random
import math
import operator

def loadDataset(filename, split, trainingSet=[] , testSet=[]):
	with open(filename, 'r') as csvfile:
	    lines = csv.reader(csvfile)
	    dataset = list(lines)
	    for x in range(len(dataset)-1):
	        for y in range(4):
	            dataset[x][y] = float(dataset[x][y])
	        if random.random() < split:
	            trainingSet.append(dataset[x])
	        else:
	            testSet.append(dataset[x])

'''euclideanDistance'''
def euclideanDistance(instance1, instance2, length):
	distance=0
	for x in range(length):
		distance += pow((instance1[x]-instance2[x]),2)
	distance=math.sqrt(distance)
	return distance

'''manhattan distance'''
def manhattan(x,y,length):
	distance=0
	for i in range(length):
		distance += abs(x[i]-y[i])
	return distance

'''chessboard distance'''
def chessboard(x,y,length):
	p=[]
	for i in range(length):
		p.append(abs(x[i]-y[i]))
	return max(p)

def getNeighbors(trainingSet, testInstance, k):
	distances = []
	distances1 = []
	distances2 = []
	distances3 = []
	length = len(testInstance)-1
	for x in range(len(trainingSet)):
		dist1 = euclideanDistance(testInstance, trainingSet[x], length)
		dist2 = manhattan(testInstance, trainingSet[x],length)
		dist3 = chessboard(testInstance, trainingSet[x],length)
		distances1.append((trainingSet[x], dist1))
		distances2.append((trainingSet[x], dist2))
		distances3.append((trainingSet[x], dist3))
	distances1.sort(key=operator.itemgetter(1))
	distances2.sort(key=operator.itemgetter(1))
	distances3.sort(key=operator.itemgetter(1))
	# print('distance', distances1,distances2,distances3)
	neighbors = []
	neighbors1 = []
	neighbors2 = []
	neighbors3 = []

	for x in range(k):
		neighbors1.append(distances1[x][0])
		neighbors2.append(distances2[x][0])
		neighbors3.append(distances3[x][0])
	neighbors=[neighbors1,neighbors2,neighbors3]
	return neighbors

def getResponse(neighbors):
	neighbors1=neighbors[0]
	neighbors2=neighbors[1]
	neighbors3=neighbors[2]
	classVotes1 = {}
	classVotes2 = {}
	classVotes3 = {}
	for x in range(len(neighbors1)):
		response1 = neighbors1[x][-1]
		if response1 in classVotes1:
			classVotes1[response1] += 1
		else:
			classVotes1[response1] = 1
	sortedVotes1 = sorted(classVotes1.items(), key=operator.itemgetter(1), reverse=True)
	for x in range(len(neighbors2)):
		response2 = neighbors2[x][-1]
		if response2 in classVotes2:
			classVotes2[response2] += 1
		else:
			classVotes2[response2] = 1
	sortedVotes2 = sorted(classVotes2.items(), key=operator.itemgetter(1), reverse=True)
	for x in range(len(neighbors3)):
		response3 = neighbors3[x][-1]
		if response3 in classVotes3:
			classVotes3[response3] += 1
		else:
			classVotes3[response3] = 1
	sortedVotes3 = sorted(classVotes1.items(), key=operator.itemgetter(1), reverse=True)
	sortedVotes=[sortedVotes1[0][0],sortedVotes2[0][0],sortedVotes3[0][0]]
	# print(sortedVotes)
	return sortedVotes

def getAccuracy(testSet, predictions):
	correct = 0
	for x in range(len(testSet)):
		if testSet[x][-1] == predictions[x]:
			correct += 1
	return (correct/float(len(testSet))) * 100.0

def main():
	# prepare data
	trainingSet=[]
	testSet=[]
	split = 0.67
	loadDataset('F:\data-analytics\iris.data', split, trainingSet, testSet)
	print ('Train set: ' + repr(len(trainingSet)))
	print ('Test set: ' + repr(len(testSet)))
	# generate predictions
	predictions=[]
	predictions1=[]
	predictions2=[]
	predictions3=[]
	# k = round(math.sqrt(len(trainingSet)))
	k=3
	print(k)
	print('\n')
	for x in range(len(testSet)):
		neighbors = getNeighbors(trainingSet, testSet[x], k)
		# print(neighbors)
		result = getResponse(neighbors)
		# print(result)
		result1=result[0]
		result2=result[1]
		result3=result[2]
		predictions1.append(result1)
		predictions2.append(result2)
		predictions3.append(result3)

		print('> predicted1=' + repr(result1) + ', actual1=' + repr(testSet[x][-1]))
		print('> predicted2=' + repr(result2) + ', actual2=' + repr(testSet[x][-1]))
		print('> predicted3=' + repr(result3) + ', actual3=' + repr(testSet[x][-1]))
	# print(predictions1)
	# print(predictions2)
	# print(predictions3)
	accuracy1 = getAccuracy(testSet, predictions1)
	accuracy2 = getAccuracy(testSet, predictions2)
	accuracy3 = getAccuracy(testSet, predictions3)
	print('Accuracy1: ' + repr(accuracy1) + '%')
	print('Accuracy2: ' + repr(accuracy2) + '%')
	print('Accuracy3: ' + repr(accuracy3) + '%')

main()
