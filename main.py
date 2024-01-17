import masik

szoveg: str="Első szöveg" # globális változó ebben a modulban látszik

print(szoveg)

#print(szoveg2) # ez a változó itt nem látszik

def eljaras():
    szoveg: str="Másik szöveg az eljárásban"
    print(szoveg)
    szoveg2: str="eljárásban"
    print(szoveg2) #  lokális változó csak az eljárásban érhető el


eljaras()

# print(szoveg2)

def masikeljaras():
    # print(masikvalami)
    print(valami) # cannot access local variable 'valami' where it is not associated with a value
    valami: str="valami"

# masikeljaras()

################### egyszerű adattípus, int, string
def elj2(valt:int):
    valt += 1
    print(valt) # 13

valt: int= 12

elj2(valt) 

print("valt", valt) # valt, 12

################### összetett adattípus, list
def elj3(lista):
    lista[0]=11111111111
    for i in range(0, len(lista), 1):
        print(lista[i])

lista=[1,2,3,4,5,6,7]

elj3(lista) 

for i in range(0, len(lista), 1):
        print("lista az eljárás hívása után", lista[i])