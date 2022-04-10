import hashlib

def hash(password):
    plaintext = password.encode()
    d = hashlib.sha256(plaintext)

    #Hacer un binary hash del password
    hasher = d.digest()
    # Crear un hash que pueda ser leido por algun humano
    hasher = d.hexdigest()
    print(hasher)


    return hasher