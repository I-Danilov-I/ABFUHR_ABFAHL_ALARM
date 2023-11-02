# Modul zum Interagieren mit Webseiten.
import requests


def download(link):
    print("\n--- Funktionsaufruf: Download ---")
    # Der oben gezeigte Code wird das Favicon (Bild) von STANDARD_URL herunterladen und Speichern
    print("Der Aktuelle Kalender wird von der Offiziellen Seite der Gemeinde heruntergeladen...")
    print(f"{link}")
    webseite = requests.get(link)

    if webseite.status_code == 200:
        print("Download der PDF gestartet..")
        # Öffne Datei Stun. und speicher den Konten Speichern webseite
        open("abfallkalender.pdf", "wb").write(webseite.content)
        print("Download abgeschlossen!")

    elif webseite.status_code == 404:
        print("Webseite nicht erreichbar!")
        input("___:")

    else:
        print("Unbekannter Fehler.")
        input("___:")
