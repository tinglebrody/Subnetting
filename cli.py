import subnet

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
            print(subnet.ip_to_binary(address))
        case 2:
            address = input("Address: ")
            print(subnet.binary_to_ip(address))
        case 3:
            hosts = int(input("# of hosts: "))
            print(subnet.subnet_mask(hosts))
        case 4:
            address = input("Address: ")
            hosts = int(input("# of hosts: "))
            subnet.print_addresses(subnet.addresses(address, hosts))
        case 5:
            address = input("Address: ")
            lans = int(input("# of LANs: "))
            hosts_list = {}
            for i in range(0, lans):
                hosts = int(input("LAN " + str(i+1) + " # of hosts: "))
                hosts_list[i] = (hosts)
            subnet.summary(subnet.network_addresses(address, hosts_list))
        case -1:
            break
    print('\n')