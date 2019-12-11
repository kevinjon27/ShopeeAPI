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
    parser.add_argument('-k', '--keyword', dest='keyword', type=str, required=True)
    parser.add_argument('-s', '--search', dest='search', type=str, required=True)

    args = parser.parse_args()


    print('Client version: {0!s}'.format(client_version))

    api = Client()

    if args.search == 'shop':
        result = api.search_users(keyword=args.keyword)
    elif args.search == 'items':
        result = api.search_items(page_type='search',keyword=args.keyword, limit=5)
        items = result.get('items', [])
        
        pp.pprint([api.imageUrl(i['image']) for i in items])

    print('All ok')


