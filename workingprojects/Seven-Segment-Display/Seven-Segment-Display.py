
rakamlar = {"0":["1","1","1","1","1","1","0"],
            "1":["0","1","1","0","0","0","0"],
            "2":["1","1","0","1","1","0","1"],
            "3":["1","1","1","1","0","0","1"],
            "4":["0","1","1","0","0","1","1"],
            "5":["1","0","1","1","0","1","1"],
            "6":["1","0","1","1","1","1","1"],
            "7":["1","1","1","0","0","0","0"],
            "8":["1","1","1","1","1","1","1"],
            "9":["1","1","1","1","0","1","1"],}

satir1=satir2=satir3=satir4=satir5=satir6=satir7=satir8=satir9=""

def Rakamlar(yazilan):
    global satir1,satir2,satir3,satir4,satir5,satir6,satir7,satir8,satir9
    for rakam in yazilan:
        liste = rakamlar[rakam]
        for i in range(len(rakamlar[rakam])):
            if liste[i] == "1":
                liste[i]="#"
            else:
                liste[i]=""


        a,b,c,d,e,f,g = rakamlar[rakam]


        satir1+=f"  {a} {a} {a}\t\t"
        satir2+=f"{f}       {b}\t"
        satir3+=f"{f}       {b}\t"
        satir4+=f"{f}       {b}\t"
        satir5+=f"  {g} {g} {g}\t\t"
        satir6+=f"{e}       {c}\t"
        satir7+=f"{e}       {c}\t"
        satir8+=f"{e}       {c}\t"
        satir9+=f"  {d} {d} {d}\t\t"



Rakamlar(input("Sayı Giriniz: "))
print(f"""
                {satir1}
                {satir2}
                {satir3}
                {satir4}
                {satir5}
                {satir6}
                {satir7}
                {satir8}
                {satir9}
                """)
