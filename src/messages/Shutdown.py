from messages.message import Message
from messages.controlMessageURN import ControlMessageURN


class Shutdown(Message):
    def __init__(self, data) -> None:
        super().__init__()
        self.urn = ControlMessageURN.SHUTDOWN.value

    def read(self):
        pass

    def write(self):
        pass
