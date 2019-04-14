from Main.nilai import nilai
from Main.gaji import gaji
from Main.kalkulator import kalkulator
from Main.pembayaran import pembayaran
def login ():
    username = input("Welcome to apps!\n\nUsername: ")
    import getpass
    password = getpass.getpass()
    if username == 'admin' and password == 'abc123':
        print("Welcome!")
        pilihan()
    else: 
        print("username atau password anda salah!")
        login()
def pilihan():
        print("==============PILIHAN PROGRAM============")
        print("\n\t========PILIHAN=======\n\t1. Penilaian\n\t2. Penggajian\n\t3. Pembayaran \n\t4. Kalkulator")
        pilih = input("\n\tSILAHKAN PILIH PROGRAMNYA :")
        if pilih == "1" :
            nilai()
            lagi()
        elif pilih == "2" :
            gaji()
            lagi()
        elif pilih == "3" :
            pembayaran()
            lagi()
        elif pilih == "4" :
            kalkulator()
            lagi()
        else :
            print("\n\t================TERIMAKASIH===============")
def lagi() :
    tanya = input("\nKEMBALI LAGI KE PILIHAN PROGRAM (y/t)?")
    if tanya == "y":
        pilihan()
    elif tanya == "t":
        print("====Terimakasih====")
        exit
    else:
        print("====Terimakasih====")
        exit
login()
        
