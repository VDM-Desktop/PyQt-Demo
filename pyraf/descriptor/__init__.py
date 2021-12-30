
class BaseDescriptor:
    def __init__(self) -> None:
        self.uri = 'vdm://{_address}/{_pid}/{_id}'
        pass

    def resume(self, stat=None):
        pass

    def retain(self):
        pass

    pass
