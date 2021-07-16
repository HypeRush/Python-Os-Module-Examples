import os

print (os.name)
print("şuan bulunduğun dizin:",os.getcwd())
path = input("Taranacak yerin pathi:",)
if path == (""):
    print (path , "Hiç bir yer bulunamadı")  
else:
    dir_list = os.listdir(path) 
    print("Aranan yerdeki dosyalar ve klasörler'", path, "' :") 
    print(dir_list) 
    goatten = input("Silmek istediğiniz dosyanın adını yazın(silmeyecekseniz boş bırakın)",)
    if goatten == (""):
          print (goatten , "Hiç bir şey silinmedi")    
    else: 
          print(goatten, "adlı dosya siliniyor")
          filewillbedeleted = os.path.join(path, goatten) 
          os.remove(filewillbedeleted)
          print(goatten, "adlı dosya başarıyla silindi")





  




