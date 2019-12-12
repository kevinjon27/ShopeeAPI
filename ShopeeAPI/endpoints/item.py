class ItemEndpointsMixin(object):
    def item_detail(self, item_id, shop_id):
        """
        :param item_id
        :param shop_id
        :return:
        """

        query = {
            'itemid': item_id,
            'shopid': shop_id,
        }

        return self._call_api("item/get", query=query, version="v2")