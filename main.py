# _____________________________________________________[ Importe ]_____________________________________________________
# Module: zum Interagieren mir dem OS.
import sys

# Modul: zum Interagieren mit der Zeit.
import time

# Modul: Text extrahieren.
import m_extract

# Modul: Text Filtern aus PDF-Datei.
import m_textfilter

# Modul: Text Sortierung
import m_sorted_dated

# Modul: Termine überprüfen
import m_check_term

# Modul: Mail versenden.
import m_sendmail

# Modul: Mail versenden.
import m_downl_PDF

# _______________________________________[ Variablen und Steuerung ]__________________________________________________
# Downloadlink zum Abfuhrkalender.
url = "https://www.hallo-minden.de/data-minden/minden/abfallkalender/abfallkalender_hille_2023.pdf"

# Pfad zum heruntergeladenen Anfuhrkalender.
pfad = "abfallkalender.pdf"

# Seite die ausgelesen werden soll.
seitenzahl = 7

# Daten zum Versenden eine E-Mail.
absender = "ABFUHR-ALARM <danilov.a@gmx.net>"
empfanger = "danilov.a@gmx.net"
betreffzeile = "Ein Termin steht morgen an!"
nachricht = "Ein wunderschönen guten Tag! \n" \
            "Bitte vergessen sie nicht die Tonne rauszustellen"

# __________________________________[ Funktionsaufrufe aus den importierten Modulen ]_____________________________
try:
    print("___________________________[ Willkommen zum Abfuhr-Abfall-Alarm ]___________________________\n")
    m_downl_PDF.download(url)

    print("\n--- Funktionsaufruf: Text Extrahieren ---")
    extract_text = m_extract.text_extraction(pfad, seitenzahl)
    # print(f"Extrahiert: {type(extract_text)} \nAnzahl Elemente: {len(extract_text)} \n{extract_text}\n")

    print("\n--- Funktionsaufruf: Text Filtern ---")
    text_filtered = m_textfilter.presort(extract_text)
    # print(f"Gefiltert: {type(text_filtered)} \nAnzahl Elemente: {len(extract_text)} \n{text_filtered}\n")

    print("\n--- Funktionsaufruf: Text Sortieren ---")
    KALENDER = m_sorted_dated.sorting_dating(text_filtered)
    # print(f"JANUAR: {type(KALENDER[0])} \nAnzahl Elemente: {len(KALENDER[0])} \n{KALENDER[0]}\n")
    # print(f"FEBRUAR: {type(KALENDER[1])} \nAnzahl Elemente: {len(KALENDER[1])} \n{KALENDER[1]}\n")
    # print(f"MÄRZ: {type(KALENDER[2])} \nAnzahl Elemente: {len(KALENDER[2])} \n{KALENDER[2]}\n")
    # print(f"April: {type(KALENDER[3])} \nAnzahl Elemente: {len(KALENDER[3])} \n{KALENDER[3]}\n")
    # print(f"Mai: {type(KALENDER[4])} \nAnzahl Elemente: {len(KALENDER[4])} \n{KALENDER[4]}\n")
    # print(f"Juni: {type(KALENDER[5])} \nAnzahl Elemente: {len(KALENDER[5])} \n{KALENDER[5]}\n")

    print("\n--- Funktionsaufruf: Check Termine ---")
    meldung = m_check_term.f_check_termins(KALENDER)

    # __________________________________________________[ Hauptprogramm ]_____________________________________________

    # Wenn Rückgabe aus meldung mehr als 5 Elem. hat stehen keine Termine an, es werden dann alle Termine aufgelistet.
    if len(meldung) > 10:
        print("Ausgabe...")
        print("\n[__Alle Termine für diese Jahr__]\n")
        for k, v in m_check_term.all_terms.items():
            print(f"|  {k:10} : {v:14}  |")
        print(" ")

        print("Für morgen stehen keine Abholtermine Termine an!")
        print("_" * 50)

    # Wenn Termin ansteht, wird E-Mail wird mit dem zutreffen Termin versendet, es folgt keine auflistung aller Termine.
    else:
        print("\n--- Funktionsaufruf: E-Mail versenden ---")
        m_sendmail.SendeEmail(send_from=absender,
                              send_to=empfanger,
                              headline=f"{betreffzeile}",
                              message=f"{nachricht} : {meldung}", )

    # Damit sich das Fenster in CMD nicht sofort schließt.
    print("Fenster wird in 60 Sec. automatisch geschlossen.")
    for i in range(-60, 1):
        time.sleep(1)
    sys.exit("Programm Ende.")

# _______________________________________________________[ ENDE ]______________________________________________________
except KeyboardInterrupt:
    sys.exit("Beendet durch benutzen.")
