#Kiril Krushkov
#Skilaverkefni_2


def celsius(farenheit): #function til þess að breyta farenheit yfir í celsius
    celsius = (farenheit - 32) / 1.8
    return celsius

def farenheit(celsius): #function til þess að breyta celsius yfir í farenheit
    farenheit = celsius * 1.8 + 32
    return farenheit

def kelvin(celsius): #function til þess að breyta celsius yfir í kelvin
    kelvin = celsius + 273.15
    return kelvin

def celsius(kelvin): #function til þess að breyta kelvin yfir í celsius
    celsius = kelvin - 273.15
    return celsius

def tomma(sentimetri): #function til þess að breyta sentimetra yfir í tommur
    tomma = sentimetri / 0.39370
    return tomma

def sentimetri(tomma): #function til þess að breyta tommum yfir í sentimetra
    sentimetri = tomma * 0.39370
    return sentimetri

def gallon(litri): #function til þess að breyta lítrum yfir í gallons
    gallon = litri * 0.26417
    return gallon

def litri(gallon): #function til þess að breyta gallons yfir í lítra
    litri = gallon / 0.26417
    return litri

def kg(litri): #function til þess að breyta lítrum yfir í kg
    kg = gr * 100
    return gallon

def gr(kg): #function til þess að breyta gallons yfir í gr
    gr = kg * 0.100
    return gr


svar = "ja"

while svar == "ja":
    print("Liður 1 - Farenheit eða Celcius ")
    print("Liður 2 - Kelvin eða Celsius ")
    print("Liður 3 - ")
    print("Liður 4 - Tommur eða Sentimetrar ")
    print("Liður 5 - Gallons eða Litrar")
    print("Liður 6 - Hæta")

    spurning = input("í hvaða lið viltu fara? ")

    if spurning == "1":
# forritið spyr notanda hvort hann vilji breyta í celsius fra farenheit eða öfugt

        hvort = input("viltu breyta yfir í celsius eða farenheit? C/F ")

        if hvort == "C" or hvort == "c":
            far = float(input("hversu heitt er úti í farenheit? "))

            print("Þetta eru í celsius = ",round(celsius(far),2))

        elif hvort == "F" or hvort == "f":
            cel = float(input("hversu margar gráður eru úti? "))

            print("þetta er í farenheit =",round(farenheit(cel),2))

        else:
            print("Villa")


    if spurning == "2":
#forritið spyr notanda hvort hann vilji breyta í celsius í kelvin eða öfugt
        hvort = input("hvort viltu breyta yfir í celsius eða kelvin? K/C ")

        if hvort == "K" or hvort == "k":
            cel = float(input("hversu heitt er úti í celsius? "))

            print("Þetta er í kelvin =",round(kelvin(cel),2))

        elif hvort == "C" or hvort == "c":
            kel = float(input("hversu heitt er úti í kelvin? "))

            print("Þetta er í celsius =",round(celsius(kel),2))

        else:
            print("Villa")

    if spurning == "3":
#forritið spyr notanda hvort hann vilji breyta í kg í g eða öfugt
        hvort = input("hvort viltu breyta yfir í celsius eða kelvin? KG/GR ")

        if hvort == "KG" or hvort == "kg":
            cel = float(input("hversu heitt er úti í kg? "))

            print("Þetta er í kg =", round(kelvin(cel), 2))

        elif hvort == "GR" or hvort == "gr":
            kel = float(input("hversu heitt er úti í g? "))

            print("Þetta er í gr =", round(celsius(kel), 2))

    if spurning == "4":
#forritið spyr notanda hvort hann ilji breyta tommum í sentimetra eða öfugt
        hvort = input("hvort viltu breyta í tommur eða sentimetra? T/S ")

        if hvort == "S" or hvort == "s":
            tom = float(input("hversu langt er þetta í tommum? "))

            print("þetta gerir þá =",round(sentimetri(tom),2),"sentimetra")

        elif hvort == "T" or hvort == "t":
            senti = float(input("hversu langt er þetta í sentimetrum? "))

            print("þetta er þá =",round(tomma(senti),2),"Tommur")

        else:
            print("Villa")

#liðurinn spyr notanda hvort hann vilji breyta lítra yfir í gallon eða öfugt
#svo skrifar notandi litrann eða gallonið sem hann vill breyta og þa fer forritið og notar function-ið sem er eftst til að reikna á milli

    if spurning == "5":
#forritið spyr notanda hvort hann vilji breyta gallons í litra eða öfugt
        hvort = input("hvort viltu breyta í gallon eða lítra? G/L ")

        if hvort == "G" or hvort == "g":
            lit = float(input("hversu margir lítrar eru þetta? "))
            print("þetta gerir þá =",round(gallon(lit),2),"gallons")

        if hvort == "L" or hvort == "l":
            gall = float(input("hversu margir gallons eru þetta? "))

            print("Þetta gerir þá =",round(litri(gall),2),"Lítra")

        else:
            print("Villa")

    if spurning == "6":
        break