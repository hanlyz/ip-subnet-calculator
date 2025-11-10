import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def calculate_c():
    '''
    ok4_32 = 1
    ok4_31 = 2            192.180.35.220/27
    ok4_30 = 4
    ok4_29 = 8
    ok4_28 = 16
    ok4_27 = 32
    ok4_26 = 64
    ok4_26 = 128
    '''

    clear_screen()
    question_input = input("Enter Class C IP (example: 192.180.35.220/27): ")
    question_ip, block_ip = question_input.split('/')
    block_ip = int(block_ip)

    total_hosts = 2 ** (32 - block_ip)

    # ========= calculate subnet block
    octets = question_ip.split(".")
    oct4 = int(octets[3])
    net_calc = oct4 / total_hosts

    # ========= calculate NET ID
    net_calc_int = int(net_calc)
    net_id = net_calc_int * total_hosts
    octets[3] = str(net_id)
    network_id = ".".join(octets)

    # ========= calculate Broadcast
    broadcast = net_id + total_hosts - 1
    octets[3] = str(broadcast)
    broadcast_result = ".".join(octets)

    # ========= calculate Subnetmask
    ip_total = 256
    subnetmask = ip_total - total_hosts

    clear_screen()
    print("==" * 15)
    print(f"Question: {question_ip}/{block_ip}")

    print("==" * 15)
    print(f"  Octet 4     {oct4}")
    print(f"----------- = ----- = {net_calc}")
    print(f"Total hosts   {total_hosts}")
    print("==" * 15)
    print()

    # output Calculate NET ID
    print("==== ( Calculate NET ID )")
    print("Net ID = Quotient x Total Hosts")
    print(f"       = {net_calc_int} x {total_hosts}")
    print(f"       = {net_id}")
    print(f"Net ID = {network_id} <---")
    print()

    # output Calculate Broadcast
    print("==== ( Calculate Broadcast )")
    print("Broadcast  = Starting IP + Total Hosts - 1")
    print(f"           = {net_id} + {total_hosts} - 1")
    print(f"           = {broadcast}")
    print(f"Broadcast = {broadcast_result} <---")
    print()

    # output Calculate Subnetmask
    print("==== ( Calculate Subnetmask )")
    print("Subnetmask  = IP Total - Total Hosts")
    print(f"           = {ip_total} - {total_hosts}")
    print(f"           = {subnetmask}")
    print(f"Subnetmask = 255.255.255.{subnetmask} <---")
    print()

    input("Press Enter to go back...")
    return


