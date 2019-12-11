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

    args = parser.parse_args()


    print('Client version: {0!s}'.format(client_version))

    api = Client()

    # print(api.imageUrl('ab166bb8de36b075b64921'))

    result = api.search_items(page_type='search',keyword=args.keyword, limit=2)
    # print("\n\n\n\n\n")
    pp.pprint(result)




def clear(self):
    os.system('cls' if os.name == 'nt' else 'clear')