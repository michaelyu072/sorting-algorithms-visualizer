import pygame
import random
import time


pygame.init()





'''Number of elements you want in the array'''
n = 150






blue = (51,153,255)
red = (255,0,0)
white = (255,255,255)
green = (0,255,0)
w = 800
win = pygame.display.set_mode((w,w))

class data:

	def __init__(self, value, width, gap, index):
		self.value = value
		self.color = blue
		self.y = width-self.value
		self.x = width*.20 + (gap*index+index)
		self.gap = gap
		self.width = width
		self.index = index

	def __repr__(self):
		return str(self.value)


	def getVal(self):
		return self.value

	def makeRed(self):
		self.color = red

	def reset(self):
		self.color = blue

	def setVal(self, value):
		self.value = value
		self.y = self.width-self.value

	def setIndex(self, index):
		self.index = index
		self.x = self.width*.20 + (self.gap*index+index)

	def getIndex(self):
		return self.index

	def makeGreen(self):
		self.color = green













'''functions for drawing, swapping, and checking if sorted'''

def isSorted(dataSet):
	for i in range(1,len(dataSet)):
		if dataSet[i].getVal()-dataSet[i-1].getVal()<0:
			return False
	else:
		return True

def swap(dataSet, index1, index2):
	
		dataSet[index1].setIndex(index2)
		dataSet[index2].setIndex(index1)
	
		dataSet[index1],dataSet[index2] = dataSet[index2],dataSet[index1]
		dataSet[index1].makeRed()

def masterDraw(dataSet, win):
	win.fill(white)
	for i in dataSet:
		pygame.draw.rect(win, i.color, (i.x, i.y, i.gap, i.value))
	pygame.display.update()

def makeData(num, width):
	array = []
	gap = width*.5/num
	for i in range(num):
		array.append(data(300+i, width, gap, i))
	random.shuffle(array)
	for i in range(len(array)):
		array[i].setIndex(i)
	return array



	





'''functions for merge sort'''


def merge(a,b, data):
	c = []
	p1, p2 = 0,0
	
	ind = a[p1].getIndex()
	

	while p1 < len(a) and p2 < len(b):

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		if a[p1].getVal() <= b[p2].getVal():
			c.append(a[p1])
			
			swap(data, ind, a[p1].getIndex())
			p1+=1
			ind+=1
			
		else:
			c.append(b[p2])
			
			swap(data, ind, b[p2].getIndex())
			p2+=1
			ind+=1
			

		masterDraw(data, win)
		




	if p1 == len(a): 
		for val in b[p2:]:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
			c.append(val)
			swap(data, ind, val.getIndex())
			masterDraw(data, win)
			ind+=1
			
	else:               
		for val in a[p1:]:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
			c.append(val)
			swap(data, ind, val.getIndex())
			masterDraw(data, win)
			ind+=1
			

	for i in data:
		i.reset()
	return c


def mergeSort(a, data):
  if len(a) <= 1: return a
  left, right = mergeSort(a[:len(a)//2], data), mergeSort(a[len(a)//2:], data)
  return merge(left, right, data)














'''Methods for QuickSort'''


def partition(arr, low, high, dataSet): 
      
    pivot = arr[low].getVal()
    
    f = low
    l = high
    i = low - 1
    j = high + 1
      
    while (True): 
        chicken = i
        baby = j
        for event in pygame.event.get():
        	if event.type == pygame.QUIT:
        		pygame.quit()
        

        i += 1
        dataSet[i].makeRed()
        while (arr[i].getVal() < pivot): 
            i += 1
            dataSet[i].makeRed()
            
            
              
         
        j -= 1
        dataSet[j].makeRed()
        while (arr[j].getVal() > pivot): 
            j -= 1
            dataSet[j].makeRed()
            
            
              
         
        if (i >= j): 
        	for k in range(f,l+1):
        		dataSet[k].reset()
        	dataSet[chicken].reset()
        	dataSet[baby].reset()
         	return j  
          
        swap(arr, i, j) 
        masterDraw(arr, win)  
        

    

def quickSort(arr, low, high, dataSet): 
  
    
    if (low < high): 
          
        pi = partition(arr, low, high, dataSet)  
          
         
        quickSort(arr, low, pi, dataSet)  
        quickSort(arr, pi + 1, high, dataSet)  












'''method for selection sort'''

def selectionSort(dataSet, win):

	for i in range(len(dataSet)):
		index = i

		for j in range(i+1, len(dataSet)):

			dataSet[j].makeRed()
			dataSet[j-1].reset()

			for event2 in pygame.event.get():
				if event2.type == pygame.QUIT:
					pygame.quit()


			

			if dataSet[j].getVal() < dataSet[index].getVal():
				index = dataSet[j].getIndex()

			
			masterDraw(dataSet,win)

		swap(dataSet, dataSet[i].getIndex(), index)
		dataSet[len(dataSet)-1].reset()

	for i in dataSet:
		i.reset()
	return dataSet















		


def main():
	
	dataSet = makeData(n, w)

	run = True
	
	while run:
		masterDraw(dataSet,win)
		
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				run = False

			if event.type==pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					if not isSorted(dataSet):
						if not selectionSort(dataSet, win):
							data = makeData(n,w)
							
				if event.key == pygame.K_SPACE:
					if not isSorted(dataSet):
						mergeSort(dataSet,dataSet)
					

				if event.key == pygame.K_c:
					dataSet = makeData(n, w)
		

				if event.key == pygame.K_q:

					if not isSorted(dataSet):
						quickSort(dataSet, 0, len(dataSet)-1, dataSet)
					for i in dataSet:
						i.reset()


		
	





main()
pygame.quit()
