
# Initialises the variables
key = int(input("Key = ")) # How Much you want the end of the message to be cut off
encrypt = input("Say a message to encrypt: ") # The messages/codes sent
encryption = [] # The list of messages/codes sent


# Function stuff(Annoying to explain)
def scrambleIt(val, key) :
    c = val[-key:]
    out = c + val[:len(encrypt)-key:]
    return out

# While loop
while encrypt != "": #If theres no message then there is nothing to scramble so it stops
    scram = scrambleIt(encrypt, key) #variable that gets the scrambled version of the messages
    encryption.append(scram) ## Appends(Adds) the scrambled version of the message to the list.
    encrypt = input("Say a message to encrypt: ") ## Asks for another message now

#FORRRRR LOOOOOOOP
for e in encryption:
    print(e) #Yea it justs prints it cleanly in a column

