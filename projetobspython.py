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
