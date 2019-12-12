import json
import os
import pprint as pp
import argparse

try:
    from ShopeeAPI import(Client, __version__ as client_version)
except ImportError:
    import sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    from ShopeeAPI import(
        Client, __version__ as client_version)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Shopee demo')
    parser.add_argument('-i', '--item_id', dest='item_id', type=str, required=True)
    parser.add_argument('-s', '--shop_id', dest='shop_id', type=str, required=True)

    args = parser.parse_args()


    print('Client version: {0!s}'.format(client_version))

    api = Client()

    #  Example command:
    #  python examples/item.py -i 5010256607 -s 67693195
    item = api.item_detail(args.item_id, args.shop_id)
    
    if item.get('error') == None:
        item = item.get('item')
        print("\nName: {} \nPrice: {}".format(item['name'], api.get_price(item['price'])))
        

    print('All ok')


