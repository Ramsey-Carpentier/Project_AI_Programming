import tkinter as tk
from tkinter import Toplevel, ttk, messagebox
import json
from tkinter.colorchooser import askcolor



# Open de bestellijst en voer wijzigingen uit
def open_bestellijst_window():
    # Laad de bestellijst en voorraad
    def load_json(filename):
        try:
            with open(filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    # Schrijf gegevens naar JSON-bestand
    def save_json(filename, data):
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

    def markeer_status(selected_item, status):
        if not selected_item:
            messagebox.showwarning("Selecteer item", "Selecteer een bestelling om de status bij te werken.")
            return
        item_index = tree.index(selected_item)
        bestellijst[item_index]["status"] = status
        if status == "Besteld":
            tree.item(selected_item, text="", tags=("besteld"))
        elif status == "Geannuleerd":
            tree.item(selected_item, text="", tags=("geannuleerd"))
        save_json("jsonfiles/bestellingen.json", bestellijst)

        bestel_window.destroy()
        open_bestellijst_window()

    def verwerk_binnenkomst(selected_item):
        if not selected_item:
            messagebox.showwarning("Selecteer item", "Selecteer een bestelling om te verwerken.")
            return

        item_index = tree.index(selected_item)
        binnenkomend_item = bestellijst.pop(item_index)

        # Vind de juiste categorie in de voorraad
        categorie_naam = binnenkomend_item["menu"]
        toegevoegd = False
        for categorie in voorraad["voorraadkamer"]["categorieën"]:
            if categorie["naam"] == categorie_naam:
                # Voeg item toe aan de juiste categorie
                categorie["items"].append({
                    "item": binnenkomend_item["bestelling"],
                    "hoeveelheid": str(binnenkomend_item["aantal"]),
                    "eenheid": "stuks",  # Voeg dit aan naar wens
                    "omschrijving": "Toegevoegd vanuit bestelling",  # Pas dit aan
                    "vervaldatum": "N.v.t."  # Voeg standaardwaarde toe
                })
                toegevoegd = True
                break

        if not toegevoegd:
            messagebox.showerror("Fout", f"Categorie '{categorie_naam}' niet gevonden in voorraad.")
            return

        # Sla beide JSON-bestanden op
        save_json("jsonfiles/bestellingen.json", bestellijst)
        save_json("jsonfiles/vooraad.json", voorraad)

        # Verwijder uit de boomstructuur
        tree.delete(selected_item)
        messagebox.showinfo("Succes", "Bestelling verwerkt en toegevoegd aan de voorraad.")


    def verwijder_bestelling(selected_item):
        if not selected_item:
            messagebox.showwarning("Selecteer item", "Selecteer een bestelling om te verwijderen.")
            return
        item_index = tree.index(selected_item)
        bestellijst.pop(item_index)
        save_json("jsonfiles/bestellingen.json", bestellijst)
        tree.delete(selected_item)

    bestel_window = Toplevel(window)
    bestel_window.title("Bestellijst Beheer")
    bestel_window.geometry("800x500")
    bestel_window.grab_set()

    # Laad JSON-data
    bestellijst = load_json("jsonfiles/bestellingen.json")
    voorraad = load_json("jsonfiles/vooraad.json")

    # Tabel om bestellingen weer te geven
    columns = ("dokter", "menu", "bestelling", "aantal", "status")
    tree = ttk.Treeview(bestel_window, columns=columns, show="headings")
    tree.pack(fill=tk.BOTH, expand=True)

    # Kolominstellingen
    for col in columns:
        tree.heading(col, text=col.capitalize())
        tree.column(col, width=150, anchor="center")

    # Kleurentags voor status
    tree.tag_configure("besteld", background="lightgreen")
    tree.tag_configure("geannuleerd", background="lightcoral")
    tree.tag_configure("openstaand", background="lightblue")

    # Voeg data toe aan tabel
    for item in bestellijst:
        status = item.get("status", "Openstaand")
        tree.insert("", tk.END, values=(item["dokter"], item["menu"], item["bestelling"], item["aantal"], status),
                    tags=(status.lower(),))

    # Knoppen voor interactie
    button_frame = tk.Frame(bestel_window)
    button_frame.pack(fill=tk.X, pady=10)

    tk.Button(button_frame, text="Markeer als Besteld", command=lambda: markeer_status(tree.focus(), "Besteld"),
              bg="lightgreen").pack(side=tk.LEFT, padx=5)
    tk.Button(button_frame, text="Markeer als Geannuleerd", command=lambda: markeer_status(tree.focus(), "Geannuleerd"),
              bg="lightcoral").pack(side=tk.LEFT, padx=5)
    tk.Button(button_frame, text="Verwerk Binnenkomst", command=lambda: verwerk_binnenkomst(tree.focus()),
              bg="yellow").pack(side=tk.LEFT, padx=5)
    tk.Button(button_frame, text="Verwijder Bestelling", command=lambda: verwijder_bestelling(tree.focus()),
              bg="red").pack(side=tk.LEFT, padx=5)

# Hoofdvenster
window = tk.Tk()
window.title("Voorraad- en Bestelbeheer")
window.geometry("400x200")

# Open bestelvenster knop
tk.Button(window, text="Open Bestellijst", command=open_bestellijst_window, font=("Arial", 14), bg="blue", fg="white").pack(pady=50)

# Start het hoofdvenster
window.mainloop()
