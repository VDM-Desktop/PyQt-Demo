__all__ = ['channel', 'descriptor']

from .descriptor import BaseDescriptor

class Yggdrasil:
    pass

class __PyRAF:
    def __init__(self) -> None:
        #TODO: [Channel] init global channel in current process
        #TODO: [Socket] init virtual network interface
        #TODO: [File] init pseudo file system
        #TODO: [Device] init device mapper
        #TODO: [remote] init discovery service
        #TODO: init Yggdrasil
        pass

    def descriptor(self, desc: BaseDescriptor,
                name=None,
                ) -> BaseDescriptor:
        _name = name if name else desc.__name__
        #TODO: wrap the __init__ function
        return desc
    
    ##------------- offline operation -------------##
    def add(self, desc: BaseDescriptor) -> str:
        #add to Yggdrasil
        pass

    def remove(self, desc: BaseDescriptor):
        #remove from Yggdrasil
        pass

    ##-------------- online operation --------------##
    def start(self):
        pass

    def stop(self):
        pass

    def retain(self, desc=None):
        pass

    def resume(self, desc=None):
        pass

    def get_connection_status(self, desc=None):
        #return all channel status
        pass

    def get_remote_list(self):
        pass

    def offload_to(self, desc: BaseDescriptor):
        pass

    pass

PYRAF = __PyRAF()
