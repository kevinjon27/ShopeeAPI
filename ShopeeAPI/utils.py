import json
import os

class Utils(object):
    
    script_dir = os.path.dirname(__file__)
    
    def image_url(self, image_id):
        """
        :param image_id: Image id
        :return:
        """
        return "https://cf.shopee.co.id/file/{image_id!s}".format(image_id=image_id)
    
    def get_category(self, category_id):
        """
        :param category_id: Category id
        :return:
        """
        RESULT = {}
        
        rel_path = "json/categories.json"
        FILE_NAME = os.path.join(self.script_dir, rel_path)

        with open(FILE_NAME, 'r') as file_data:
            result = json.load(file_data)
            for item in result:
                if item['id'] == category_id:
                    return item
            else:
                return 'category not found'
            
    def get_price(self, price, ending='00000'):
        """
        :param price: variable price from Shopee
        :return:
        """
        price = str(price)
        if price.endswith(ending):
            return price[:-len(ending)]
        return price