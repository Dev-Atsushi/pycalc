def sum(firstag, secondag):
    return int(firstag) + int(secondag)

def sub(firstag, secondag):
    return int(firstag) - int(secondag)

def div(firstag, secondag):
    return int(firstag) / int(secondag)

def mut(firstag, secondag):
    return int(firstag) * int(secondag)

while True:
    num = input("Tell me the first number: ")
    ndus = input("Tell me the second number: ")
    oq = input("Do you want to multiply, divide, add or subtract? ")

    if(oq.lower() == "divide"):
        print("[/] Its result is", div(num, ndus))
    elif(oq.lower() == "add"):
        print("[+] Its result is", sum(num, ndus))
    elif(oq.lower() == "subtract"):
        print("[-] Its result is", sub(num, ndus))
    elif(oq.lower() == "mutiply"):
        print("[*] Its result is", mut(num, ndus))

    input("[x] To use the calculator again, press any key...")
