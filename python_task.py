import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import json

url = 'https://shop.mango.com/gb/women/skirts-midi/midi-satin-skirt_17042020.html?c=99'
page = urllib.request.urlopen(url)
data_parsed = BeautifulSoup(page, 'html.parser')
page.close()

data = str(data_parsed.findAll('script')[2])
data_split = data.split('var dataLayerV2Json = ')[1].split('var dataLayer = ')
product_data = data_split[0].rsplit(';', 1)[0].encode().decode('utf-8')

product_data_as_json = json.loads(product_data)
product_info = {}

for el in product_data_as_json['ecommerce']['detail']['products']:
    for key, value in el.items():
        if key == 'name':
            product_info['name'] = value
        elif key == 'salePrice':
            product_info['price'] = value
        elif key == 'sizeAvailability':
            product_info['size'] = value.split(',')
        elif key == 'colorId':
            if value == '99':
                product_info['color'] = "black"
            else:
                product_info['color'] = "beige"


with open('python_task/output.json', 'w+') as f:
    json.dump(product_info, f)


