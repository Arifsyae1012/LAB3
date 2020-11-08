#Bilangan acak
print ("menampilkan n bilangan acak yang lebih kecil dari 0,5")
jumlah =int (input("masukkan jumlah n = "))
import random
for i in range(jumlah) :
    print("Data ke -> ", 1+i, "=",(random.uniform(0.0,0.5)))