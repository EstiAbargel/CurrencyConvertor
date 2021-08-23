from data import fetch_data, convert, fetch_data_xml
def converter(amount, src_type, dst_type):
    result = convert(amount, src_type, dst_type)
    print(amount, src_type, "in", dst_type, ":", result, dst_type)
    return result
list_currencies = list(fetch_data()['rates'].keys())
date = fetch_data()['date']
print(list_currencies)
converter(5,'ILS','USD')

def find_currency(currency):
    tree = fetch_data_xml()
    options = tree.findall('option')
    for option in options:
        if option.text == currency:
            return option.get("title")
    return currency