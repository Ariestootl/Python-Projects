import requests
import pandas as pd
from bs4 import BeautifulSoup

baseurl = "https://www.thewhiskyexchange.com/"

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'
}

product_links = []
for i in range(1, 2):
    url = f'https://www.thewhiskyexchange.com/search?q=Japanese+Whiskey&pg={i}'
    x = requests.get(url, headers=headers)

    soup = BeautifulSoup(x.content, 'lxml')

    productlist = soup.find_all('li', class_='product-grid__item')



    for item in productlist:
        for link in item.find_all('a', href=True):
            product_links.append(baseurl + link['href'])
len(product_links)

# testurl = 'https://www.thewhiskyexchange.com//p/55475/bourbon-whiskey-ratafia-finish-dumangin-batch-005'


liquorlist = []

for link in product_links:
    x = requests.get(link, headers=headers)

    soup = BeautifulSoup(x.content, 'lxml')

    try:
        Name = soup.find('h1', class_='product-main__name').text.strip()
    except:
        Name = "None"
    try:
        Price = soup.find('p', class_='product-action__price').text.strip()
    except:
        Price = "None"
    try:
        AlcoholContent = soup.find('p', class_='product-main__data').text.strip()
    except:
        AlcoholContent = "None"
    try:
        Description = soup.find('div', class_='product-main__description').p.text.strip()
    except:
        Description = "None"
    try:
        Rating = soup.find('p', class_='review-overview__content').span.text.replace('\n', '')
    except:
        Rating = "None"

    liquor = {
        'Name': Name,
        'Price': Price,
        'Alcohol Content': AlcoholContent,
        'Description': Description,
        'Rating': Rating
    }

    liquorlist.append(liquor)

df1 = pd.DataFrame(liquorlist)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

xlwriter = pd.ExcelWriter('/home/ariestootl/Documents/Python Practice/0. Python Projects/WebScraping/WhiskeyExchange/Output.xlsx')
df1.to_excel(xlwriter, sheet_name="Japanese Whiskey", index=False)
xlwriter.close()
    # facts1 = soup.find_all('h4', class_='product-facts__type')
    # facts2 = soup.find_all('p', class_='product-facts__data')
    # facttitle = []
    # factdesc = []
    # for i in range(len(facts2)):
    #     factdesc.append(facts2[i].text.strip())
    # for i in range(len(facts1)):
    #     facttitle.append(facts1[i].text.strip())
    #
    # df2 = pd.DataFrame(factdesc)
    # df1 = pd.DataFrame(facttitle)
    #
    # df3 = df1.T.copy()
    # df4 = df2.T.copy()
    # df4.columns = df3.iloc[0]
    #
    # df4
    #
    # frames = [liquorlist, df4]
    #
    # alcohollist = pd.concat(frames, axis=1, join="outer")
    #
    # alcohollist
