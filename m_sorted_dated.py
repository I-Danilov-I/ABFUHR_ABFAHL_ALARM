import datetime

# Aktuelles Datum
current = datetime.date.today().today()
# Aktueller Tag einzeln
today = datetime.date.today().day
# Aktueller Monat Einzeln
month = datetime.date.today().month
# Aktuelles Jahr
year = datetime.date.today().year


# Abholtermine: Fertig sortiert und mit Datum versehen.
januar = {}
februar = {}
marz = {}
april = {}
mai = {}
juni = {}


def sorting_dating(text):
    print("Termine werden sortiert und datiert...")
    for i in range(len(text)):

        # Termin und Name einzeln herausgefiltert.
        # weekday = str(text[i][0:2])
        day = int(text[i][2:4])
        name = str(text[i][4:20]).upper()

        # Index und Elemente zur Information.
        # print(f"{text[i]:20} | Index: {i}")

        # Wenn der Name kein Eintrag hat, mit Leer kennzeichnen.
        if name == "":
            name = "Leer"

        # Januar
        if i in range(0, 168, 6):
            termin = str(datetime.date(year, 1, day))
            januar[termin] = name
            # print(text[i][0:4])
        elif i in range(168, 179, 5):
            termin = str(datetime.date(year, 1, day))
            januar[termin] = name
            # print(text[i][0:4])

        # Februar
        elif i in range(1, 168, 6):
            termin = str(datetime.date(year, 2, day))
            februar[termin] = name
            # print(text[i][0:4])
        elif i in range(168, 179, 5):
            termin = str(datetime.date(year, 2, day))
            februar[termin] = name
            # print(text[i][0:4])

        # März
        elif i in range(2, 168, 6):
            termin = str(datetime.date(year, 3, day))
            marz[termin] = name
            # print(text[i][0:4])
        elif i in range(164, 180, 5):
            termin = str(datetime.date(year, 3, day))
            marz[termin] = name
            # print(text[i][0:4])

        # April
        elif i in range(3, 165, 6):
            termin = str(datetime.date(year, 4, day))
            april[termin] = name
            # print(text[i][0:4])
        elif i in range(165, 180, 5):
            termin = str(datetime.date(year, 4, day))
            april[termin] = name
            # print(text[i][0:4])

        # Mai
        elif i in range(4, 166, 6):
            termin = str(datetime.date(year, 5, day))
            mai[termin] = name
            # print(text[i][0:4])
        elif i in range(166, 176, 5):
            termin = str(datetime.date(year, 5, day))
            mai[termin] = name
            # print(text[i][0:4])
        elif i in range(176, 181, 4):
            termin = str(datetime.date(year, 5, day))
            mai[termin] = name

        # Juni
        elif i in range(5, 167, 6):
            termin = str(datetime.date(year, 6, day))
            juni[termin] = name
            # print(text[i][0:4])

        elif i in range(167, 178, 5):
            termin = str(datetime.date(year, 6, day))
            juni[termin] = name

    print("Sortierte Abholtermine als Dictionary's in einer Liste gespeichert...")
    return [januar, februar, marz, april, mai, juni]
