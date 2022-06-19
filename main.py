def Brute(Text):
    DecryptText = ""
    Key = 1 
    alfabe=['a','b' ,'c' ,'ç', 'd', 'e', 'f', 'g' ,'ğ' , 'h' ,'ı' , 'i' ,'j','k' ,'l' ,'m' ,'n' ,'o' ,'ö' , 'p' ,'r' ,'s' ,'ş','t' ,'u' ,'ü', 'v', 'y' ,'z']
    while Key < 65:
        for i in Text:


        #DecryptText+=alfabe[(alfabe.index(i)+3)%len(alfabe)]
         # DecryptText = "'a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'ı','i', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'r', 's', 'ş', 't', 'u', 'ü', 'v', 'y', 'z' "
            DecryptText = DecryptText + chr(ord(i) - Key)
        print("[+] Key>>",str(Key) + " Decrypt Text>>",DecryptText)
        Key += 1
        DecryptText = ""


def Encrypt(Text, Key):
    EncryptText = ""
    for i in Text:
        EncryptText = EncryptText + chr(ord(i) + Key)
    print("[+] Key>>",str(Key) + " . Şifreleme>>",EncryptText)

  

print("""

[1] Şifreyi Çöz
[2] şifrele    
[9] Exit
""")

Option = int(input("Option>> "))
if Option == 9:
    print("[-] Exit...")
    exit

elif Option == 1:
    Text = input("[+] Text>> ")
    Brute(Text)
elif Option == 2:
    Text = input("[+] Text>> ")
    Key = int(input("[+] Key>> "))
    Encrypt(Text, Key)
else:
    print("[?] Please Select Options !")
    exit