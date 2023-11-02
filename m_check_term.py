# Importiere Modul zum Arbeiten mit Datum.
import datetime


# Datumsangaben
date_to_day = datetime.date.today()
tomorrow = date_to_day + datetime.timedelta(1)
tomorrow = str(tomorrow)

# Suchwörter
keywords = ["BIOMÜLL", "PAPIER", "RESTMÜLL", "GELBE", "SONDERMÜLL", "BIOMÜLL/1,1CBM", "MAIFEIERTAG", "OSTERSONNTAG",
            "OSTERMONTAG", "KARFREITAG", "1,1", "NEUJAHR", "FRONLEICHNAM"]

# Alle TErmine zur Auflistung und übersicht.
all_terms = {}


def f_check_termins(kalender):
    print("Termine werden überprüft...")
    for d in kalender:
        for date, name in d.items():
            if date == tomorrow and name in keywords:
                return ["Datum:", date, "Ereignis:", name]
            elif name in keywords and not date == "Leer":
                all_terms[date] = name
    return all_terms
