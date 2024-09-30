import random
def parola_olustur(parola_uzunluğu):

    karakterler = '+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    parola = ""
    for i in range(parola_uzunluğu):
        parola += random.choice(karakterler)

    return parola

#print=parola_olustur[8:]