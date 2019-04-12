from texttable import Texttable
table1 = Texttable ()
def pembayaran () :
    no1 = 0
    nama = []
    nim = []
    kls = []
    uts = []
    uas = []
    bulan = []
    bseminar = []
    bkas = []
    admin = []
    jawab = 'y'
    while (jawab == 'y'):
        print("____________________________________________")
        print("\n\tPembayaran Kampus Pelita Bangsa")
        print("============================================")
        nama.append(input("Nama   : ")) 
        nim.append(input("NIM    : "))
        kls.append(input("Kelas  : "))
        print("============================================")
        print("Pilih pembayaran\n\t1. Pembayaran UTS\n\t2. Pembayaran UAS")
        plh = input("Masukan pilihan : ")
        if  (plh == '1') :
            uas.append(0)
            print("+++=====Pembayaran UTS=====+++")
            uts.append(input("Masukan jumlah mata kuliah yang akan dibayar : "))
        elif (plh == '2') :
            uts.append(0)
            print("+++=====Pembayaran UAS=====+++")
            uas.append(input("Masukan jumlah mata kuliah yang akan dibayar : "))
        else:
            break
        bulan.append(input("Masukan jumlah bulan yang akan dibayar       : "))
        smr = input("Bayar Seminar (y/t)                          : ")
        if (smr == 'y') :
            bseminar.append(100000)
        else :
            bseminar.append(0)
        kas = input("Bayar kas (y/t)                              : ")
        if (kas == 'y') :
            bkas.append(20000)
        else :
            bkas.append(0)
        admin.append(5000)
        print("Admin 5000")
        jawab = input("Tambah data (y/t)")
        no1 +=1
    for i1 in range (no1) :
        blan = int(bulan[i1])
        us = int(uts[i1])
        ua = int(uas[i1])
        bbulan = (blan*500000)
        buts = (us*50000)
        buas = (ua*50000)
        total = (bbulan + buts + buas + bkas[i1] + bseminar[i1] + admin[i1])
        table1.set_cols_width([2,10,10,10,7,7,7,7,7,7,8])
        table1.set_cols_dtype(['i','t','i','t','i','i','i','i','i','i','i'])
        table1.set_cols_align(['c','l','c','c','c','c','c','c','c','c','c'])
        table1.add_rows([['No','Nama','NIM','Kelas','UTS','UAS','SPP','Seminar','Kas','Admin','Total'],
                        [i1+1, nama[i1],nim[i1],kls[i1],buts,buas,bbulan,bseminar[i1],bkas[i1],admin[i1],total]])                      
    print(table1.draw())

    
