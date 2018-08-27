#encoding=utf-8
from pyhpecw7.features import mac
from pyhpecw7.comware import HPCOM7  

username = 'test'  
password = 'test'  
port = 830  
hostname = '16.1.151.251' 

device_args = dict(host=hostname, username=username,password=password, port=port)
device = HPCOM7(**device_args)
device.open()

macTable = mac.MacUnicastTable(device)
macTableList = macTable.getMacList()

for mac in macTableList:
    print(mac)
