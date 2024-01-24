import pytest
from simplesubnet import subnet as subnetter

ip = "192.168.5.0"
hosts = {1: 64, 2: 45, 3: 14, 4: 9}

def test_valid_subnet():
    assert subnetter.network_addresses(ip, hosts)[2]['broadcast'] == '192.168.5.191/26'
    