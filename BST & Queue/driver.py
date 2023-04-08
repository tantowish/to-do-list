from Queue import Queue
import os

queue = Queue()

def tugasDisplay():
    if(queue.isEmpty()==True):
        return
    else:
        print("Antrian Tugas : ")
        queue.display()
        print("\n")

def menu():
   os.system('cls||clear')
   tugasDisplay()
   print("1. Input Tugas")
   print("2. Selesaikan Tugas")
   print("3. Keluar")
   pil=int(input("Pilih : "))
   if pil==1:
       return inp()
   elif pil==2:
        return garap()
   elif pil==3:
       return
   else:
       return menu()

def inp():
    print('''
    =====================================
    |     |    K e p e n t i n g a n    |
    =====================================
    |  k  |  1  |  2  |  3  |  4  |  5  |
    |  e  |     |     |     |     |     |
    |  s  |  2  |  4  |  6  |  8  |  10 |
    |  u  |     |     |     |     |     |
    |  s  |  3  |  6  |  9  |  12 |  15 |
    |  a  |     |     |     |     |     |
    |  h  |  4  |  8  |  12 |  16 |  20 |
    |  a  |     |     |     |     |     |
    |  n  |  5  |  10 |  15 |  20 |  25 |
    |     |     |     |     |     |     |
    =====================================''')
    # Input tugas, kepentingan, kesusahan (1-5)
    n =int(input("Jumlah tugas : "))
    print("Cara input :\nnama_tugas(spasi)kepentingan(spasi)kesusahan")
    for i in range(n):
        tugas = list(map(str,input("Tugas "+str(i+1)+" : ").split()))
        tugas[1] = int(tugas[1])*int(tugas[2]) # Bobot kepentingan * kesusahan 
        tugas.pop(2)
        queue.enqueue(tugas)
    return menu()

def garap():
    if(queue.isEmpty()==True):
        print("Tidak ada tugas yang perlu dikerjakan")
        return menu()
    else:
        print("Antrian Tugas : ")
        queue.display()
    print("\n\nketik 'selesai' untuk menyelesaikan tugas\n'kembali' untuk kembali ke menu\n")
    while(queue.isEmpty() != True):
        print("Tugas tersisa :",queue.size)
        queue.display()
        query=input("\n")
        if query.lower()=="selesai":
            queue.dequeue()
        elif query.lower()=="kembali":
            return menu()
    print("Semua tugas telah selesai")
    return menu()

menu()