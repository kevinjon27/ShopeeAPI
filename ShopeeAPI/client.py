# -*- coding: utf-8 -*-
from io import BytesIO
import logging
import gzip
import json

from .constants import Constants
from .utils import Utils
from .compat import (
    compat_urllib_parse, compat_urllib_error,
    compat_urllib_request, compat_urllib_parse_urlparse,
    compat_http_client)

from .endpoints import (
    SearchEndpointsMixin,ItemEndpointsMixin
)

logger = logging.getLogger(__name__)


class Client(SearchEndpointsMixin, ItemEndpointsMixin, Utils, object):
    def __init__(self, **kwargs):
        """
        :param kwargs: See below
        :Keyword Arguments:
            - **timeout**: Timeout interval in seconds. Default: 15
            - **api_url**: Override the default api url base
        :return:
        """

        self.timeout = kwargs.pop('timeout', 15)
        self.logger = logger

        handlers = []
        opener = compat_urllib_request.build_opener(*handlers)
        self.opener = opener
        super(Client, self).__init__()

    @staticmethod
    def _read_response(response):
        """
        Extract the response body from a http response.
        :param response:
        :return:
        """
        if response.info().get('Content-Encoding') == 'gzip':
            buf = BytesIO(response.read())
            res = gzip.GzipFile(fileobj=buf).read().decode('utf8')
        else:
            res = response.read().decode('utf8')
        return res

    @property
    def default_headers(self):
        return {
            'User-Agent': 'iOS app iPhone Shopee appver=24724',
            'Accept': '*/*',
            'Accept-Language': 'en-US',
            'Accept-Encoding': 'gzip, deflate, br',
            'x-api-source': 'rn',
            'referer': 'https://shopee.co.id/',
        }

    def _call_api(self, endpoint, params=None, query=None, return_response=False, version="v1"):
        """
        Calls the private api.
        :param endpoint: endpoint path that should end with '/', example 'discover/explore/'
        :param params: POST parameters
        :param query: GET url query parameters
        :param return_response: return the response instead of the parsed json object
        :param version: for the versioned api base url. Default 'v1'.
        :return:
        """
        url = "{0}{1}".format(Constants.API_BASE_URL.format(version=version), endpoint)

        if query:
            url += ('?' if '?' not in endpoint else '&') + compat_urllib_parse.urlencode(query)
        headers = self.default_headers
        data = None

        req = compat_urllib_request.Request(url, data, headers=headers)

        response = self.opener.open(req, timeout=self.timeout)

        response_content = self._read_response(response)
        self.logger.debug('RESPONSE: {0:d} {1!s}'.format(response.code, response_content))
        json_response = json.loads(response_content)

        print("url: " + url)
        return json_response