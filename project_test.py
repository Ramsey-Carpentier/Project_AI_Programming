import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
from PIL import Image, ImageTk
import json
from datetime import datetime

# Laad de afspraken uit het JSON-bestand
def load_appointments():
    try:
        with open('jsonfiles/afspraken.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Sla de afspraken op in het JSON-bestand
def save_appointments(appointments):
    with open('jsonfiles/afspraken.json', 'w') as file:
        json.dump(appointments, file, indent=4)

# Maak een afspraak
def maak_afspraak(dokter, bureau):
    # Dit is de functie die het nieuwe venster opent om een afspraak te maken
    afspraak_window = tk.Toplevel(window)
    afspraak_window.title(f"Afspraken - {dokter}")
    afspraak_window.geometry("600x500")
    
    afspraak_window.grab_set()
    # Laad de bestaande afspraken
    afspraken = load_appointments()

    # Verzeker dat de dokter al bestaat in de afspraken
    if dokter not in afspraken:
        afspraken[dokter] = []

    # Voeg tekst toe over de dokter en het bureau
    afspraak_text = f"Maak een afspraak met {dokter} van {bureau}.\n\n"
    afspraak_label = tk.Label(afspraak_window, text=afspraak_text, font=("Arial", 16))
    afspraak_label.grid(row=0, column=0, columnspan=2, pady=20)

    # Vraag om de naam van de patiënt
    patient_label = tk.Label(afspraak_window, text="Naam patiënt:", font=("Arial", 12))
    patient_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)
    patient_entry = tk.Entry(afspraak_window, font=("Arial", 12))
    patient_entry.grid(row=1, column=1, padx=10, pady=5)

    # Kies een datum voor de afspraak
    datum_label = tk.Label(afspraak_window, text="Kies een datum (YYYY-MM-DD):", font=("Arial", 12))
    datum_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)
    datum_entry = tk.Entry(afspraak_window, font=("Arial", 12))
    datum_entry.grid(row=2, column=1, padx=10, pady=5)

    # Kies een tijd voor de afspraak
    tijd_label = tk.Label(afspraak_window, text="Kies een tijd:", font=("Arial", 12))
    tijd_label.grid(row=3, column=0, sticky="w", padx=10, pady=5)

    tijden = []
    for hour in range(9, 16):
        for minute in ["00", "30"]:
            tijden.append(f"{hour}:{minute}")

    tijd_combobox = ttk.Combobox(afspraak_window, values=tijden, font=("Arial", 12))
    tijd_combobox.grid(row=3, column=1, padx=10, pady=5)

    # Vraag om de reden van de afspraak
    reden_label = tk.Label(afspraak_window, text="Reden voor de afspraak:", font=("Arial", 12))
    reden_label.grid(row=4, column=0, sticky="w", padx=10, pady=5)
    reden_entry = tk.Entry(afspraak_window, font=("Arial", 12))
    reden_entry.grid(row=4, column=1, padx=10, pady=5)

    # Voeg een knop toe om de afspraak te bevestigen
    def bevestig_afspraak():
        datum = datum_entry.get()
        tijd = tijd_combobox.get()
        patient = patient_entry.get()
        reden = reden_entry.get()

        # Controleer of er al een afspraak is op dat moment
        for afspraak in afspraken[dokter]:
            if afspraak["datum"] == datum and afspraak["tijd"] == tijd:
                messagebox.showerror("Fout", "Dit tijdslot is al bezet. Kies een ander tijdslot.")
                return

        # Voeg de afspraak toe aan de lijst
        afspraken[dokter].append({
            "patient": patient,
            "datum": datum,
            "tijd": tijd,
            "reden": reden
        })

        # Sla de nieuwe afspraken op in het bestand
        save_appointments(afspraken)
        messagebox.showinfo("Afspraak bevestigen", f"Afspraak voor {patient} op {datum} om {tijd} is bevestigd.")

        afspraak_window.destroy()

    bevestig_button = tk.Button(afspraak_window, text="Bevestig afspraak", font=("Arial", 12), command=bevestig_afspraak)
    bevestig_button.grid(row=5, column=0, columnspan=2, pady=20)

    # Zet de focus op het eerste veld
    patient_entry.focus()

def open_Bureau(kamer):
    # Maak een nieuw venster voor het bureau
    Kamer_window = tk.Toplevel(window)
    Kamer_window.title(f"{kamer} - Bureau Window")
    Kamer_window.geometry("900x500")
    Kamer_window.grab_set()

    # Maak een frame voor de indeling
    main_frame = tk.Frame(Kamer_window)
    main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    # Naam van het bureau bovenaan
    kamer_label = tk.Label(main_frame, text=f"{kamer}", font=("Arial", 22, "bold"))
    kamer_label.pack(pady=10)  # Plaats het label met wat ruimte bovenaan het frame

    # Informatie afhankelijk van de kamer
    dokter = ""
    beschikbaar = ""
    image_path = ""

    if kamer == "Bureau 101":
        dokter = "Dr. T. Terryn"
        beschikbaar = "Niet beschikbaar op Maandag en Zondag."
        image_path = "images/thibo.jpg"
    elif kamer == "Bureau 102":
        dokter = "Dr. R. Carpentier"
        beschikbaar = "Niet beschikbaar op Woensdag en Zondag."
        image_path = "images/ik.png"
    elif kamer == "Bureau 103":
        dokter = "Dr. M. Ooghe"
        beschikbaar = "Niet beschikbaar op Dinsdag en Zaterdag."
        image_path = "images/michiel.png"
    elif kamer == "Bureau 104":
        dokter = "Dr. F. Titiljon"
        beschikbaar = "Niet beschikbaar op Dinsdag en Vrijdag."
        image_path = "images/floflo.png"
    elif kamer == "Bureau 105":
        dokter = "Dr. J. De Vos"
        beschikbaar = "Niet beschikbaar op Donderdag en Zaterdag."
        image_path = "images/jos.jpg"

    # Maak een frame voor de afbeelding en tekst
    info_frame = tk.Frame(main_frame)
    info_frame.pack(side=tk.TOP, pady=20)

    # Laad de afbeelding en pas de grootte aan
    try:
        original_image = Image.open(image_path)
        resized_image = original_image.resize((150, 150))  # Verander de grootte naar wens
        userimage = ImageTk.PhotoImage(resized_image)

        # Toon de afbeelding
        img_label = tk.Label(info_frame, image=userimage)
        img_label.image = userimage  # Bewaar de referentie naar de afbeelding
        img_label.pack(side=tk.LEFT, padx=20)

    except Exception as e:
        print(f"Fout bij het laden van de afbeelding: {e}")

    # Voeg de tekstinformatie toe aan de rechterkant van de afbeelding
    text_frame = tk.Frame(info_frame)
    text_frame.pack(side=tk.LEFT, padx=20)

    # Toon de naam van de dokter en de beschikbaarheid
    dokter_label = tk.Label(text_frame, text=f"{dokter}", font=("Arial", 18, "bold"))
    dokter_label.pack(padx=10, pady=5)

    beschikbaar_label = tk.Label(text_frame, text=f"{beschikbaar}", font=("Arial", 14))
    beschikbaar_label.pack(padx=10, pady=5)

    # Voeg de knop toe om een afspraak te maken
    afspraak_button = tk.Button(Kamer_window, text="Maak een afspraak", font=("Arial", 14), command=lambda: maak_afspraak(dokter, kamer))
    afspraak_button.pack(side=tk.BOTTOM, pady=20)

# Hoofdvenster
window = tk.Tk()
window.geometry("900x500")

# Test de functie
open_Bureau("Bureau 101")
window.mainloop()
