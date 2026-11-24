##    key = int(input("Key = "))
##    encryption = [input("Say a message to encrypt: ")]
##    encrypt = ""
##    while encrypt.lower() != "stop":
##        encrypt = input("Say a message to encrypt: ")
##        encryption.append(encrypt)

lines = []
print("Enter your text (press Enter on an empty line to finish):")

while True:
    line = input()
    if line == "":
        break
    lines.append(line)

text = "\n".join(lines)
print("\nYou entered:\n" + text)
