# string ifadelerin detaylari
"a" + "B"

"a" + " B"

"a" + " + B"

"abc" + "cdf"

"a" * "B"

"a" * 3

"a"  + "3"

"a" / 3

"a" / "b"

"a" - 3

"a" - "b"

# string Method'lari " -len()"
a = 11
b = 13

a * b


hello = "merhaba dünya"

print (hello)

len(hello)

len("hello")

# string Metodları / upper() & lower()

hello.upper()

B = hello.upper()
print (B)

B.lower()
B.islower()
B.isupper()

# string Metodları / replace()

hello.replace("ü", "u")
print (hello)
print (hello.replace("ü", "u"))

# string Metodları / strip()
hello= "_merhaba_dünya_"
print (hello)

hello.strip()
hello.strip("_")

hello= hello.strip("_")
print (hello)

# METHOD'lara genel bakış
dir(hello)

# substrings / index()
print(hello)
len(hello)
hello[13]
hello[12]
hello[0:7]
hello[1:9]
# değişkenler / variables
A = 111
B = 113
p = 3.14

# "type" dönüşümleri
tSayi1 = input()
tSayi2 = input()

# veri Tipleri
    # listeler
        # [] - list()

onar = [10, 20, 30, 40]
beser = [5, 10, 15, 20]    
onbeser = [onar, beser]

type(onbeser)
type(onbeser[0])
type(onbeser[1])
type(beser[0])


sinif = [3.14, 314, "okul", onbeser]
type(sinif[0])
type(sinif[1])
type(sinif[2])
type(sinif[3])

    # listeler
        # eleman işlemleri
            # çağırma - listeleme

aile = ["ali", "veli", "ayşe", "sinem"]

aile
aile[:2]
aile[3:]

        # eleman işlemleri
            # ekleme, slime, değiştirme
            
aile
aile + ["kemal"]
aile = aile + ["kemal"]
aile
del(aile[4])
aile
aile[2]="ayse"

# listeler
    # liste metodları
        # append & remove

araba = ["BMW", "MERCEDES", "VOLVO"]

araba.append("OPEL")
araba

araba.remove("VOLVO")
araba

        # insert

araba.insert(2,"VOLVO")
araba

araba.insert(len(araba), "FORD")
araba

        # pop
        
araba.insert(len(araba),"FORD")
araba.insert(len(araba), "FIAT")

araba.pop(5)
araba.pop((len(araba) - 1))

        # count (eşdeğerleri sayar)

araba.append("OPEL")

araba.count("BMW")
araba.count("VOLVO")
araba.count("OPEL")

        # copy
        
araba_yedek = araba.copy()       
        
        # extend
        
araba.extend(["HONDA", "TOYOTA", "MAZDA", "PAGANI"])        
araba        

        # index

araba.index("HONDA")
araba.index("BMW")

        # reverse

araba.reverse()
araba
araba.reverse()
araba

        # short

ikili = [2,8,4,6]
ikili.sort()
ikili
        
        # clear
ikili.clear()
ikili


# Veri Tipleri
    # tuple() - ()

Aile = (1, 2, 3, 4)
Aile = ("ozgun", "sebnem", "taha", "yunus")

Aile[1]        
Aile[:3]
kume = ("ali", "veli", 2, 3, 3.14,["a", "b", "c"])
kume[5]



