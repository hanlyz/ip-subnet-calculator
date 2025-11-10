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
    soal_input = input("Masukkan soal IP C (contoh: 192.180.35.220/18): ")
    soal_ip, block_ip = soal_input.split('/')
    block_ip = int(block_ip)

    jumlah_host = 2 ** (32 - block_ip)

    # ========= hitung block subnet
    oktets = soal_ip.split(".")
    okt4 = int(oktets[3])
    hasil_net = okt4 / jumlah_host

    # ========= hitung NET ID
    hasil_netid = int(hasil_net)
    net_id = hasil_netid * jumlah_host
    oktets[3] = str(net_id)
    network_id = ".".join(oktets)

    # ========= hitung Broadcast
    broadcast = net_id + jumlah_host - 1
    oktets[3] = str(broadcast)
    broadcast_hasil = ".".join(oktets)

    # ========= hitung Subnetmask
    ip_total = 256
    subnetmask = ip_total - jumlah_host

    clear_screen()
    print("==" * 15)
    print(f"Soal: {soal_ip}/{block_ip}")

    print("==" * 15)
    print(f"  oktet 4     {okt4}")
    print(f"----------- = ----- = {hasil_net}")
    print(f"jumlah host   {jumlah_host}")
    print("==" * 15)
    print()

    # output Hitung NET ID
    print("==== ( Hitung NET ID )")
    print("Net ID = Hasil bagi x jumlah host")
    print(f"       = {hasil_netid} x {jumlah_host}")
    print(f"       = {net_id}")
    print(f"Net ID = {network_id} <---")
    print()

    # output Hitung Broadcast
    print("==== ( Hitung Broadcast )")
    print("Broadcast  = IP Awal + jumlah host - 1")
    print(f"           = {net_id} + {jumlah_host} - 1")
    print(f"           = {broadcast}")
    print(f"Broadcast = {broadcast_hasil} <---")
    print()

    # output Hitung Subnetmask
    print("==== ( Hitung Subnetmask )")
    print("Subnetmask  = IP Total - jumlah host")
    print(f"           = {ip_total} - {jumlah_host}")
    print(f"           = {subnetmask}")
    print(f"Subnetmask = 255.255.255.{subnetmask} <---")
    print()

