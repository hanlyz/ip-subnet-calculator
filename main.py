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
    print("Select an option:")
    print("1. Calculate IP Class B")
    print("2. Calculate IP Class C")
    choice = input("Enter your choice (1 or 2): ")
    if choice == '1':
        hitung_ip_b.calculate_b()
    elif choice == '2':
        hitung_ip_c.calculate_c()
    else:
        print("Invalid choice. Please try again.")
        menu()

if __name__ == "__main__":
    menu()
