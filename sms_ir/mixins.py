import logging
import sys
import requests
from requests import (
    ReadTimeout,
    ConnectTimeout,
    HTTPError,
    Timeout,
    ConnectionError,
)


class LoggerMixin:
    def config_logger(self):                                                                                                     
        self.log_level=logging.INFO                                         

        log_format = logging.Formatter('[%(asctime)s] [%(levelname)s] - %(message)s')
        self.logger = logging.getLogger(__name__)                                  
        self.logger.setLevel(self.log_level)                                       

        # writing to stdout                                                     
        handler = logging.StreamHandler(sys.stdout)                             
        handler.setLevel(self.log_level)                                        
        handler.setFormatter(log_format)                                        
        self.logger.addHandler(handler)                                            


class RequestsMixin :
    def post(self, url, data):
        try :
            self.logger.info("send request to %s", url)
            return requests.post(
                url,
                headers=self._headers,
                json=data,
            )
        except (ConnectTimeout, HTTPError, ReadTimeout, Timeout, ConnectionError) as e:
            self.logger.error(str(e))
            return self.fake_response(e.request)

    def delete(self, url):        
        try :
            self.logger.info("send request to %s", url)
            return requests.delete(
                url,
                headers=self._headers,
            )
        except (ConnectTimeout, HTTPError, ReadTimeout, Timeout, ConnectionError) as e:
            self.logger.error(str(e))
            return self.fake_response(e.request)
    
    def get(self, url, params=None):
        try :
            self.logger.info("send request to %s", url)
            return requests.get(
                url,
                headers=self._headers,
                params=params,
            )
        except (ConnectTimeout, HTTPError, ReadTimeout, Timeout, ConnectionError) as e:
            self.logger.error(str(e))
            return self.fake_response(e.request)        
    
    def fake_response(self, request):
        response = requests.models.Response()

        response.status_code = 503
        response.request = request
        response.url = request.url

        return response