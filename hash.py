import hashlib

def hash(entry):
    password = str(entry)
    plaintext = password.encode()
    d = hashlib.sha256(plaintext)

    #Hacer un binary hash del password
    hasher = d.digest()
    # Crear un hash que pueda ser leido por algun humano
    hasher = d.hexdigest()


    return hasher
