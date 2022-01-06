def abrechnung(einkauf, mwst=.2):
    '''

    Diese Funktion berechnet die Gesamtsumme des EInkaufs
    inklusive Mehrwertsteuer

    :param einkauf: Liste von Preisen (list von float)
    :param mwst: Mehrwertsteuer (float)
    :return Summe inklusive MWST

    '''

    summe = 0.0
    for e in einkauf:
        summe += e
    summe *= 1. + mwst
    return summe


# Dieser kleine Test überprüft, ob wir usn in dem Hauptteil des Programms befinden,
# oder als Bibliothek verwendet werden. Im Falle der Bibliothek soll nämlich keine
# Funktion ausgeführt werden; Das wäre störend.


if __name__ == '__main__':
    print(__name__)  # das ist "file1" in der Datei "wifi.py", wenn als Library ausgeführt
    a = abrechnung([5.6, 1, 9])
    print(a)

# test
