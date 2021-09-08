import csv
import pandas as pd
import plotly.figure_factory as pff
import statistics
import random
import plotly.graph_objects as pgo
df=pd.read_csv("tempdata.csv")
data=df["temp"].tolist()

def randommean(counter): 
 dataset=[]
 for i in range(0,counter):
      randomdata=random.randint(0,len(data)-1)
      value=data[randomdata]
      dataset.append(value)
 mean=statistics.mean(dataset)
 return mean
 
def showgraph(meandata):
    df=meandata
    mean=statistics.mean(meandata)
    graph=pff.create_distplot([df],["Temprature"],show_hist=False)
    graph.add_trace(pgo.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="mean"))
    graph.show()
def setup():
    meanlist=[]    
    for i in range(0,1000):
        allmean=randommean(100)
        meanlist.append(allmean)
    showgraph(meanlist)    
setup()
