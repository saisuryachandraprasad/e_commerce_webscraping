import httpx
from bs4 import BeautifulSoup
import pandas


url = "https://www.houseoffraser.co.uk/men/hoodies-and-sweatshirts"
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}


def extract_product_data(product):
    try:
        
        brand = product.find('span',class_="productdescriptionbrand").text
        name = product.find('span', class_="productdescriptionname").text
        price = product.find('span',class_="CurrencySizeLarge curprice").text
        print(f'{brand}, {name}, {price}')

    
    except Exception as e:
        print(e)

def main():
    response = httpx.get(url, headers = headers)
    response_html = response.text
    
    soup = BeautifulSoup(response_html, "html.parser")
    products = soup.find_all('div', class_='s-productthumbbox')

    for product in products:
        extract_product_data(product)



    
if __name__ == "__main__":
    main()