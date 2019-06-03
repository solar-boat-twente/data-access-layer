import logging
import time

from urllib.parse import urlencode
from urllib.request import Request, urlopen
from threading import Thread
import config
from data_to_web_app import data_queue

logger = logging.getLogger()


class SendData(Thread):
    def __init__(self):
        super().__init__()
        self.url = 'http://'+config.web_app_ip+':'+config.web_app_port+'/data'

    @staticmethod
    def __get_data_from_queue():
        post_fields = data_queue.data_queue.get()
        print("From queue: {}".format(post_fields))
        #data_queue.data_ready = False
        return post_fields

    def __send_request(self, post_fields):
        input = {'data': post_fields}
        request = Request(self.url, urlencode(input).encode())
        output = urlopen(request).read().decode()
        print(output)

    def run(self):
        while True:
            print("Running")
            post_fields = self.__get_data_from_queue()
            self.__send_request(post_fields)
            time.sleep(1)