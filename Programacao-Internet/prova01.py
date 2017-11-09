import re
from bs4 import BeautifulSoup
import requests

def search():
    #keyword = input("Digite a plavra chave: ")
    url = requests.get("http://example.webscraping.com/")

    url_test = url

    html_sem_tags = BeautifulSoup(url_test.text, "html.parser")
    #tentativa com regex
    #ahref = re.findall(r'< a href="">(.*Albania)</a>',url_test)
    #print(ahref)

    links =  html_sem_tags.find_all("a")

    for i in links:
        #chave = "Log In"

        #if(i  == "Albania"):
        print(i)
    print(links)

search()


