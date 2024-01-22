def ip_to_binary(address):
    octets = address.split('.')
    binary_ip = ''
    for octet in octets:
        binary_ip = binary_ip + format(int(octet), '08b')+ '.'
    binary_ip = binary_ip[:-1]
    print(binary_ip)
    
def binary_to_ip(address):
    octets = address.split('.')
    decimal_ip = ''
    for octet in octets:
        decimal_ip = decimal_ip + str(int(octet, 2)) + '.'
    decimal_ip = decimal_ip[:-1]
    print(decimal_ip)
    
    
print('\n')
print("#####    SUBNETTING HELPER   #####")
print("What would you like to do?")
print("(1): Convert IP Address to Binary")
print("(2): Convert Binary Address to Decimal IP")
choice = int(input("Select: "))
match choice:
    case 1:
        address = input("Address: ")
        ip_to_binary(address)
    case 2:
        address = input("Address: ")
        binary_to_ip(address)
print('\n')