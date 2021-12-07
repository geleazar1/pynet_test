#!/usr/bin/env python 
ip1 = input(" Enter IP address: ")
ip_split = ip1.split(".")
print (f"{ip_split[0]:<12}{ip_split[1]:<12}{ip_split[2]:<12}{ip_split[3]:<12}")
