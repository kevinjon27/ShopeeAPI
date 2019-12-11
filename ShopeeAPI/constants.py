# -*- coding: utf-8 -*-
from blessings import Terminal

class Constants(object):


    term = Terminal()

    # COLORS
    WARNING = "FFEB3B"
    SUCCESS = "8BC34A"
    INFO = "03A9F4"
    DANGER = "FF5722"
    BLACK = "000"

    # THEME INQUIRER
    THEME = {
                'List': {
                    'selection_color': term.bold_green,
                    'selection_cursor': '❯'
                }
            }

    BASE_URL = "https://shopee.co.id/"
    API_BASE_URL = "https://mall.shopee.co.id/api/{version!s}/"