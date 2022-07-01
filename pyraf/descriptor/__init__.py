
class BaseDescriptor:
    def __init__(self) -> None:
        from ..utils.RafUri import RafUri
        ##
        self.__uri = RafUri()
        self.__group = dict()
        pass

    @property
    def uri(self):
        return self.__uri

    def __setattr__(self, __name: str, __value, propagate=True) -> None:
        super().__setattr__(__name, __value)
        ##
        __key = __name.split('_',maxsplit=1)[0]
        if __key not in self.__group:
            return
        ##
        if __name not in self.__group[__key]:
            self.__group[__key][__name] = __value
            if propagate: self.triggerHandle('add', __key, __name, __value)
        elif self.__group[__key][__name]!=__value:
            self.__group[__key][__name] = __value
            if propagate: self.triggerHandle('update', __key, __name, __value)
        else:
            pass
        pass

    def __delattr__(self, __name: str) -> None:
        super().__delattr__(__name)
        ##
        __key = __name.split('_',maxsplit=1)[0]
        if __key not in self.__group:
            return
        ##
        self.__group[__key].pop(__name)
        self.triggerHandle('del', __key, __name)
        pass

    def setGroup(self, group_name, shared_dict=None) -> None:
        __key = f'{group_name}'
        if __key not in self.__group:
            _dict = shared_dict if shared_dict else dict()
            self.__group[ __key ] = _dict
        pass

    def getGroup(self, group_name) -> list:
        __key = f'{group_name}'
        if __key in self.__group:
            return self.__group[ __key ]
        else:
            return None

    def addToGroup(self, group_name, *value) -> None:
        __key = f'{group_name}'
        if __key not in self.__group:
            raise Exception(f'Group Name not Exist: {group_name}.')
        else:
            self.__group[ __key ].extend(value)
        pass

    def listGroup(self):
        return list( self.__group.keys() )

    def triggerHandle(self, *args, **kwargs):
        pass

    def resume(self, stat=None):
        # resume from pickling, and no need to propagate
        self.__group = stat
        pass

    def retain(self):
        # return copy of `self.__group` and wait for destroy
        return self.__group

    pass
