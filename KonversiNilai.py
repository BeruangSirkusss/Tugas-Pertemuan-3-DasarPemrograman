nilai = int(input(" Masukan Nilai :"))

if nilai <50 :
    hasil = "E"

elif nilai >=50 and nilai <60 :
    hasil = "D"
    
elif nilai >=60 and nilai <70 :
    hasil = "C"

elif nilai >=70 and nilai <80 :
    hasil = "B"
    
elif nilai >=80 :
    hasil = "A"
    
print("Jika Kamu Mendapatkan Nilai",nilai," Maka Kamu Mendapatkan",hasil)