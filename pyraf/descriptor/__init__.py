
class BaseDescriptor:
    def __init__(self) -> None:
        self.uri = 'raf://{_address}/{_pid}/{_id}'
        pass

    def triggerHandle(self, *args, **kwargs):
        pass

    def resume(self, stat=None):
        pass

    def retain(self):
        pass

    pass
