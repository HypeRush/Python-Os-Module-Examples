import os
if os.name == "nt":
      operatingsys = "windows"
elif os.name == "posix" or os.name == "Linux" or os.name == "Linux2":
      operatingsys == "posix"
else:
      operatingsys == "Cannot find your operating system via os module" 


print(operatingsys)
print("şuan bulunduğun dizin:",os.getcwd())
path = input("Taranacak yerin pathi:",)


def main(path):
    if path == (""):
      path = os.getcwd()
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



if __name__ == "__main__":
      main(path)

