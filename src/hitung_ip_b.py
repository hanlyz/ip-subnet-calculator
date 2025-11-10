import os

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

    os.system('cls')
    soal_input = input("Masukkan soal IP B (contoh: 172.80.50.150/18): ")
    soal_ip, block_ip = soal_input.split('/')
    block_ip = int(block_ip)

    blockip_to_c = block_ip + 8
    jumlah_host = 2 ** (32 - blockip_to_c)

    # ========= hitung block subnet
    oktets = soal_ip.split(".")
    okt3 = int(oktets[2])
    hasil_net = okt3/jumlah_host

    # ========= hitung NET ID
    hasil_netid = int(hasil_net)
    net_id = hasil_netid*jumlah_host
    oktets[2] = str(net_id)
    oktets[3] = "0"
    network_id = ".".join(oktets)

    # ========= hitung Broadcast
    broadcast = net_id+jumlah_host-1
    oktets[2] = str(broadcast)
    oktets[3] = "255"
    broadcast_hasil = ".".join(oktets)

    # ========= hitung Subnetmask
    ip_total = 256
    subnetmask = ip_total - jumlah_host
    oktets[2] = str(subnetmask)

    os.system('cls')
    print("=="*15)
    print(f"Soal: {soal_ip}/{block_ip}")

    # output Hitung block subnet
    print("=="*15)
    print(f"  oktet 3      {okt3}")
    print(f"----------- = ---- = {hasil_net}")
    print(f"jumlah host    {jumlah_host}")
    print("=="*15)
    print()

    # ========================================================================

    # output Hitung NET ID
    print("=="*4, "( Hitung NET ID")
    print("Net ID = Hasil bagi x jumlah host")
    print(f"       = {hasil_netid} x {jumlah_host}")
    print(f"       =",net_id)
    print(f"Net ID = {network_id} <---")
    print()

    # output Hitung Broadcast
    print("=="*4, "( Hitung Broadcast")
    print("Broadcast  = IP Awal + jumlah host - 1")
    print(f"           = {net_id} + {jumlah_host} - 1")
    print(f"           = {broadcast}")
    print(f"Broadcast = {broadcast_hasil} <---")
    print()

    # output Hitung Subnetmask
    print("=="*4, "( Hitung Subnetmask")
    print("Subnetmask  = IP Total - jumlah host")
    print(f"           = {ip_total} - {jumlah_host}")
    print(f"           = {subnetmask}")
    print(f"Subnetmask = 255.255.{subnetmask}.0 <---")
    print()

