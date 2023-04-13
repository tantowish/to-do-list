import Stack
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
=====================================
''')
# Input tugas, kepentingan, kesusahan (1-5)
stack = Stack.Stack()
n =int(input("Jumlah tugas : "))
print("Cara input :\nnama_tugas(spasi)kepentingan(spasi)kesusahan")
for i in range(n):
  tugas = list(map(str,input("Tugas "+str(i+1)+" : ").split()))
  tugas[1] = int(tugas[1])*int(tugas[2]) # Bobot kepentingan * kesusahan 
  tugas.pop(2)
  stack.push(tugas)
stack.bubbleSort()
print("\nMaka didapat antrian tugas seperti berikut : ")
stack.display()
print()
# Sorting dari bobot terbesar ke terkecil
# Antrian penyelesaian tugas yang sudah disorting tadi