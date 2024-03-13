import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

url = "https://candidat.francetravail.fr/offres/emploi/data-analyst/s28m18"
page = requests.get(url)

soup = bs(page.content, 'html.parser')
soup

france_travail = soup.find_all("li" , class_="result")
france_travail

titles_clean = []
adress_clean = []
description_clean = []
type_contrat_clean  = []


for france_travail in france_travail :

    titles_clean.append(france_travail.find("span", class_="media-heading-title").text)

    adress_clean.append(france_travail.find('p', class_="subtext").find("span").text)


    description_clean.append(france_travail.find('p' , class_="description").text)

    type_contrat_clean.append(france_travail.find('p', class_="contrat visible-xs").text)

df = pd.DataFrame({"Poste" : titles_clean , "Lieu" : adress_clean , "Description" : description_clean, "Contrat" : type_contrat_clean})
df
