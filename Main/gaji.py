def gaji () :
    from texttable import Texttable
    table1 = Texttable ()
    no1 = 0
    nama1 = []
    jabatan = []
    gaji = []
    jawab1 = "ya"

    while (jawab1 == 'ya'):
        nama1.append(input("Masukan Nama: "))
        jab = input("Jabatan : ")
        jabatan.append(jab)
        if  (jab == 'Operator') :
            gaji.append(3000000)
        
            jawab1 = input("\nTambah Lagi (y/t)? ")
        elif (jab == 'Leader') :
            gaji.append(3300000)
        
            jawab1 = input("\nTambah Lagi (y/t)? ")
        elif (jab == 'Supervisor') :
            gaji.append(4500000)
            jawab1 = input("\n Tambah lagi (y/t)? ")
        elif (jab == 'Manajer') :
            gaji.append(7000000)
            
            jawab1 = input("\n Tambah lagi (y/t)? ")     
        else:
            break
        no1+=1
       
    for i1 in range (no1) :
        table1.set_cols_width([2,10,10,10])
        table.set_cols_dtype(['i','t','t','i'])
        table.set_cols_align(['c','l','c','c'])
        table1.add_rows([['No','Nama','Jabatan','Gaji'], [i1+1, nama1[i1],jabatan[i1],gaji[i1]]])                      
    print(table1.draw())

