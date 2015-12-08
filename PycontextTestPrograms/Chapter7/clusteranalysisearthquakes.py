import random
import math
import turtle

def euclidD(point1, point2):
    sum = 0
    for index in range(len(point1)):
        diff = (point1[index]-point2[index]) ** 2
        sum = sum + diff
        
    euclidDistance = math.sqrt(sum)
    return euclidDistance

def readFile(filename):
    datafile = open(filename, "r")
    datadict = {}
    key = 0

    for aline in datafile:
       items = aline.split()
       key = key + 1
       lat = float(items[3])   
       lon = float(items[4])   
       datadict[key] = [lon,lat]

    return datadict


def createCentroids(k, datadict):
    centroids=[]           
    centroidCount = 0
    centroidKeys = []

    while centroidCount < k: 
       rkey = random.randint(1,len(datadict))
       if rkey not in centroidKeys:
           centroids.append(datadict[rkey])   
           centroidKeys.append(rkey)       
           centroidCount = centroidCount + 1   
           
    return centroids
    
def createClusters(k, centroids, datadict, repeats):
    for apass in range(repeats):
        print("****PASS",apass,"****")
        clusters = []                      
        for i in range(k):
           clusters.append([])             

        for akey in datadict:
           distances = []                     
           for clusterIndex in range(k):    
               dist = euclidD(datadict[akey],centroids[clusterIndex])
               distances.append(dist)       

           mindist = min(distances)         
           index = distances.index(mindist)   

           clusters[index].append(akey)     

        dimensions = len(datadict[1])      
        for clusterIndex in range(k):      
           sums = [0]*dimensions
           for akey in clusters[clusterIndex]:
               datapoints = datadict[akey]
               for ind in range(len(datapoints)):           
                   sums[ind] = sums[ind] + datapoints[ind]  
           for ind in range(len(sums)):                    
               clusterLen = len(clusters[clusterIndex])
               if clusterLen != 0:
                  sums[ind] = sums[ind]/clusterLen   
       
           centroids[clusterIndex] = sums   
           
        for c in clusters:          
           print ("CLUSTER")
           for key in c:
               print(datadict[key], end=" ")
           print()                     
           
    return clusters

def visualizeQuakes(dataFile):
    datadict = readFile(dataFile)
    quakeCentroids = createCentroids(6, datadict)
    clusters = createClusters(6, quakeCentroids, datadict, 7)
    
    quakeT = turtle.Turtle()
    quakeWin = turtle.Screen()
    quakeWin.bgpic("worldmap.gif")   
    quakeWin.screensize(448,266)     
    
    wFactor = (quakeWin.screensize()[0]/2)/180
    hFactor = (quakeWin.screensize()[1]/2)/90    

    quakeT.hideturtle()
    quakeT.up()

    colorlist = ["red","green","blue","orange","cyan","yellow"] 

    for clusterIndex in range(6):
        quakeT.color(colorlist[clusterIndex])  
        for akey in clusters[clusterIndex]:
            lon = datadict[akey][0]
            lat = datadict[akey][1]
            quakeT.goto(lon*wFactor,lat*hFactor)
            quakeT.dot()
    quakeWin.exitonclick()

visualizeQuakes("earthquakes.txt")