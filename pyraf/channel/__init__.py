import re
from collections.abc import MutableMapping
from multiprocessing import Queue

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

class ChannelDescriptor:
    __type__ = ['shared', 'forward', 'broadcast']

    def __init__(self, tx, rx, type='forward', _filter=None):
        self._filter = _filter
        (tx.uri, rx.uri)
        pass

    @property
    def receivers(self):
        return self._receivers

    @property
    def filter(self):
        try:
            _regex = re.compile(self._filter)
            _filter = lambda x: {k:v for k,v in x.items() if _regex.fullmatch(k) is not None}
            return _filter
        except:
            return (lambda x: x)

    def send(self):
        pass

    def recv(self):
        pass

    pass