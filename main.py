lista_zakupow=[]
while True:
    zakup=input("Dodaj zakupy do listy: ")
    lista_zakupow.append(zakup)
    polecenie=input("Czy chcesz zakończyć listę:")
    if polecenie == "tak":
        break
    else:
        zmiana=input("Czy chcesz zmodyfikować swoją listę:")
        if zmiana=="tak":
            zmiana_numer=int(input("Który element chcesz zmienić: "))
            lista_zakupow[zmiana_numer]=str(input("Na co chcesz zmienić:"))       
print(lista_zakupow)

