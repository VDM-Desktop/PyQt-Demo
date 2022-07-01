import os, netifaces
import itertools

__INDEX = itertools.count()

class RafUri:
    def __init__(self):
        self.address = netifaces.gateways()['default'][netifaces.AF_INET][0]
        self.pid = os.getpid()
        self.id = next(__INDEX)
        ##
        self.__uri = f'raf://{self.address}/{self.pid}/{self.id}'
        pass
    
    def __str__(self) -> str:
        return self.__uri

    def __mod__(self, another):
        if self.address!=another.address:
            return (True,False)
        elif self.pid!=another.pid:
            return (False,True)
        else:
            return (False,False)
        pass

    pass