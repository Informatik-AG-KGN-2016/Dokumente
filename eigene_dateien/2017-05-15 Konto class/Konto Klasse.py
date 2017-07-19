class Konto:
    Kontonummer = 1
    def __init__(self, kontoinhaber, kontostand=0.0):
        if isinstance(kontoinhaber, str) and isinstance(kontostand, (int, float)):
            self.__kontoinhaber = kontoinhaber
            self.__kontonummer = Konto.Kontonummer
            Konto.Kontonummer += 1
            self.__kontostand = float(kontostand)
        else:
            raise Exception

    def info(self):
        print("Kontoinhaber: " + self.__kontoinhaber)
        print("Kontonummer:  " + str(self.__kontonummer))
        print("Kontostand:   " + str(self.__kontostand))


    def einzahlen(self, geldmenge):
        """
        >>> konto1 = Konto("Danilo", 1, 4000)
        >>> konto1.einzahlen(200)
        Einzahlung erfolgreich!
        >>> konto1.info()
        Kontoinhaber: Danilo
        Kontonummer:  1
        Kontostand:   4200.0
        >>> konto1.einzahlen(0)
        Ungültige Geldmenge!
        >>> konto1.info()
        Kontoinhaber: Danilo
        Kontonummer:  1
        Kontostand:   4200.0
        >>> konto1.einzahlen(-20)
        Ungültige Geldmenge!
        >>> konto1.info()
        Kontoinhaber: Danilo
        Kontonummer:  1
        Kontostand:   4200.0
        >>> konto1.einzahlen(800)
        Einzahlung erfolgreich!
        >>> konto1.info()
        Kontoinhaber: Danilo
        Kontonummer:  1
        Kontostand:   5000.0
        """
        if not isinstance(geldmenge, (int, float)):
            return print("Ungültige Geldmenge!")  
        elif geldmenge <= 0:
            return print("Ungültige Geldmenge!")
        else:
            self.__kontostand = self.__kontostand + geldmenge
            return print("Einzahlung erfolgreich!")
        
    def auszahlen(self, geldmenge):
        """
        >>> konto1 = Konto("Danilo", 1, 4000)
        >>> konto1.auszahlen(200)
        Auszahlung erfolgreich!
        >>> konto1.info()
        Kontoinhaber: Danilo
        Kontonummer:  1
        Kontostand:   3800.0
        >>> konto1.auszahlen(0)
        Ungültige Geldmenge!
        >>> konto1.info()
        Kontoinhaber: Danilo
        Kontonummer:  1
        Kontostand:   3800.0
        >>> konto1.auszahlen(-20)
        Ungültige Geldmenge!
        >>> konto1.info()
        Kontoinhaber: Danilo
        Kontonummer:  1
        Kontostand:   3800.0
        >>> konto1.auszahlen(4000)
        Ungültig! Geldmenge übersteigt Kontostand!
        >>> konto1.info()
        Kontoinhaber: Danilo
        Kontonummer:  1
        Kontostand:   3800.0
        >>> konto1.auszahlen(800)
        Auszahlung erfolgreich!
        >>> konto1.info()
        Kontoinhaber: Danilo
        Kontonummer:  1
        Kontostand:   3000.0
        """
        if not isinstance(geldmenge, (int, float)):
            return print("Ungültige Geldmenge!")    
        elif geldmenge <= 0:
            return print("Ungültige Geldmenge!")
        elif geldmenge > self.__kontostand:
            return print("Ungültig! Geldmenge übersteigt Kontostand!")
        else:
            self.__kontostand = self.__kontostand - geldmenge
            return print("Auszahlung erfolgreich!")
        
    def ueberweisen(self, empfaenger_konto, geldmenge):
        """
        >>> konto1 = Konto("Danilo", 1, 4000)
        >>> konto2 = Konto("Detlef", 2, 1000)
        >>> konto1.ueberweisen(konto2, 500)
        Auszahlung erfolgreich!
        Einzahlung erfolgreich!
        Überweisung erfolgreich!
        >>> konto1.info()
        Kontoinhaber: Danilo
        Kontonummer:  1
        Kontostand:   3500.0
        >>> konto2.info()
        Kontoinhaber: Detlef
        Kontonummer:  2
        Kontostand:   1500.0
        >>> konto1.ueberweisen(konto2, 0)
        Ungültige Geldmenge!
        >>> konto1.info()
        Kontoinhaber: Danilo
        Kontonummer:  1
        Kontostand:   3500.0
        >>> konto2.info()
        Kontoinhaber: Detlef
        Kontonummer:  2
        Kontostand:   1500.0
        >>> konto1.ueberweisen(konto2, -20)
        Ungültige Geldmenge!
        >>> konto1.info()
        Kontoinhaber: Danilo
        Kontonummer:  1
        Kontostand:   3500.0
        >>> konto2.info()
        Kontoinhaber: Detlef
        Kontonummer:  2
        Kontostand:   1500.0
        >>> konto1.ueberweisen(konto2, 4000)
        Ungültig! Geldmenge übersteigt Kontostand!
        >>> konto1.info()
        Kontoinhaber: Danilo
        Kontonummer:  1
        Kontostand:   3500.0
        >>> konto2.info()
        Kontoinhaber: Detlef
        Kontonummer:  2
        Kontostand:   1500.0
        >>> konto1.ueberweisen(konto2, 500)
        Auszahlung erfolgreich!
        Einzahlung erfolgreich!
        Überweisung erfolgreich!
        >>> konto1.info()
        Kontoinhaber: Danilo
        Kontonummer:  1
        Kontostand:   3000.0
        >>> konto2.info()
        Kontoinhaber: Detlef
        Kontonummer:  2
        Kontostand:   2000.0
        """
        if not isinstance(geldmenge, (int, float)):
            return print("Ungültige Geldmenge!")
        elif geldmenge <= 0:
            return print("Ungültige Geldmenge!")
        elif geldmenge > self.__kontostand:
            return print("Ungültig! Geldmenge übersteigt Kontostand!")
        else:
            self.auszahlen(geldmenge)
            empfaenger_konto.einzahlen(geldmenge)
            return print("Überweisung erfolgreich!")

    def __add__(self, other):
        pass

#main    
"""
konto1 = Konto("Danilo", 1, 4000)
konto2 = Konto("Detlef", 2, 1000)

print("==== konto1 ====")
konto1.info()
print()
print("==== konto2 ====")                             
konto2.info()

print()
print("___.info: Kontoinformationen abrufen")
print("___.einzahlen(Geldmenge)")
print("___.auszahlen(Geldmenge)")
print("___.ueberweisen(Empfaengerkonto)")
"""

print(Konto.Kontonummer)
konto1 = Konto("Danilo")
konto1.info()
konto2 = Konto("Dieter")
konto2.info()


"""
if __name__ == "__main__":
    import doctest
    doctest.testmod()
"""
