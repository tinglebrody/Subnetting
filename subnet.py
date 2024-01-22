import math

def ip_to_binary():
    address = input("Address: ")
    octets = address.split('.')
    binary_ip = ''
    for octet in octets:
        binary_ip = binary_ip + format(int(octet), '08b')+ '.'
    binary_ip = binary_ip[:-1]
    print('\n' + binary_ip)
    
def binary_to_ip():
    address = input("Address: ")
    octets = address.split('.')
    decimal_ip = ''
    for octet in octets:
        decimal_ip = decimal_ip + str(int(octet, 2)) + '.'
    decimal_ip = decimal_ip[:-1]
    print('\n' + decimal_ip)

def calculate_needed_hosts(hosts):
    zeroes_from_end = 1
    allowed_hosts = 2
    while (allowed_hosts-2 < hosts):
        allowed_hosts *= 2
        zeroes_from_end += 1
    return allowed_hosts
def calculate_subnet_mask(hosts):
    allowed_hosts = calculate_needed_hosts(hosts)
    mask = '/' + str(32 - int(math.log(allowed_hosts, 2)))
    return mask

def find_addresses(address, hosts):
    octets = address.split('.')
    mask = calculate_subnet_mask(hosts)
    allowed_hosts = calculate_needed_hosts(hosts)
    
    print('Network Address: ' + octets[0] + '.' + octets[1] + '.' + octets[2] + '.' + octets[3] + mask)
    print('First Usable Address: ' + octets[0] + '.' + octets[1] + '.' + octets[2] + '.' 
        + str(int(octets[3]) + 1) + mask)
    print('Broadcast Address: ' + octets[0] + '.' + octets[1] + '.' 
          + octets[2] + '.' + str(int(octets[3]) + allowed_hosts - 2) + mask)
    print('Broadcast Address: ' + octets[0] + '.' + octets[1] + '.' + octets[2] 
          + '.' + str(int(octets[3]) + allowed_hosts - 1) + mask)
    return octets[0] + '.' + octets[1] + '.' + octets[2] + '.' + str(int(octets[3]) + allowed_hosts)

def find_addresses_for_network(address, hosts_list):
    sorted(hosts_list, reverse=True)
    for hosts in hosts_list:
        print('\n')
        next = find_addresses(address, hosts)
        address = next
        
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
            ip_to_binary()
        case 2:
            binary_to_ip()
        case 3:
            hosts = int(input("# of hosts: "))
            print(calculate_subnet_mask(hosts))
        case 4:
            address = input("Address: ")
            hosts = int(input("# of hosts: "))
            find_addresses(address, hosts)
        case 5:
            address = input("Address: ")
            lans = int(input("# of LANs: "))
            hosts_list = []
            for i in range(0, lans):
                hosts = int(input("LAN " + str(i+1) + " # of hosts: "))
                hosts_list.append(hosts)
            find_addresses_for_network(address, hosts_list)
        case -1:
            break
    print('\n')