import random as rd, time

class Konto:
    def __init__(self, kontoinhaber, kontonummer, kontostand=0.0):
        if isinstance(kontoinhaber, str) and isinstance(kontonummer, int) and isinstance(kontostand, (int, float)):
            self.__kontoinhaber = kontoinhaber
            self.__kontonummer = kontonummer
            self.__kontostand = float(kontostand)
        else:
            raise Exception

    def einzahlen(self, geldmenge):
        """
        >>> Konto1 = Konto("Hugo A.", 1234355)
        >>> Konto1.einzahlen(123)
        Die Einzahlung von 123 € war erfolgreich!
        >>> Konto1.einzahlen(1234.56)
        Die Einzahlung von 1234.56 € war erfolgreich!
        >>> Konto1.einzahlen("zehn")
        Der Betrag oder die Kontonummer ist ungültig
        >>> Konto1.einzahlen(-23)
        Der Betrag darf nicht negativ oder null sein
        >>> Konto1.einzahlen(0)
        Der Betrag darf nicht negativ oder null sein
        """
        if isinstance(geldmenge, (int, float)):
            if geldmenge > 0:
                self.__kontostand += geldmenge
                print("Die Einzahlung von",  geldmenge, "€ war erfolgreich!")
            else:
                print("Der Betrag darf nicht negativ oder null sein")
        else:
            print("Der Betrag oder die Kontonummer ist ungültig")

    def auszahlen(self, geldmenge):
        """
        >>> Konto2 = Konto("A. Schloch", 201923, 50.00)
        >>> Konto2.auszahlen(20)
        Die Auszahlung von 20 € war erfolgreich!
        >>> Konto2.auszahlen(4.99)
        Die Auszahlung von 4.99 € war erfolgreich!
        >>> Konto2.auszahlen("elf euro")
        Der Betrag oder die Kontonummer ist ungültig
        >>> Konto2.auszahlen(-2)
        Der Betrag darf nicht negativ oder null sein
        >>> Konto2.auszahlen(0)
        Der Betrag darf nicht negativ oder null sein
        >>> Konto2.auszahlen(100)
        Dieser Betrag übersteigt das Kapital des Kontos
        """
        if isinstance(geldmenge, (int, float)):
            if geldmenge > 0:
                if geldmenge < self.__kontostand:
                    self.__kontostand -= geldmenge
                    print("Die Auszahlung von", geldmenge, "€ war erfolgreich!")
                else:
                    print("Dieser Betrag übersteigt das Kapital des Kontos")
            else:
                print("Der Betrag darf nicht negativ oder null sein")
        else:
            print("Der Betrag oder die Kontonummer ist ungültig")

    def anzeigen(self):
         print("Kontoinhaber:",  self.__kontoinhaber)
         print("Kontonummer:", self.__kontonummer)
         print("Kontostand:", self.__kontostand)

    def ueberweisen(self, geldmenge, konto):
        """
        >>> Konto3 = Konto("Adolf Daßler", 4219391945666, 100.00) 
        >>> Konto3.ueberweisen(40, 12687687686)
        Die Überweisung von 40 € war erfolgreich!
        >>> Konto3.ueberweisen(2.99, 12687687686)
        Die Überweisung von 2.99 € war erfolgreich!
        >>> Konto3.ueberweisen("elf euro", 12687687686)
        Der Betrag oder die Kontonummer ist ungültig
        >>> Konto3.ueberweisen(-2, 12687687686)
        Der Betrag darf nicht negativ oder null sein
        >>> Konto3.ueberweisen(0, 12687687686)
        Der Betrag darf nicht negativ oder null sein
        >>> Konto3.ueberweisen(200, 12687687686)
        Dieser Betrag übersteigt das Kapital des Kontos
        """
        if isinstance(geldmenge, (int, float)) and isinstance(konto, int):
            if geldmenge > 0:
                if geldmenge < self.__kontostand:
                    self.__kontostand -= geldmenge
                    konto += geldmenge
                    print("Die Überweisung von", geldmenge, "€ war erfolgreich!")
                else:
                    print("Dieser Betrag übersteigt das Kapital des Kontos")
            else:
                print("Der Betrag darf nicht negativ oder null sein")
        else:
            print("Der Betrag oder die Kontonummer ist ungültig")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
