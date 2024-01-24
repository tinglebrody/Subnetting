    simplesubnet
    by Brody Tingle

    This is a simple, lightweight tool that can be used to help with subnetting.

    I created this while studying for my CCNA to help with problems and gain a deeper understanding
    of subnetting.

    To install, run:
        pip3 install simplesubnet

    To import, include this in your header:
        from simplesubnet import subnet

    FUNCTIONS:

    Binary IP to Decimal IP Converter:
        subnet.binary_to_ip(address):
            returns a string representing the decimal IP address

    Decimal IP to Binary IP Converter:
        subnet.ip_to_binary(address):
            returns a string representing the decimal IP address

    Calculate proper subnet mask based on amount of hosts needed:
        subnet.subnet_mask(num_hosts):
            returns the subnet mask as an INTEGER (i.e /30 => 30)

    Calculate Network and Broadcast Address given an address and a number of needed hosts:
        subnet.addresses(starting_address, hosts):
            returns a dictionary containing values:
                ['network'] = network address
                ['broadcast'] = broadcast address

    Calculate Network and Broadcast Addresses for a network with
    multiple LAN's provided # of hosts per LAN. Uses VLSM to calculate.
        subnet.network_addresses(starting_address, hosts):
            hosts is a dictionary containing the # of hosts per VLAN:
                ex. {1: 64, 2: 45, 3: 14: 4: 9}
            returns a dictionary of dictionaries from the {addresses} method
            keys are VLAN #'s
                ex:
                    {1: {'network': 192.168.5.0/25, 'broadcast': 192.168.5.127/25},
                    2: {'network': 192.168.5.128/26, 'broadcast': 192.168.5.191/26}}
    Summary Function:
        subnet.summary(address_book):
            address_book is a dictionary returned from the {network_addresses} function
            prints the dictionary in clean formatting
