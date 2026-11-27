key = int(input("Key = "))
encrypt = input("Say a message to encrypt: ")
encryption = []

def scrambleIt(val, key) :
    c = val[-key:]
    out = c + val[:len(encrypt)-key:]
    return out

while encrypt != "":
    scram = scrambleIt(encrypt, key)
    encrypt = input("Say a message to encrypt: ")
    encryption.append(scram)

for e in encryption:
    print(e)

