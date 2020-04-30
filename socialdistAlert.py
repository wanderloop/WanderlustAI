import numpy as np
from datetime import datetime
import math
from twilio.rest import Client

account_sid = 'AC19c5f9d669be0ab9b93c2f27c11fd17c'
auth_token = '4d1170aa069d44a5f70df6feba71f740'
client = Client(account_sid, auth_token)

def continous_check(IDForsms):
    

 def Union(lst1, lst2): 
     final_list = list(set(lst1) | set(lst2)) 
     return final_list 

 def distance(lat1, lon1, lat2, lon2,u):
 
     radius = 6371 # km

     dlat = math.radians(lat2-lat1)
     dlon = math.radians(lon2-lon1)
     a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
     c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
     d = radius * c
     if d<u:
         return(True)
     else:
         return(False)



 def date_time_match_check(time1,date1,time2,date2,goku):

  def date_time_match(time1,date1,time2,date2):

   def date_time(time,date):
    
    def time_split(time):
     x=time.split(':')
     return(int(x[0]),int(x[1]))

    def date_split(date):
        k=date.split('/')
        return(int(k[1]),int(k[0]))
    
    m,n=time_split(time)
    g,h=date_split(date)
 
    day1 = datetime(2020, h, g, m, n, 0)
    return(day1)
 

 
   day1=date_time(time1,date1)

 
   day2 = date_time(time2,date2)
   diff = day1-day2

   e=str(diff).split('days')
   e=e[0].split(':')
   #print(e)
   hrs=int(e[0])
   mins=int(e[1])
   secs=int(e[0])

   if hrs<1:
       if mins<goku:
           return('True')
       else:
           return('False')

   else:
       return('False')

  try:
      x=date_time_match(time1,date1,time2,date2)
      return(x)
  except:
      return('False')


 def string_ParseTo_Float(mystring):
  alist=[]
  k=mystring.split("X:")
  j=k[0]
  

  x=j.split("ID:")
  j=x[1]
  ID=j
  m=k[1].split("Y:")
  long=m[0]
  n=m[1].split("TIME:")
  lat=n[0]
  c=n[1].split("DATE: ")
  time=c[0]
  date=c[1]
  return(ID,long,lat,time,date)



 with open('/home/ahmed/Desktop/tester') as f:
     content = f.readlines()
 content = [x.strip() for x in content]

 j=0
 rows, cols = (len(content), 5) 
 arr = [[0]*cols]*rows 

 IDLis=[]
 longLis=[]
 latLis=[]
 timeLis=[]
 dateLis=[]

 for i in range(1,len(content)):
  ID,long,lat,time,date=string_ParseTo_Float(content[i]) 
  IDLis.append(ID)
  longLis.append(long)
  latLis.append(lat)
  timeLis.append(time)
  dateLis.append(date)


 item=IDForsms

 def find(item,where):
  j=0
  note=[]
  item=' '+item+' ' # yeh srf notepad data key liye hai baad mein remove kardena
  for i in where:
      if i==item:
          note.append(j)
          j=j+1
      else:
          j=j+1

  return(note)

 y=find(item,IDLis)
 #print(y)

 #Generate list1 backward

 def backward(y):
  note=[]
  for i in y:
      note.append(int(i)-1)
  return(note)

 note=backward(y)
 #print(note)

 def forward(y):
  note=[]
  for i in y:
      note.append(int(i)+1)
  return(note)

 note=forward(y)
 #print(note)



 #------------------------
 #all values of dates of infected person (General)
 inf_Gen_dates=[]
 for i in y:
     inf_Gen_dates.append(dateLis[int(i)])


 #print(inf_Gen_dates)

 inf_Gen_time=[]
 for i in y:
     inf_Gen_time.append(timeLis[int(i)])
    
 #print(inf_Gen_time)
    
 #--------------------------------
 #all values of dates of close_match person(Backward)
 note=backward(y)
 inf_back_dates=[]
 for i in note:
     inf_back_dates.append(dateLis[int(i)])

 
 #print(inf_back_dates)

 inf_back_time=[]
 for i in note:
     inf_back_time.append(timeLis[int(i)])
    
 #print(inf_back_time)

 #-------------------------------------------------
 #Back dates and time matchup with general

 h=0
 date_time_result=[]
 goku=1
 for i in range(0,len(y)):
     s=date_time_match_check(inf_Gen_time[h],inf_Gen_dates[h],inf_back_time[h],inf_back_dates[h],int(goku))
     date_time_result.append(s)
     h=h+1
    
    
 #print(date_time_result)
 #--------------------------------------------------------extracting True Positives for further proceeding
 posLis=[]
 q=0
 for i in date_time_result:
     if i=='True':
         posLis.append(q)
         q=q+1
     else:
         q=q+1

 #print(posLis)

 new_lis=[]
 for i in posLis:
     new_lis.append(y[i])
    
 #print(new_lis)
 y=new_lis
 #print(y)

 #--------------------------------------------------
 #Now we test distance--------------------------------General Distance
 inf_Gen_longitude=[]
 for i in y:
     inf_Gen_longitude.append(longLis[int(i)])
 #print(inf_Gen_longitude)

 #-----------------------------------------------------latititude

 inf_Gen_latitude=[]
 for i in y:
     inf_Gen_latitude.append(latLis[int(i)])
 #print(inf_Gen_latitude)

 #---------------------------------------------------Backaward longitude
 inf_Gen_longitude_back=[]
 note=backward(y)
 for i in note:
     inf_Gen_longitude_back.append(longLis[int(i)])
 #print(inf_Gen_longitude_back)

 #--------------------------------------------------Backward latitude

 inf_Gen_latitude_back=[]
 note=backward(y)
 for i in note:
     inf_Gen_latitude_back.append(latLis[int(i)])
 #print(inf_Gen_latitude_back)

 #------------------------------------------------------------Distnace calculation (General vs Backward)



 #x=distance(lat1, lon1, lat2, lon2)
 #print(x)

 h=0
 lat_long_result_backward=[]
 u=1
 for i in range(0,len(y)):
     s=distance(float(inf_Gen_longitude[h]),float(inf_Gen_latitude[h]),float(inf_Gen_longitude_back[h]), float(inf_Gen_latitude_back[h]),float(u))
     lat_long_result_backward.append(s)
     h=h+1

 #print(lat_long_result_backward)

 #----------------------------from sucessful TRUE extracting the ID Values
 f=0
 note=backward(y)
 imp_ret=[]
 for i in  lat_long_result_backward:
     if i==True:
         imp_ret.append(IDLis[note[f]])
         f=f+1
     else:
         f=f+1
        
 #print('BACKWARD RESULT')
 #print(imp_ret)
 BACKWARD_RESULT=imp_ret

 #---------------------------------------------------------------------------
 #STEPS FOR FORWARD CHECK
 #-----------------------------------------------------------------------
 #-----------------------------------------------------------------------
 #-----------------------------------------------------------------------
 #-----------------------------------------------------------------------
 #-----------------------------------------------------------------------
 def find(item,where):
  j=0
  note=[]
  item=' '+item+' ' # yeh srf notepad data key liye hai baad mein remove kardena
  for i in where:
      if i==item:
          note.append(j)
          j=j+1
      else:
          j=j+1

  return(note)

 y=find(item,IDLis)
 #print(y)

 def forward(y):
  note=[]
  for i in y:
      note.append(int(i)+1)
  return(note)

 note=forward(y)
 #print(note)




 #------------------------
 #all values of dates of infected person (General)
 inf_Gen_dates=[]
 for i in y:
     inf_Gen_dates.append(dateLis[int(i)])


 #print(inf_Gen_dates)

 inf_Gen_time=[]
 for i in y:
     inf_Gen_time.append(timeLis[int(i)])
    
 #print(inf_Gen_time)
    
 #--------------------------------
 #all values of dates of close_match person(Forward)
 note=forward(y)
 inf_forward_dates=[]
 for i in note:
     inf_forward_dates.append(dateLis[int(i)])


 #print(inf_back_dates)

 inf_forward_time=[]
 for i in note:
     inf_forward_time.append(timeLis[int(i)])
    
 #print(inf_back_time)
 
 #-------------------------------------------------
 #Back dates and time matchup with general

 h=0
 date_time_result=[]
 goku=1
 for i in range(0,len(y)):
     s=date_time_match_check(inf_Gen_time[h],inf_Gen_dates[h],inf_forward_time[h],inf_forward_dates[h],int(goku))
     date_time_result.append(s)
     h=h+1
    
    
 #print(date_time_result)
 #--------------------------------------------------------extracting True Positives for further proceeding
 posLis=[]
 q=0
 for i in date_time_result:
     if i=='True':
         posLis.append(q)
         q=q+1
     else:
         q=q+1

 #print(posLis)

 new_lis=[]
 for i in posLis:
     new_lis.append(y[i])
    
 #print(new_lis)
 y=new_lis
 #print(y)

 #--------------------------------------------------
 #Now we test distance--------------------------------General Distance
 inf_Gen_longitude=[]
 for i in y:
     inf_Gen_longitude.append(longLis[int(i)])
 #print(inf_Gen_longitude)

 #-----------------------------------------------------latititude

 inf_Gen_latitude=[]
 for i in y:
     inf_Gen_latitude.append(latLis[int(i)])
 #print(inf_Gen_latitude)

 #---------------------------------------------------forward longitude
 inf_Gen_longitude_forward=[]
 note=forward(y)
 for i in note:
     inf_Gen_longitude_forward.append(longLis[int(i)])
 #print(inf_Gen_longitude_back)

 #--------------------------------------------------forward latitude

 inf_Gen_latitude_forward=[]
 note=forward(y)
 for i in note:
     inf_Gen_latitude_forward.append(latLis[int(i)])
 #print(inf_Gen_latitude_back)

 #------------------------------------------------------------Distnace calculation (General vs Backward)



 #x=distance(lat1, lon1, lat2, lon2)
 #print(x)

 h=0
 lat_long_result_forward=[]
 u=1
 for i in range(0,len(y)):
     s=distance(float(inf_Gen_longitude[h]),float(inf_Gen_latitude[h]),float(inf_Gen_longitude_forward[h]), float(inf_Gen_latitude_forward[h]),float(u))
     lat_long_result_forward.append(s)
     h=h+1

 #print(lat_long_result_backward)

 #----------------------------from sucessful TRUE extracting the ID Values
 f=0
 note=forward(y)
 imp_ret=[]
 for i in  lat_long_result_forward:
     if i==True:
         imp_ret.append(IDLis[note[f]])
         f=f+1
     else:
         f=f+1
        
 #print('FORWARD RESULT')
 #print(imp_ret)
 FORWARD_RESULT=imp_ret
 result=Union(FORWARD_RESULT,BACKWARD_RESULT)
 print('\n')
 print('                 UNION RESULT of 1st ITERATION Check: ')
 print('\n')
 return(result)

while True:
 result=continous_check('Umer Uni')
 if len(result)>0:
     message = client.messages \
                .create(
                     body="Sir/Maa'm You are not maintaining social distancing-Social distancing is the best way to keep yourself safe from covid19.",
                     from_='+15203326362',
                     to='+923061924723'
                 )
     print(message.sid)
     break
