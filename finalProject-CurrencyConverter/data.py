import urllib.request as urllib
import json
import xml.etree.ElementTree as ET

def fetch_data():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    return data
def convert(amount ,src, dst):
    data = fetch_data()
    result = 1/data['rates'][src]*data['rates'][dst]*amount
    return result

def fetch_data_xml():
    file = open("cl-currencies-select-option.txt")
    data = file.read()
    file.close()
    return ET.fromstring(data)

