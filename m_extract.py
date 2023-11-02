# Externer Modul: Einfache Text-Extrahieren aus PDf-Dateien.
from PyPDF2 import PdfReader


def text_extraction(path_pdf, page_num):
    print("Text aus Pdf wird extrahiert...")
    try:
        seitenzahl_pdf = int(page_num) - 1
        text = PdfReader(path_pdf).pages[seitenzahl_pdf].extract_text().split()
        return text
    except FileNotFoundError:
        input("Anscheinend stimmt was mit dem Pfad nicht: ")
