from src import hitung_ip_b, hitung_ip_c
import os

def banner():
    print("""
     __  ____     ___  __   _  _  __ _  ____
    (  )(  _ \   / __)/  \ / )( \(  ( \(_  _)
     )(  ) __/  ( (__(  O )) \/ (/    /  )(  
    (__)(__)     \___)\__/ \____/\_)__) (__) 
    
    """)

def menu():
    os.system('cls')
    banner()
    print("Pilih opsi:")
    print("1. Hitung IP B")
    print("2. Hitung IP C")
    choice = input("Masukkan pilihan (1 atau 2): ")
    if choice == '1':
        hitung_ip_b.calculate_b()
    elif choice == '2':
        hitung_ip_c.calculate_c()
    else:
        print("Pilihan tidak valid. Coba lagi.")
        menu()

if __name__ == "__main__":
    menu()
