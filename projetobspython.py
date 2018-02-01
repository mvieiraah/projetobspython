import requests
from bs4 import BeautifulSoup

url= 'http://www.rj.gov.br/web/seeduc' 

r = requests.get(url)

soup = BeautifulSoup.BeautifulSoup(r.text,'html.parser')
 
lista_diretorias = soup.find_all('table': class='Diretorias_regionais'):
#print(lista_diretorias)
       
url= 'http://www.rj.gov.br/web/seeduc/exibeconteudo?article-id=375402'

for lista_td in lista_diretorias:
    lista_td.findall('td')
    for lista_dados in lista:
    #print(lista_dados.next_element)
        if lista_dados.next_element.name == 'a':
           url_it = '{0}{1}'.format(url,lista_diretorias.next_element.get('href'))
        else:
            print(lista_dados.next_element)
