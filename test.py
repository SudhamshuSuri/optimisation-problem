import csv
import numpy as np
from geneticalgorithm2 import geneticalgorithm2 as ga
import sys
varbound = ((-sys.maxsize, sys.maxsize), (-sys.maxsize, sys.maxsize))

###----------------------------------------------READING INPUT CSV FILE--------------------------------------###
points = csv.reader(open('.geneticalgorithms\points.csv'), delimiter=',')
a = [(eval(x), eval(y)) for (x,y) in points]

###---------------------------------SETTING UP LINESEGLIST VARIABLE LIST AND ENDPOINT------------------------###
endpoint = np.array(a[-1])
a = a[:-1]

lineseglist = []
i = 0
while i in range(0, len(a)-1):
    lineseglist.append(np.array([a[i], a[i+1]]))
    i+=2

varlist = []
for i in range(len(lineseglist)):
    varlist.append(np.random.rand(2))

###----------------------------------------OBJECTIVE FUNCTION AND HELPER FUNCTIONS---------------------------###
def func(varlist, endpoint):
    for i in range(0, len(varlist)):
        if isBetween(lineseglist[i][0], lineseglist[i][1], varlist[i]):
            sum = 0
            j = 0
            while j in range(0, len(varlist)-1):
                sum += np.linalg.norm(varlist[i+1]- varlist[i])
                j += 1
            sum += np.linalg.norm(endpoint - varlist[-1])    
            return sum


def isBetween(point1, point2, point3):
    # Calculate the distances between the points along each dimension
    distances = np.abs(point2 - point1)
    # Find the minimum and maximum values for each dimension
    min_values = np.minimum(point1, point2)
    max_values = np.maximum(point1, point2)
    # Check if point3 lies within the minimum and maximum values along each dimension
    between = np.all((point3 >= min_values) & (point3 <= max_values))
    return between

###---------------------------------------- SETTING UP MODEL ----------------------------------###
model = ga(function=func, dimension = 2, variable_type='real',variable_boundaries=varbound)

###----------------------------------------------RUNNING THE MODEL-------------------------------------------###
model.run()