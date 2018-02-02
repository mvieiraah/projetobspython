#coding:utf-8
try:
  from bs4 import BeautifulSoup
  import requests 
except:
  print ("Módulos não carregados")

url = "http://www.rj.gov.br/web/seeduc/exibeconteudo?article-id=375402"
r = requests.get (url)
pega = r.text
soup = BeautifulSoup(pega)  

for links in soup.find_all('a'):
  print (links.get('href'))

  ********************************************************************************************


import requests
from bs4 import BeautifulSoup

url= 'http://www.rj.gov.br/web/seeduc' 

r = requests.get(url)

soup = BeautifulSoup.BeautifulSoup(r.text,'lxml')
 
lista_diretorias = soup.find_all('table': class='Diretorias_regionais'):
#print(lista_diretorias)
       
url= 'http://www.rj.gov.br/web/seeduc/exibeconteudo?article-id=375402'

for lista_td in lista_diretorias:
    lista_td,findall('td')
    for lista_dados in lista:
    #print(lista_dados.next_element)
        if lista_dados.next_element.name == 'a':
           url_it = '{0}{1}'.format(url,lista_diretorias.next_element.get('href'))
        else:
            print(lista_dados.next_element)
