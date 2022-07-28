# K-Means Clustering Algorithm
# Data Mining and Warehousing [CS-2376] | Spring 2021 | Ashoka University
# Group 'BSOD' : Rishabh Goswami, Mohammed Zahir Ali, Shreyash Naman

# importing required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plot

class KMeans:
  def __init__(self, k, iterations): #initialise the parameters
    self.k = k #number of clusters/cluster centers
    self.iterations = iterations #maximum number of iterations          

  def clustering(self, data): #initialise clusters
    
    self.centers = {} #create an empty dictionary for cluster centers
    print("Brew a tea while we process your data.")
    for i in range(self.k):
      self.centers[i] = data[i] #choose the first k items in the dataset as the initial cluster centers

    for i in range(self.iterations):
      self.cluster = {}

      for i in range(self.k):
        self.cluster[i] = [] 
      
      self.assignCluster(data)

  def assignCluster(self, data): #function to assign a datapoint to a cluster

    for points in data:
        
      distances = [np.linalg.norm(points - self.centers[center]) for center in self.centers] #calculate the distance of a datapoint from all cluster centres, and store in an array
      
      kIndex = distances.index(min(distances)) #choose the lowest value (least distance) from the array
      self.cluster[kIndex].append(points) #add the point to cluster with the same index as least distance value
        
    self.newCenter()

  def newCenter(self):

    for kIndex in self.cluster: #calculate new cluster centre based on average of all points in the cluster
      self.centers[kIndex] = np.average(self.cluster[kIndex], axis=0)

  
def importData(path, col1, col2): #function to import dataset
  frame = pd.read_csv(path) #read csv file from path using pandas and copy all data into dataframe
  frame = frame[[col1,col2]] #isolate two columns of interest from the dataset
  frame = frame.dropna() #drop all datapoints with missing values
 
  ds = frame.values 
  return ds

def scatterPlot(dataset, k, iterations):

  colors = [ "orange", "cyan", "blue", "pink", "olive","red", "brown", "gray", "green", "purple"] #specifying colors for clusters

  kmean = KMeans(k, iterations) #specifying parameters - k clusters and number of iterations
  kmean.clustering(dataset) 
  print("Data Processing is done.")
  
  
  print("Please wait while we plot your data. This may take a while...")
  for kIndex in kmean.cluster:
   
    color = colors[kIndex] #assign different color to each cluster

    for point in kmean.cluster[kIndex]:
      plot.scatter(point[0], point[1], color = color, s = 35) #plotting points
  
  
  for center in kmean.centers:
    plot.scatter(kmean.centers[center][0], kmean.centers[center][1], s= 120, marker = 'x', color = 'black')   #plotting cluster centers
  
  print('Done!')
  plot.show()
 
def main():
  
  # ImportData function takes "file path, col1 and col2" as parameters and returns a dataframe to process the data
   dataset = importData("crime_2k.csv", 'latitude','longitude')
   
   # scatterPlot function processes the data by appling k-mean algorithm and plot a graph.
   # This function takes "dataset k value and number of iterations as parameters
   scatterPlot(dataset, 8, 100)
  

if __name__ == "__main__":
  main()