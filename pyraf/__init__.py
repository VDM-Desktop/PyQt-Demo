__all__ = ['channel', 'descriptor']

from .descriptor import BaseDescriptor
from .channel import (CHANNEL_FORWARD, CHANNEL_SHARED, CHANNEL_BROADCAST)

class Yggdrasil:
    __slots__ = ['things']

    def __init__(self, things=None) -> None:
        self.things = things if things else dict()
        pass

    def prune(self, name):
        pass

    def merge(self, ):
        pass

    pass

class __PyRAF:
    def __init__(self) -> None:
        #TODO: [Channel] init global channel in current process
        #TODO: [Socket] init virtual network interface
        #TODO: [File] init pseudo file system
        #TODO: [Device] init device mapper
        #TODO: [remote] init discovery service
        #NOTE: init Yggdrasil
        self.root = Yggdrasil()
        pass
    
    def Descriptor(self, desc, isolated=False, remote=None):
        origin_init = desc.__init__

        def __init__(_self, *args, **kwargs):
            origin_init(_self, *args, **kwargs)
            self.add(_self, isolated, remote)
            pass

        def __rshift__(_self, _desc):
            self.connect(_self, _desc, type=CHANNEL_FORWARD)
            pass

        desc.__init__ = __init__
        desc.__rshift__ = __rshift__
        return desc
    
    def Daemon(self, func):
        from functools import wraps
        @wraps(func)
        def _wrap_func(*args, **kwargs):
            self.start()
            res = func(*args, **kwargs)
            self.stop()
            return res
        return _wrap_func

    def IsolatedExecutor(self, desc):
        #TODO: prepare control/data link for the desc
        pass

    ##-------------- offline operation -------------##
    def add(self, desc: BaseDescriptor, isolated:bool, remote:bool) -> str:
        assert( isinstance(desc, BaseDescriptor) )
        #add to Yggdrasil
        pass

    def remove(self, desc: BaseDescriptor):
        #remove from Yggdrasil
        pass

    def connect(self, desc_a, desc_b, type):
        assert( desc_a in self.root.things )
        assert( desc_b in self.root.things )
        #
        pass

    ##-------------- online operation --------------##
    def start(self):
        pass

    def stop(self):
        #stop 1) the remote 2) the isolated ones 3) the channels
        pass

    def retain(self, desc):
        pass

    def resume(self, desc):
        pass

    def get_channel_status(self, desc=None):
        #return channel status bound to `desc`
        pass

    ##-------------- offload operation -------------##
    def get_remote_list(self):
        pass

    def offload_to(self, desc: BaseDescriptor):
        pass

    pass

PyRAF = __PyRAF()



if __name__=='__main__':
    pass
