k = input("k: ")
word = input("word: ")

# Fehlerbehandlung
# Ungültiges k

if k.isalpha() or not word.isalpha():
    print("False")
   
else:
    print("True")
   
