from messages.message import Message
import messages.ControlMessageProto_pb2 as protoBuf
from messages.controlMessageURN import ControlMessageURN


class AKCommand(Message):
    def __init__(self):
        Message.__init__(self)
        self.urn = ControlMessageURN.AK_COMMAND.value
        self.commands = []
        self.message = None

    def add_command(self, command):
        self.commands.append(command)

    def read(self):
        pass

    def write(self):
        aKCommand = protoBuf.AKCommandProto()
        
        for command in self.commands:
            commandProto = protoBuf.CommandProto()
            commandProto.urn = command.get_urn()

            for f in command.get_fields().keys():
                value = command.get_fields().get(f)
                #print(f, value)
                if isinstance(value, int):
                    commandProto.fields[f].valueInt = int(value)

                elif isinstance(value, bool):
                    commandProto.fields[f].valueBool = bool(value)

                elif isinstance(value, float):
                    commandProto.fields[f].valueDouble = float(value)

                elif isinstance(value, bytes):
                    commandProto.fields[f].listByte = value

                elif isinstance(value, list):
                    intListProto = protoBuf.IntListProto()
                    #intListProto.values.extend(value)
                    
                    # arr = [279, 266]
                    # for v in arr:
                    #     intListProto.addInt(v)
                    #print(intListProto)

                    path = []
                    path.append(279)
                    path.append(266)
                    # path.append(266)

                    # for i in range(len(value)):
                    #     path.append(value[i])

                    #commandProto.fields[f].listInt.extend(path)
                    commandProto.fields[f].listInt.values.extend(path)
                    # commandProto.fields[f].listInt.values.append(int(266))
                    # commandProto.fields[f].listInt.values.append(int(266))

                elif isinstance(value, [[]]):
                    intMatrixProto = protoBuf.IntMatrixProto()
                    for i in range(len(value)):
                        intListProto = protoBuf.IntListProto()
                        for j in range(len(value[i])):
                            intListProto.values.append(value[i][j])
                        intMatrixProto.values.append(intListProto)

                    commandProto.fields[f].matrixInt = intMatrixProto

            aKCommand.commands.append(commandProto)

        print(aKCommand)

        print(aKCommand.SerializeToString())    
        return aKCommand.SerializeToString()