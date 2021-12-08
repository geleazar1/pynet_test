#1/usr/bin/env python

# Create dictionary
netdev1 = {
    "ip_address" : "192.168.1.100",
    "username" : "pyclass",
    "password" : "88newclass",
    "device_type" : "arista_eos",
    }

for k,v in netdev1.items():
    print(k, v)
netdev1["password"] = "new_value"
netdev1["secret"] = "new_secret"
device_type = netdev1.get("device_type", "cisco_ios")
print(f"\nDefault decive type: {device_type}\n")
# print(netdev1.get("Cisco_IOS"))

