from bs4 import BeautifulSoup
import requests
import pandas as pd


search_term = 'vape'

def get_data(search_term):
    url = f"https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=%27{search_term}%27&_sacat=0&LH_TitleDesc=0&_odkw=canon+m50&_osacat=0"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def parse(soup):
    products_list = []
    results = soup.find_all('div', {'class': 's-item__info clearfix'})
    for item in results:
        products = {
            'Title': item.find('h3', {'class': 's-item__title'}).text,
            'Price': item.find('span', {'class': 's-item__price'}).text.replace('$', '').replace(',', '').strip(),
            'Link': item.find('a', {'class': 's-item__link'})['href']
        }
        products_list.append(products)
    # print(results)
    return products_list

def output(products_list, search_term):
    df1 = pd.DataFrame(products_list)
    df1.to_csv('/home/ariestootl/Documents/Python Practice/0. Python Projects/WebScraping/eBayPrices/'+ search_term  + "_" + 'output.csv', index=False)
    return

soup = get_data(search_term)
products_list = parse(soup)
output(products_list, search_term)
