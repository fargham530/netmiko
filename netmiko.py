#!/usr/bin/env python
from netmiko import ConnectHandler
iosv_l2_s1= {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.72',
    'username': 'ahsan',
    'password': 'cisco',
}
iosv_l2_s2= {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.75',
    'username': 'ahsan',
    'password': 'cisco',
}
net_connect= ConnectHandler(**iosv_l2_s1)
output=net_connect.send_command('sh ip int brief')
print(output)
net_connect= ConnectHandler(**iosv_l2_s2)
output=net_connect.send_command('sh ip int brief')
print(output)
