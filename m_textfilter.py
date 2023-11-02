
def presort(text):
    print("Text wird gefiltert...")
    wanted = ("Mo", "Di", "Mi", "Do", "Fr", "Sa", "So")
    special_terms = ["Sollte", "Sondermüll", "Sammeltermine"]
    deleted = []
    for wort in list(text):
        if wort in special_terms:
            deleted.append(wort)
            text.remove(wort)
        elif wort.startswith(wanted):
            pass
        else:
            deleted.append(wort)
            text.remove(wort)
    print("Ausgabe des gefilterten textes...")
    return text
