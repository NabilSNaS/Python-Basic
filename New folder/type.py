'''from typing import Dict, Tuple
numbers: tuple[int]
planets=['Earth','Mars','Jupiter'] # type:list[str]'''

'''from typing import ClassVar
class Human:
    name:str
    age:int
    gender:str
    address:ClassVar[str]='Dhaka'

    def __int__(self, name:str='nabu') ->None:
        self.name=name'''

'''from typing import Dict, List
HostName=str
Address=str
Server=Dict[HostName,Address]
Network=List[Server]
'''

'''from typing import Dict,List,NewType
HostName=NewType('HostName', str)
Address=NewType('Address', str)
Server=NewType('Server', Dict[HostName,Address])
Network=NewType('Network', List[Server])'''

'''hostname=HostName('local')
address =Address('127.0.0.1')
server=Server({hostname:address})
network =Network([server])
'''

from typing import TypeVar
A= TypeVar('A')
B= TypeVar('B', str,int)
C= TypeVar('C', str,int)

def add(x:A, y:C)-> A:
    pass











