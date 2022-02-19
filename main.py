import os
import time
lista_zakupow=[]
while True:
    os.system("clear")
    OPCJE=int(input("Uzytkowniku, w celu dalszego działania, wybierz opcje:\n1. Dodanie zakupu do listy\n2. Modyfikacja listy\n3. Usuwanie zakupu z listy\n4. Czyszczenie listy\n5. Zliczanie wystąpień zakupu\n6. Zakończenie\n "))
    if OPCJE==1:
        while True:
            ELEMENT_LISTY=input("Wpisz zakup:")
            lista_zakupow.append(ELEMENT_LISTY)
            DODANIE=input("Czy chcesz dodać coś jeszcze? ")
            if DODANIE=="nie":
                break
    elif OPCJE==2 and len(lista_zakupow)>0:
        print(lista_zakupow)
        MODYFIKACJA_NUMER=int(input("Który element chcesz zmodyfikować: "))-1
        MODYFIKACJA_ELEMENT=input("Na jaki produkt chcesz zmienić: ")
        lista_zakupow[MODYFIKACJA_NUMER]=MODYFIKACJA_ELEMENT
    elif OPCJE==3:
        print(lista_zakupow)
        USUWANIE=input("Który produkt chcesz usunąć: ")
        lista_zakupow.remove(USUWANIE)
    elif OPCJE==4:
        lista_zakupow.clear()
    elif OPCJE==5:
        ZLICZANY_ELEMENT=input("Uzytkowniku, ktory zakup chcesz zliczyc?")
        LICZENIE=lista_zakupow.count(ZLICZANY_ELEMENT)
        print(f"Zakup {ZLICZANY_ELEMENT} wystąpił {LICZENIE} raz/y.")
        time.sleep(5)
    elif OPCJE==6:
        break
    else:
        print("Nie rozumiem.")
print(lista_zakupow)

