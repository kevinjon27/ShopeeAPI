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

    if args.search == 'users':
        #  python examples/search.py -k "zahrasydl" -s users
        #  python examples/search.py -k "kevin" -s users
        result = api.search_users(keyword=args.keyword)
        
        users = result.get('data').get('users')
        if users:
            # pp.pprint(users[0])
            if len(users) == 1:
                user = users[0]
                print('Shop ID: {}'.format(user.get('shopid')))
                print('Username: {}'.format(user.get('username')))
                
                print('Fetching shop items..\n\n')
                result = api.search_items(page_type='shop', match_id=user.get('shopid'),)
                items = result.get('items', [])
                
                pp.pprint(["Name: {}".format(i['name']) for i in items])
            else:
                pp.pprint(["Shop name: {}".format(user.get('shopname')) for user in users])
                
        else:
            print('User not found')
            
        
    elif args.search == 'items':
        #  python examples/search.py -k "iphone x" -s items
        result = api.search_items(page_type='search',keyword=args.keyword, limit=5)
        items = result.get('items', [])
        
        pp.pprint(["Name: {}".format(i['name']) for i in items])

    print('All ok')


