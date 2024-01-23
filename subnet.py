import math
import ipaddress

def ip_to_binary(address):
    octets = address.split('.')
    binary_ip = ''
    for octet in octets:
        binary_ip = binary_ip + format(int(octet), '08b')+ '.'
    binary_ip = binary_ip[:-1]
    return(binary_ip)
    
def binary_to_ip(address):
    octets = address.split('.')
    decimal_ip = ''
    for octet in octets:
        decimal_ip = decimal_ip + str(int(octet, 2)) + '.'
    decimal_ip = decimal_ip[:-1]
    return(decimal_ip)

def needed_hosts(hosts):
    zeroes_from_end = 1
    allowed_hosts = 2
    while (allowed_hosts-2 < hosts):
        allowed_hosts *= 2
        zeroes_from_end += 1
    return allowed_hosts

def subnet_mask(hosts):
    allowed_hosts = needed_hosts(hosts)
    mask = 32 - int(math.log(allowed_hosts, 2))
    return mask

def addresses(address, hosts):
    octets = address.split('.')
    mask = subnet_mask(hosts)
    allowed_hosts = needed_hosts(hosts)
    addresses = {}
    address = ipaddress.IPv4Address(address)
    addresses["network"] = str(address) + '/' + str(mask)
    addresses["first"] = str(address + 1) + '/' + str(mask)
    addresses["last"] = str(address + allowed_hosts-2) + '/' + str(mask)
    addresses["broadcast"] = str(address + allowed_hosts-1) + '/' + str(mask)
    addresses["next"] = str(address + allowed_hosts)
    return addresses

def print_addresses(addresses):
    print("Network: " + addresses["network"])
    print("First Usable: " + addresses["first"])
    print("Last Usable: " + addresses["last"])
    print("Broadcast: " + addresses["broadcast"])
    
def network_addresses(address, hosts_list):
    sorted(hosts_list, reverse=True)
    address_book = {}
    for key in hosts_list:
        book = addresses(address, hosts_list[key])
        address_book[key] = book
        address = book["next"]
    return address_book

def summary(address_book):
    for key in address_book:
        print("\nVLAN " + str(key))
        print("Network: " + address_book[key]["network"])
        print("First Usable: " + address_book[key]["first"])
        print("Last Usable: " + address_book[key]["last"])
        print("Broadcast: " + address_book[key]["broadcast"] + '\n')