import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def calculate_b():
    '''
    ok4_32 = 1
    ok4_31 = 2            172.80.50.150/18
    ok4_30 = 4
    ok4_29 = 8
    ok4_28 = 16
    ok4_27 = 32
    ok4_26 = 64
    ok4_26 = 128
    '''

    clear_screen()
    question_input = input("Enter Class B IP (example: 172.80.50.150/18): ")
    question_ip, block_ip = question_input.split('/')
    block_ip = int(block_ip)

    blockip_to_c = block_ip + 8
    total_hosts = 2 ** (32 - blockip_to_c)

    # ========= calculate subnet block
    octets = question_ip.split(".")
    oct3 = int(octets[2])
    net_calc = oct3 / total_hosts

    # ========= calculate NET ID
    net_calc_int = int(net_calc)
    net_id = net_calc_int * total_hosts
    octets[2] = str(net_id)
    octets[3] = "0"
    network_id = ".".join(octets)

    # ========= calculate Broadcast
    broadcast = net_id + total_hosts - 1
    octets[2] = str(broadcast)
    octets[3] = "255"
    broadcast_result = ".".join(octets)

    # ========= calculate Subnetmask
    ip_total = 256
    subnetmask = ip_total - total_hosts
    octets[2] = str(subnetmask)

    clear_screen()
    print("==" * 15)
    print(f"Question: {question_ip}/{block_ip}")

    # output Calculate subnet block
    print("==" * 15)
    print(f"  Octet 3       {oct3}")
    print(f"----------- = ---- = {net_calc}")
    print(f"Total hosts     {total_hosts}")
    print("==" * 15)
    print()

    # ========================================================================

    # output Calculate NET ID
    print("==" * 4, "( Calculate NET ID")
    print("Net ID = Quotient x Total Hosts")
    print(f"       = {net_calc_int} x {total_hosts}")
    print(f"       = {net_id}")
    print(f"Net ID = {network_id} <---")
    print()

    # output Calculate Broadcast
    print("==" * 4, "( Calculate Broadcast")
    print("Broadcast  = Starting IP + Total Hosts - 1")
    print(f"           = {net_id} + {total_hosts} - 1")
    print(f"           = {broadcast}")
    print(f"Broadcast = {broadcast_result} <---")
    print()

    # output Calculate Subnetmask
    print("==" * 4, "( Calculate Subnetmask")
    print("Subnetmask  = IP Total - Total Hosts")
    print(f"             = {ip_total} - {total_hosts}")
    print(f"             = {subnetmask}")
    print(f"Subnetmask = 255.255.{subnetmask}.0 <---")
    print()

