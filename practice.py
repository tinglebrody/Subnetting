import subnet

ip = '192.168.0.0'
hosts_needed = {1: 200, 2: 3000, 3: 7}
subnet.summary(subnet.network_addresses(ip, hosts_needed))

