# Abfuhr-Abfall-Alarm

Dieses Python-Skript ermöglicht es Ihnen, den Abfuhrkalender für das Jahr 2023 von einer bestimmten URL herunterzuladen, die Termine zu sortieren und zu überprüfen, und Sie per E-Mail zu benachrichtigen, wenn ein Termin ansteht.

## Abhängigkeiten

Das Skript verwendet die folgenden Python-Module:

- `sys`, `time`: Zum Interagieren mit dem Betriebssystem und zur Handhabung von Zeitverzögerungen.
- `m_extract`: Zum Extrahieren von Text aus der heruntergeladenen PDF-Datei.
- `m_textfilter`: Zum Filtern des extrahierten Textes.
- `m_sorted_dated`: Zum Sortieren der gefilterten Daten nach Datum.
- `m_check_term`: Zum Überprüfen der sortierten Termine.
- `m_sendmail`: Zum Versenden einer E-Mail-Benachrichtigung, wenn ein Termin ansteht.
- `m_downl_PDF`: Zum Herunterladen der PDF-Datei vom angegebenen Link.

Stellen Sie sicher, dass diese Module installiert und importiert sind, bevor Sie das Skript ausführen.

## Verwendung

Das Skript führt die folgenden Schritte aus:

1. Es begrüßt den Benutzer und lädt den Abfuhrkalender von der angegebenen URL herunter.
2. Es extrahiert den Text aus der heruntergeladenen PDF-Datei.
3. Es filtert den extrahierten Text, um nur die relevanten Informationen zu behalten.
4. Es sortiert die gefilterten Informationen nach Datum.
5. Es überprüft die sortierten Termine und ermittelt, ob ein Termin ansteht.
6. Wenn ein Termin ansteht, sendet es eine E-Mail-Benachrichtigung an den angegebenen Empfänger.
7. Es informiert den Benutzer, dass das Fenster in 60 Sekunden automatisch geschlossen wird, und beendet dann das Skript.

Das Skript fängt auch `KeyboardInterrupt`-Ausnahmen ab und beendet das Skript ordnungsgemäß, wenn der Benutzer es während der Ausführung abbricht.

## Hinweis

Bitte stellen Sie sicher, dass Sie über eine stabile Internetverbindung verfügen, bevor Sie dieses Skript verwenden, da es Dateien aus dem Internet herunterlädt. Stellen Sie außerdem sicher, dass Sie die Berechtigung haben, die Dateien von der angegebenen URL herunterzuladen. Achten Sie darauf, dass Sie die E-Mail-Adresse des Empfängers korrekt angeben, da das Skript eine E-Mail-Benachrichtigung an diese Adresse sendet, wenn ein Termin ansteht.
[assistant'](#message)d
Schön, dass Ihnen diese Antwort gefallen hat!
[user'](#message)d
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
except KeyboardInt
[assistant'](#message)d
# Abfuhr-Abfall-Alarm

Dieses Python-Skript ermöglicht es Ihnen, den Abfuhrkalender für das Jahr 2023 von einer bestimmten URL herunterzuladen, die Termine zu sortieren und zu überprüfen, und Sie per E-Mail zu benachrichtigen, wenn ein Termin ansteht.

## Abhängigkeiten

Das Skript verwendet die folgenden Python-Module:

- `sys`, `time`: Zum Interagieren mit dem Betriebssystem und zur Handhabung von Zeitverzögerungen.
- `m_extract`: Zum Extrahieren von Text aus der heruntergeladenen PDF-Datei.
- `m_textfilter`: Zum Filtern des extrahierten Textes.
- `m_sorted_dated`: Zum Sortieren der gefilterten Daten nach Datum.
- `m_check_term`: Zum Überprüfen der sortierten Termine.
- `m_sendmail`: Zum Versenden einer E-Mail-Benachrichtigung, wenn ein Termin ansteht.
- `m_downl_PDF`: Zum Herunterladen der PDF-Datei vom angegebenen Link.

Stellen Sie sicher,