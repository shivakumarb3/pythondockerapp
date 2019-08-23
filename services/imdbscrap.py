import requests
from bs4 import BeautifulSoup

class Scrap:
    def __init__(self, entity,intent):
        self.e = entity
        self.i=intent
        
    def getAnswer(self):
         p={
    
          'q':self.e+" "+self.i
         }

         r1=requests.get("https://www.imdb.com/title/tt7465992/")
         #print(r1)
         #print(self.i)
         print(r1.text)
         soup = BeautifulSoup(r1.text,"html.parser")
         #li = soup.find('span', {'class': 'oqSTJd'})
         #li2=soup.find('div', {'class': 'BNeawe vvjwJb AP7Wnd'})clc
         #li=soup.select('div.BNeawe s3v9rd AP7Wnd')
         s=""
         #print(soup)
         #print(li)
         r=""
         #if li2!=None:
            #for element  in li2:
                #r=r+element+"\n"
         #if li!=None:
            #for element in li:
           #print(element)
                #s=s+element+"\n"
         #return s+"\n"+r
v=Scrap("maharshi","review")
print(v.getAnswer())
#r=Review("rangasthalam")
#print(v.getAnswer())
      

