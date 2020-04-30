import pickle
from sklearn import linear_model
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import os


#Run this program in linux command line rather than here.
# This program will read line by line of names2 and extract XY coordinates from screen 

os.system(" ./darknet detect cfg/yolov3.cfg yolov3.weights dataset/1.jpg")
def predict(x_mid,y_mid):
 pickle_in=open("dict.pickle","rb")
 regr=pickle.load(pickle_in)
 x=regr.predict([[x_mid,y_mid]])
 pickle_in.close()
 pickle_in=open("dict1.pickle","rb")
 regr=pickle.load(pickle_in)
 y=regr.predict([[x_mid,y_mid]])
 pickle_in.close()
 return(x,y)
 
def search_keyword_person(line):
    v=line.split(':')
    if v[0]=='person':
        return(1)
    else:
        return(0)
    
def parser(string):
    q=string.split(':')
    q=q[1].split(',')
    ak_lis=[]
    for i in q:
        j=i.split('=')
        ak_lis.append(int(j[1]))
    return(ak_lis)   
    
fh = open('coo_extract','r')

k=0
count=0
imp_lis=[]
while True:
    line = fh.readline()
    j=search_keyword_person(line)
    if j==1:
        imp_lis.append(k+2)
        count=count+1
    if not line:
        #print(count)
        break
    k=k+1

fh.close()
with open("coo_extract") as f:
    lines = f.readlines()
coo_lis=[]
for i  in imp_lis:
    v=parser(lines[int(i)-1])
    coo_lis.append(v)
f.close()

#print(coo_lis,' count : '+str(count))
#print(coo_lis)
for i in coo_lis:
    a=(i[0]+i[2])/2
    b=(i[1]+i[3])/2
    x,y=predict(int(a),int(b))
    print(x,y)
    
f = open("coo_extract", "w")
f.close()

    
