
class BaseDescriptor:
    def __init__(self) -> None:
        self.uri = 'vdm://{_address}/{_pid}/{_id}'
        pass

    def start(self, stat=None):
        pass

    def stop(self):
        pass

    pass
