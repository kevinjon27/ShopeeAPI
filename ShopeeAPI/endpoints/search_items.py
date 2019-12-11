class SearchItemsEndpointsMixin(object):
    def search_items(self, page_type, by='relevancy', order_by='desc', newest=0, limit=20, **kwargs):
        """
        :param page_type: Example: 'shop', 'search'
        :param by: 
            :meth:'pop' = populer
            :meth:'ctime' = terbaru
            :meth:'sales' = terlaris
            :meth:'price' = harga
            :meth:'relevancy' = terkait (need keyword params)
        :param order_by: Example: 'desc', 'asc'
        :param newest: Example: 0
        :param kwargs: See below
        :Keyword Arguments:
            - **shop_categoryids**: For shop category
            - **match_id**: For shop id
            - **keyword**: Search by keyword
        :return:
        """

        query = {
            'page_type': page_type,
            'order': order_by,
            'version': '2',
            'limit': limit,
            'is_buyer_perspective': '1'
        }

        query.update(kwargs)
        
        return self._call_api("search_items/", query=query, version="v2")