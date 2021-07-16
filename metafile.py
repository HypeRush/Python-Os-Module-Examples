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
    goatten = input("Sorgulamak istediğiniz dosyanın adını yazın(sorgulamayacaksanız boş bırakın)",)
    if goatten == (""):
          print (goatten , "Hiç bir şey sorgulanmadı")    
    else: 
          print(goatten, "adlı dosya sorgulanıyor...")
          print(os.stat(goatten))
          print(goatten, "adlı dosya başarıyla sorgulandı")


