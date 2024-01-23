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

def calculate_needed_hosts(hosts):
    zeroes_from_end = 1
    allowed_hosts = 2
    while (allowed_hosts-2 < hosts):
        allowed_hosts *= 2
        zeroes_from_end += 1
    return allowed_hosts

def calculate_subnet_mask(hosts):
    allowed_hosts = calculate_needed_hosts(hosts)
    mask = 32 - int(math.log(allowed_hosts, 2))
    return mask

def find_addresses(address, hosts):
    octets = address.split('.')
    mask = calculate_subnet_mask(hosts)
    allowed_hosts = calculate_needed_hosts(hosts)
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
    
def find_addresses_for_network(address, hosts_list):
    sorted(hosts_list, reverse=True)
    address_book = {}
    for key in hosts_list:
        book = find_addresses(address, hosts_list[key])
        address_book[key] = book
        address = book["next"]
    return address_book

def print_address_book(address_book):
    for key in address_book:
        print("\nVLAN " + str(key))
        print("Network: " + address_book[key]["network"])
        print("First Usable: " + address_book[key]["first"])
        print("Last Usable: " + address_book[key]["last"])
        print("Broadcast: " + address_book[key]["broadcast"] + '\n')
        
print('\n')
print("#####     SUBNETTING HELPER     #####")
while (True):
    print("1: Convert IP Address to Binary")
    print("2: Convert Binary Address to Decimal IP")
    print("3: Calculate Subnet Mask")
    print("4: Find Addresses")
    print("5: Find Addresses for Network")
    print("-1: Exit")
    choice = int(input("Select: "))
    match choice:
        case 1:
            address = input("Address: ")
            print(ip_to_binary(address))
        case 2:
            address = input("Address: ")
            print(binary_to_ip(address))
        case 3:
            hosts = int(input("# of hosts: "))
            print(calculate_subnet_mask(hosts))
        case 4:
            address = input("Address: ")
            hosts = int(input("# of hosts: "))
            print_addresses(find_addresses(address, hosts))
        case 5:
            address = input("Address: ")
            lans = int(input("# of LANs: "))
            hosts_list = {}
            for i in range(0, lans):
                hosts = int(input("LAN " + str(i+1) + " # of hosts: "))
                hosts_list[i] = (hosts)
            print_address_book(find_addresses_for_network(address, hosts_list))
        case -1:
            break
    print('\n')