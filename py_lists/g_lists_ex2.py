#!/usr/bin/env python


ip_addr = input("\nPlease enter IP address: ")
octets = ip_addr.split(".")

# One solution
print()
print(f"{octets[0]:<12}{octets[1]:<12}{octets[2]:<12}{octets[3]:<12}")
print()

# Alternate solution using unpacking
print()
print("{:<12}{:<12}{:<12}{:<12}".format(*octets))
print()

#start of lists exercise
octets[-1]=0
binary = []
binary.append(bin(int(octets[0])))
binary.append(bin(int(octets[1])))
binary.append(bin(int(octets[2])))
binary.append(bin(int(octets[3])))

print()
print ("{:<12}{:<12}{:<12}{:<12}".format("Octet1", "Octet2", "Octet3", "Octet4"))
print ("{:<12}{:<12}{:<12}{:<12}".format(*octets))
print ("{:<12}{:<12}{:<12}{:<12}".format(*binary))
print ()


