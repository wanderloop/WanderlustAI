import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import pyautogui
import time
import datetime
from insertToDatabase import insert_table
from insertToDatabase import count_rows


#-------------------------------------------------------------------------
#function for time stamp

def time_stamp_update():
    x = datetime.datetime.now()
    return(str(x.strftime("%M")),str(x.strftime("%H")),str(x.strftime("%x")))


#------------------------------------------------------------------------------
#This code return a list of contacts from pane

def Union(lst1, lst2): 
    final_list = list(set(lst1) | set(lst2)) 
    return final_list 

def loop_watch(delay_time,times):
 
 def loop_check_n_update():
  images= driver.find_elements_by_class_name('_1wjpf')

  k=0
  aList =['start']

  for image in images:
      aList.insert( k, image.get_attribute('title'))
      k+1
 

  k=0
  for i in aList:
      if i=='' or i=='start':
          aList.remove(aList[k])
          k=k+1
      else:
          k=k+1
        

  return(aList)

 i=0
 oldList=[]
 while True:
     try:
         x=loop_check_n_update()
         y=list(set().union(oldList,x))
         i=i+1
         oldList=x
         if i==times:
             break
     except:
         continue
         
 return(y)
    
def cmp(a, b): 
    return len(list(set(a) & set(b)))


def contacts_extract():
 i=0
 lencount=0
 k=[]
 olddata=[]
 save_data=[]
    
 while True:
     j=loop_watch(5,1)
     time.sleep(0.5)
     olddata=Union(j, olddata)
     pyautogui.click(x=520, y=767)
     k.append(len(olddata))
     #print('value of i== '+str(i))
     #print(len(olddata))
     if len(k)>=6:
         e=k[i-5]-k[i-4]+k[i-3]-k[i-2]+k[i-1]-k[i]
         if e==0 :
             #print(olddata)
                      
             return(olddata)
        
         else:
             i=i+1
             continue
     else:
         i=i+1
         continue

def lis_of_contacts():           
 v=contacts_extract()
 newdata=[]
 for  k in v:
  try:
      print(k)
     #do not remove the print statement
      newdata.append(k)
     
  except UnicodeEncodeError:
      print('UPPP')
      #do not remove the print statement
      newdata.append('UPPP')

 return(newdata)
#----------------------------------------------------------------------------

#This program searches for name ,extract coordinates and return back to normal serach pane

def string_ParseTo_Float(mystring):
 alist=[]
 x=mystring.split("?ll=")
 j=x[1]
 x=j.split("&z=")
 j=x[0]
 datum=j
 c=re.sub('[^a-zA-Z0-9\n\.]', ' ', datum)
 f=c.replace('2C','')
 
 for i in f:
     if i==' ':
         break
     else:
         alist.append(i)
 new=''
 for a in alist:
     new += a
     
 y=f.replace(new,'')
 y=float(y)
 x=float(new)

 return(x,y)

def find_co_ordinates(name):
 user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
 user.click()
 time.sleep(5) #this sleep time is important
 try:
  images = driver.find_element_by_class_name('_2-3jQ')
  images.click()
  time.sleep(5)#time sleep is important
  imag = driver.find_elements_by_xpath('/html/body/div[1]/div/div/div[2]/div[3]/span/div/div/div/div/div[2]/div[1]/div/div/div[2]/a')
  k=0
  aList =['start']
  for elem in driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/span/div/div/div/div/div[3]/div[1]/div/div/div/div/div[2]/div[2]/div[1]/span'):
      print(elem.text)
  print(elem.text)
  if elem.text=='Updated just now':
   for im in imag:
       aList.insert( k, im.get_attribute('href'))
   a,b=string_ParseTo_Float(aList[0])
   return(a,b)
  else:
      return(0,0)
 except:
     return(0,0)
    
def search_pane(msg):
    user = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]')
    user.click()
    msg_box = driver.find_element_by_class_name('_2S1VP')
    msg_box.send_keys(msg)
    
def send_message(name,msg):
    count=1
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()
    msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    for i in range(count):
        msg_box.send_keys(msg)
        button = driver.find_element_by_class_name('_35EW6')
        button.click()
        
def search_send_messg_by_name(msg,name):
    search_pane(msg)
    time.sleep(3)
    send_message(name,msg)



def back():
    user = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[1]/div/button/div[2]/span')
    user.click()

def name_based_loc_extract(name): 
 try:
     
     search_pane(name)
     time.sleep(3)#this time delay is also important
     a,b=find_co_ordinates(name)
     #print("X:  "+str(a)+" Y:  "+str(b))
     back()
     return(float(a),float(b))
 except:
     return(0,0)
    
#-------------------------------------------------------------------------------

# this section deletes chat head your in
def delete_chat_head():
 user = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[3]/div/span')
 user.click()
 time.sleep(0.5)
 user = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[3]/span/div/ul/li[5]/div')
 user.click()
 user = driver.find_element_by_xpath('/html/body/div[1]/div/span[2]/div/div/div/div/div/div/div[2]/div[2]')
 user.click()
 time.sleep(2)

#-------------------------------------------------------------------------
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome('/home/ahmed/Desktop/WanderLust_AI/chromedriver',chrome_options=options)
driver.get('https://web.whatsapp.com/')
input('Enter anything after scanning QR code')
#y,x=name_based_loc_extract('Fahad Ali')
#print(y,x)
#g=lis_of_contacts()
#print(g)
file1 = open("text_database","a+")
t=count_rows()
while True:
    g=lis_of_contacts()
    for i in g:
        y,x=name_based_loc_extract(i)
        a,b,c=time_stamp_update()
        if x==0 and y==0:
            #delete_chat_head()
            print('deleted')
        else:
            file1.write(' \n'+'ID: '+str(i)+' X:'+str(y)+' Y:'+str(x)+' '+'TIME:'+b+':'+a+' '+'DATE: '+c)
            insert_table(int(t+2),str(i),float(y),float(x),str(b)+':'+str(a),str(c))
            t=t+1

    search_send_messg_by_name('UPPP','UPPP')
    file1.close()
    break
#-----------------------------------------------------------------------------------------


