# -*- coding: utf-8 -*-

from os import replace
import requests
from bs4 import BeautifulSoup
import lxml
from itertools import zip_longest

from Movie.models import *


links=[]

titles=[]
iframes=[]
images=[]
description=[]
rates=[]
actors=[]
Directors=[]
geners=[]
categorys=[]
quality=[]
time=[]
Releases=[]
contry=[]
crew=[]
slug=[]
id=[]


url="https://ww1.solarmovie.cr/featured/"

for page in range(1):
    print("------page------")
    req=requests.get(url+str(page))
    print(url+str(page))
    soup=BeautifulSoup(req.content , "lxml")

    box=soup.findAll('div',class_="ml-item")


    for x in box:
        link=x.find('a').get('href')
        link='https://ww1.solarmovie.cr'+link+'watching'



        req1=requests.get(link)
        soup1=BeautifulSoup(req1.content,'lxml')
        id=None
        file_list=[ id ,titles ,quality,categorys,geners,contry,rates ,time ,Releases,Directors,actors,description,images,iframes ,slug]
        exported=zip_longest(*file_list)
        exported1=list(zip(*file_list))

        try:
            title=x.find('span' ,{ 'class':'mli-info'}).get_text().replace(' ','').replace('\n','')
            titles.append(title)
            
            iframe=soup1.find('iframe' , { 'id':'iframe-embed'} )
            iframes.append(iframe.get('src'))


            img=soup1.find('img' , class_='thumb mli-thumb lazy').get('src')
            images.append('https://ww1.solarmovie.cr'+img)
            

            desc=soup1.find('div' ,{ 'class':'desc'}).get_text()
            description.append(desc)

            
            cate=soup1.find('div' ,{ 'class':'mvici-left'}).get_text().replace(' ','').split('\n')
            cate=cate[2].replace('，',',').split(',')
            cate=cate[0]
            categorys.append(cate)
            
            genre=soup1.find('div' ,{ 'class':'mvici-left'}).get_text().replace(' ','').split('\n')
            genre=genre[2].replace('，',' , ')
            geners.append(genre)              
            
            actorss=soup1.find('div' ,{ 'class':'mvici-left'}).get_text().replace(' ','').split('\n')
            actorss=actorss[4].replace('，',' , ')
            actors.append(actorss)
            
            con=soup1.find('div' ,{ 'class':'mvici-left'}).get_text().replace(' ','').split('\n')
            con=con[8]
            con=con.replace('，',',')
            contry.append(con)
            
            dir=soup1.find('div' ,{ 'class':'mvici-left'}).get_text().replace(' ','').split('\n')
            dir=dir[6]
            dir=dir.replace('，',',')
            Directors.append(dir)
            

            tim=soup1.find('div' ,{ 'class':'mvici-right'}).get_text().replace(' ','').split('\n')
            tim=tim[1].split('Duration:')
            tim=tim[1]
            time.append(tim)
            
            rat=soup1.find('div' ,{ 'class':'mvici-right'}).get_text().replace(' ','').split('\n')
            rat=rat[4].replace('IMDb:','')
            rates.append(rat)
            
            qua=soup1.find('div' ,{ 'class':'mvici-right'}).get_text().replace(' ','').split('\n')
            qua=qua[2].replace('Quality:','')
            quality.append(qua)
            
            year=soup1.find('div' ,{ 'class':'mvici-right'}).get_text().replace(' ','').split('\n')
            year=year[3] .replace('Release:' ,'')               
            Releases.append(year)
            

           
        except AttributeError:
            print(AttributeError)
        except requests.exceptions.ConnectionError:
            print(ConnectionError)
        except ValueError :
            print(ValueError)
        except PermissionError:
            print(PermissionError)
      
        for x in exported :
            movie_db=Movie(id=x[0],title=x[1],gener=x[2],quality=x[3],category=x[4],contry=x[5],rate=x[6],time=x[7],year=x[8],Directors=x[9],actors=x[10],overview=x[11],image=x[12],Iframemovie=x[13],slug=x[14])
            if Movie.objects.first() != x :
                movie_db.save()
            else:
                pass
print("Done")
# ['id','title' ,'gener', 'quality', 'category','contry','rate', 'time', 'year',  'Directors','Actors','overview','image', 'Iframemovie','slug']
