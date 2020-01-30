import sys
import string # Required to call maketrans function.

#Input = "Testing, Testing, 123"
Input = "aRt/=,XyZaRt/=,XyZ+73"

#Type = "Encrypt"
Type = "Decrypt"

#Encryption Key, must have same length as charlist, and should have one of every character
Key = 'a9z8b7c6d 5e4f3g2h1i0j/k*l-m=y.x,w+vAuBtCsDrnEoFpGqHZIYJXKWLMUVNOPSTQR'
Charlist = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789/*-+=., ' # Character list
#print (len(Key), len(Charlist))


if Type == "Encrypt" :
  trans = str.maketrans(Key, Charlist)
  Encryptedstr = Input.translate(trans)
  print (Encryptedstr)

if Type == "Decrypt" :
  trans = str.maketrans(Charlist, Key)
  Decryptedstr = Input.translate(trans)
  print (Decryptedstr)
