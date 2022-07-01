import socket
from collections.abc import MutableMapping
from multiprocessing import Queue

from ..descriptor import BaseDescriptor
from ..remote import DAEMON_PORT

CHANNEL_FORWARD   = 0x01
CHANNEL_SHARED    = 0x02
CHANNEL_BROADCAST = 0x03

class ChannelContext(MutableMapping):
    def __init__(self, parent, channels:list, _input=None, _output=None) -> None:
        self.parent, self.channels = parent, channels
        self._input  = _input if _input else dict()
        self._output = _output if _output else dict()
        pass

    def __getitem__(self, key):
        return self._input[key]
    
    def __iter__(self):
        return iter(self._input)
    
    def __len__(self):
        return len(self._input)

    def __setitem__(self, key, value) -> None:
        self._output[key] = value
        self.__send__({key:value})
        pass
    
    def __delitem__(self, key):
        try:
            del self._output[key]
        except Exception as e:
            if key not in self._input:
                raise e
        pass

    def update(self, kwargs:dict) -> None:
        self._output.update(kwargs)
        self.__send__(kwargs)
        pass

    def __send__(self, kwargs:dict) -> None:
        for chan in self.channels:
            chan.send( chan.filter(kwargs) )
        pass

    pass

class ChannelFactory:
    def __init__(self) -> None:
        pass
    pass

class ChannelDescriptor:
    def __init__(self, tx, *rx, groups:tuple, type=CHANNEL_FORWARD):
        self.groups = groups
        if type!=CHANNEL_BROADCAST:
            assert( len(rx)==1 )
        ##
        rx_one = rx[0]
        _remote, _isolated = tx % rx_one
        if _remote:
            tx_chan, rx_chan = self.__remote(tx, rx_one)
        elif _isolated:
            tx_chan, rx_chan = self.__isolated(tx, rx_one)
        else:
            tx_chan, rx_chan = self.__local(tx, rx_one)
        ##
        {
            CHANNEL_FORWARD: self.__forward,
            CHANNEL_SHARED:  self.__shared,
            CHANNEL_BROADCAST: self.__broadcast
        }[type](tx, rx, tx_chan, rx_chan)
        pass

    def __local(self, tx, rx):
        _dict = dict()
        return (_dict, _dict)

    def __isolated(self, tx, rx):
        _q = Queue()
        return (_q, _q)

    def __remote(self, tx, rx):
        return (rx.address, tx.address)

    def send(self):
        pass

    def recv(self):
        pass

    pass
