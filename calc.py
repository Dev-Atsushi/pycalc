def sum(firstag, secondag):
    return int(firstag) + int(secondag)

def sub(firstag, secondag):
    return int(firstag) - int(secondag)

def div(firstag, secondag):
    return int(firstag) / int(secondag)

def mut(firstag, secondag):
    return int(firstag) * int(secondag)

while True:
    num = input("Me diga o primeiro número: ")
    ndus = input("Me diga o segundo número: ")
    oq = input("Você quer mutiplicar, dividir, somar ou subtrair? ")

    if(oq.lower() == "dividir"):
        print("[/] Seu resultado é", div(num, ndus))
    elif(oq.lower() == "somar"):
        print("[+] Seu resultado é", sum(num, ndus))
    elif(oq.lower() == "subtrair"):
        print("[-] Seu resultado é", sub(num, ndus))
    elif(oq.lower() == "mutiplicar"):
        print("[*] Seu resultado é", mut(num, ndus))

    input("[x] Para usar novamente a calculadora precione qualquer tecla...")
