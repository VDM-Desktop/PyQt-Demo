import os, netifaces
import itertools

__INDEX = itertools.count()

class RafUri:
    def __init__(self):
        _address = netifaces.gateways()['default'][netifaces.AF_INET][0]
        _pid = os.getpid()
        _id = next(__INDEX)
        ##
        self.__uri = f'raf://{_address}/{_pid}/{_id}'
        pass

    @property
    def uri(self):
        return self.__uri
    pass