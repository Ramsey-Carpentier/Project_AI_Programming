import tkinter as tk
import json
from tkinter import Tk, ttk, Button, Label, Toplevel, simpledialog, Text, Entry, Scrollbar, messagebox, StringVar, VERTICAL, RIGHT, Y, END
from PIL import Image, ImageTk
from datetime import datetime
import cv2

class CameraApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Camera Feed with Detection")
        
        # Label for the video feed
        self.video_label = Label(master)
        self.video_label.pack()

        # Start the camera
        self.vid = cv2.VideoCapture(0)

        # Load the Haar Cascade for face detection
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        # Start the video loop
        self.update()

    def update(self):
        # Read a frame from the camera
        ret, frame = self.vid.read()
        if ret:
            # Convert the frame to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect faces in the frame
            faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

            # Draw a rectangle around each face
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Convert the frame to RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Convert the frame to an image
            img = Image.fromarray(frame)
            img_tk = ImageTk.PhotoImage(image=img)

            # Update the label with the new image
            self.video_label.imgtk = img_tk
            self.video_label.configure(image=img_tk)

        # Call this function again after 10 ms
        self.master.after(10, self.update)

    def __del__(self):
        # Close the camera when the window is closed
        if self.vid.isOpened():
            self.vid.release()

def teken_ziekenhuis():
    # Clear any existing content on the canvas
    canvas.delete("all")
    
    # Draw main hospital layout
    canvas.create_oval(350, 350, 650, 650, fill="lightgray", outline="lightgray")
    canvas.create_rectangle(150, 300, 800, 500, fill="lightgray", outline="lightgray")
    canvas.create_rectangle(50, 200, 250, 600, fill="lightgray", outline="lightgray")
    rect = canvas.create_rectangle(650, 200, 1050, 400, fill="lightblue", outline="lightgray")
    
    # Add text label for Vleugel A
    canvas.create_text(820, 300, text="Vleugel A", font=("Arial", 16, "bold"))
    
    # Bind events for hover and click on Vleugel A
    canvas.tag_bind(rect, "<Enter>", on_hover)
    canvas.tag_bind(rect, "<Leave>", on_leave)
    canvas.tag_bind(rect, "<Button-1>", toon_gedetailleerde_kaart)

def on_hover(event):
    canvas.config(cursor="hand2")

def on_leave(event):
    canvas.config(cursor="")

def toon_gedetailleerde_kaart(event):
    canvas.delete("all")
    canvas.create_text(500, 100, text="Vleugel A", font=("Arial", 25, "bold"))
    canvas.create_text(110, 237, text="Plategrond", font=("Arial", 18))

    # Teken elke kamer expliciet (nu met witte achtergrond en kamernaam)
    # Top row
    evnt1 = canvas.create_rectangle(50, 250, 200, 330, outline="black", fill="white")  # Bureau 101
    canvas.create_text(125, 290, text="Bureau 101", font=("Arial", 10))

    evnt2 = canvas.create_rectangle(200, 250, 350, 330, outline="black", fill="white")  # Bureau 102
    canvas.create_text(275, 290, text="Bureau 102", font=("Arial", 10))

    evnt3 = canvas.create_rectangle(350, 250, 500, 330, outline="black", fill="white")  # Bureau 103
    canvas.create_text(425, 290, text="Bureau 103", font=("Arial", 10))

    evnt4 = canvas.create_rectangle(500, 250, 650, 330, outline="black", fill="white")  # Kamer 101
    canvas.create_text(575, 290, text="Kamer 101", font=("Arial", 10))

    evnt5 = canvas.create_rectangle(650, 250, 800, 330, outline="black", fill="white")  # Kamer 102
    canvas.create_text(725, 290, text="Kamer 102", font=("Arial", 10))

    evnt6 = canvas.create_rectangle(800, 250, 950, 370, outline="black", fill="white")  # Operatiezaal 101
    canvas.create_text(875, 310, text="Operatiezaal 101", font=("Arial", 10))

    # Middle row
    evnt7 = canvas.create_rectangle(50, 370, 200, 450, outline="black", fill="white")  # Onthaal
    canvas.create_text(125, 410, text="Onthaal", font=("Arial", 10))

    evnt8 = canvas.create_rectangle(200, 370, 350, 450, outline="black", fill="white")  # Kleedkamer
    canvas.create_text(275, 410, text="Kleedkamer", font=("Arial", 10))

    evnt9 = canvas.create_rectangle(50, 450, 350, 570, outline="black", fill="white")  # Operatiezaal 102
    canvas.create_text(200, 510, text="Operatiezaal 102", font=("Arial", 10))

    evnt10 = canvas.create_rectangle(350, 370, 700, 530, outline="black", fill="white")  # Wachtzaal (dashed)
    canvas.create_text(525, 450, text="Wachtzaal", font=("Arial", 10))

    evnt11 = canvas.create_rectangle(700, 370, 950, 530, outline="black", fill="white")  # Voorraadkamer
    canvas.create_text(825, 450, text="Voorraadkamer", font=("Arial", 10))

    # Bottom row
    evnt12 = canvas.create_rectangle(50, 570, 200, 650, outline="black", fill="white")  # Bureau 104
    canvas.create_text(125, 610, text="Bureau 104", font=("Arial", 10))

    evnt13 = canvas.create_rectangle(200, 570, 350, 650, outline="black", fill="white")  # Bureau 105
    canvas.create_text(275, 610, text="Bureau 105", font=("Arial", 10))

    evnt14 = canvas.create_rectangle(350, 570, 450, 650, outline="black", fill="white")  # Kamer 103
    canvas.create_text(400, 610, text="Kamer 103", font=("Arial", 10))

    evnt15 = canvas.create_rectangle(450, 570, 550, 650, outline="black", fill="white")  # Kamer 104
    canvas.create_text(500, 610, text="Kamer 104", font=("Arial", 10))

    evnt16 = canvas.create_rectangle(550, 570, 650, 650, outline="black", fill="white")  # Kamer 105
    canvas.create_text(600, 610, text="Kamer 105", font=("Arial", 10))

    evnt17 = canvas.create_rectangle(650, 570, 750, 650, outline="black", fill="white")  # Kamer 106
    canvas.create_text(700, 610, text="Kamer 106", font=("Arial", 10))

    evnt18 = canvas.create_rectangle(750, 570, 850, 650, outline="black", fill="white")  # Kamer 107
    canvas.create_text(800, 610, text="Kamer 107", font=("Arial", 10))

    evnt19 = canvas.create_rectangle(850, 530, 950, 650, outline="black", fill="white")  # Kamer 108
    canvas.create_text(900, 590, text="Kamer 108", font=("Arial", 10))

    # Add 'Hangen' areas in white
    canvas.create_rectangle(50, 330, 800, 370, fill="white", outline="black")  # Hangen 1

    canvas.create_rectangle(150, 530, 850, 570, fill="white", outline="black")  # Hangen 2

    # Teken een rechtse pijl als voorbeeld
    canvas.create_line(20, 350, 40, 350, arrow=tk.LAST, width=2)

    #Voeg events toe
    canvas.tag_bind(evnt1, "<Button-1>", lambda e: open_Bureau("Bureau 101"))
    canvas.tag_bind(evnt2, "<Button-1>", lambda e: open_Bureau("Bureau 102"))
    canvas.tag_bind(evnt3, "<Button-1>", lambda e: open_Bureau("Bureau 103"))
    canvas.tag_bind(evnt12, "<Button-1>", lambda e: open_Bureau("Bureau 104"))
    canvas.tag_bind(evnt13, "<Button-1>", lambda e: open_Bureau("Bureau 105"))

    canvas.tag_bind(evnt4, "<Button-1>", lambda e: open_Kamer("Kamer 101"))
    canvas.tag_bind(evnt5, "<Button-1>", lambda e: open_Kamer("Kamer 102"))
    canvas.tag_bind(evnt14, "<Button-1>", lambda e: open_Kamer("Kamer 103"))
    canvas.tag_bind(evnt15, "<Button-1>", lambda e: open_Kamer("Kamer 104"))
    canvas.tag_bind(evnt16, "<Button-1>", lambda e: open_Kamer("Kamer 105"))
    canvas.tag_bind(evnt17, "<Button-1>", lambda e: open_Kamer("Kamer 106"))
    canvas.tag_bind(evnt18, "<Button-1>", lambda e: open_Kamer("Kamer 107"))
    canvas.tag_bind(evnt19, "<Button-1>", lambda e: open_Kamer("Kamer 108"))

    canvas.tag_bind(evnt6, "<Button-1>", lambda e: open_Operatiezaal1())
    canvas.tag_bind(evnt9, "<Button-1>", lambda e: open_Operatiezaal2())
    canvas.tag_bind(evnt10, "<Button-1>", lambda e: open_wachtzaal(e, "Wachtzaal"))
    canvas.tag_bind(evnt11, "<Button-1>", lambda e: open_vooraadkamer(e, "Voorraadkamer"))

    global back_button
    back_button = tk.Button(window, text="↩︎", font=("Arial", 25), command=terug_naar_ziekenhuis,
                            bg="lightblue", fg="black")
    back_button.place(x=50, y=50)

    # Functie voor de toolbar (als dat nodig is)
    teken_Toolbalk()

def terug_naar_ziekenhuis():
    back_button.destroy()
    teken_ziekenhuis()

def teken_Toolbalk():
    # Tekent het rechthoek
    canvas.create_rectangle(50, 700, 950, 801, fill="white", outline="black")
    canvas.create_text(91, 687, text="Toolbalk", font=("Arial", 18))

    # Patient
    user_image_path = "images/patient.png"
    original_image = Image.open(user_image_path)
    resized_image = original_image.resize((99, 80)) 
    userimage = ImageTk.PhotoImage(resized_image)
    userimage_button = Button(window, image=userimage, command=open_user_window, borderwidth=0)
    userimage_button.image = userimage
    canvas.create_window(600, 742, window=userimage_button)  
    user_label = Label(window, text="Patiënten", font=("Arial", 10, "bold"), bg="white")
    canvas.create_window(600, 789, window=user_label)  

    # patient toevoegen
    user_add_image_path = "images/patient_toevoegen.png"
    original_image = Image.open(user_add_image_path)
    resized_image = original_image.resize((99, 80)) 
    useraddimage = ImageTk.PhotoImage(resized_image)
    useraddimage_button = Button(window, image=useraddimage, command=open_user_add_window, borderwidth=0)
    useraddimage_button.image = useraddimage
    canvas.create_window(700, 742, window=useraddimage_button)
    useradd_label = Label(window, text="Add Patiënten", font=("Arial", 10, "bold"), bg="white")
    canvas.create_window(700, 789, window=useradd_label)

    # dokter
    dokter_image_path = "images/dokter.png"
    original_image = Image.open(dokter_image_path)
    resized_image = original_image.resize((99, 80))
    dokterimage = ImageTk.PhotoImage(resized_image)
    dokterimage_button = Button(window, image=dokterimage, command=open_dokter_window, borderwidth=0)
    dokterimage_button.image = dokterimage
    canvas.create_window(500, 742, window=dokterimage_button) 
    dokter_label = Label(window, text="Dokters", font=("Arial", 10, "bold"), bg="white")
    canvas.create_window(500, 789, window=dokter_label)

    # bestellen
    bestel_image_path = "images/bestelling.png"
    original_image = Image.open(bestel_image_path)
    resized_image = original_image.resize((99, 80))
    bestelimage = ImageTk.PhotoImage(resized_image)
    bestelimage_button = Button(window, image=bestelimage, command=open_bestel_window, borderwidth=0)
    bestelimage_button .image = bestelimage
    canvas.create_window(300, 742, window=bestelimage_button ) 
    bestel_label = Label(window, text="Bestellen", font=("Arial", 10, "bold"), bg="white")
    canvas.create_window(300, 789, window=bestel_label)

    #bestellijst
    bestel_image_path = "images/bestellijst.png"
    original_image = Image.open(bestel_image_path)
    resized_image = original_image.resize((99, 80))
    bestelimage = ImageTk.PhotoImage(resized_image)
    bestelimage_button = Button(window, image=bestelimage, command=open_bestellijst_window, borderwidth=0)
    bestelimage_button .image = bestelimage
    canvas.create_window(400, 742, window=bestelimage_button ) 
    bestel_label = Label(window, text="Bestellijst", font=("Arial", 10, "bold"), bg="white")
    canvas.create_window(400, 789, window=bestel_label)

    #Kamers
    kamer_image_path = "images/Kamer.png"
    original_image = Image.open(kamer_image_path)
    resized_image = original_image.resize((99, 80))
    kamerimage = ImageTk.PhotoImage(resized_image)
    kamerimage_button = Button(window, image=kamerimage, command=open_kamer_window, borderwidth=0)
    kamerimage_button .image = kamerimage
    canvas.create_window(800, 742, window=kamerimage_button ) 
    kamer_label = Label(window, text="Kamers", font=("Arial", 10, "bold"), bg="white")
    canvas.create_window(800, 789, window=kamer_label)

def lees_json_bestand(bestandsnaam):
    try:
        with open(bestandsnaam, 'r', encoding='utf-8') as bestand:
            data = json.load(bestand)
            print(data)  # Debug: print de geladen JSON om de structuur te zien
        return data
    except FileNotFoundError:
        print(f"Fout: Het bestand '{bestandsnaam}' is niet gevonden.")
        return {}
    except json.JSONDecodeError:
        print(f"Fout: Het bestand '{bestandsnaam}' kan niet worden gedecodeerd.")
        return {}

def open_vooraadkamer(event, kamer):
    # Laad de gegevens van de voorraadkamer uit een bestand
    data = lees_json_bestand('jsonfiles/vooraad.json')

    if kamer == "Voorraadkamer":
        # Nieuw venster openen met gedetailleerde informatie over de Voorraadkamer
        voorraad_window = tk.Toplevel(window)
        voorraad_window.title("Informatie over Voorraadkamer")
        voorraad_window.geometry("1200x600")  # Stel het venster in op 1200px breed en 600px hoog

        # Voeg labels toe voor de algemene informatie van de voorraadkamer
        info_label = tk.Label(voorraad_window, text="De Voorraadkamer bevat medische materialen en apparatuur.", font=("Arial", 12))
        info_label.pack(pady=10)

        voorbeeld_label = tk.Label(voorraad_window, text="In deze kamer worden de voorraden beheerd en opgeslagen.", font=("Arial", 12))
        voorbeeld_label.pack(pady=10)

        # Functie om categorieën en items te tonen in een raster
        def toon_categorieen(parent, categorieen):
            # Maak een frame waarin de categorieën naast elkaar komen te staan
            grid_frame = tk.Frame(parent)
            grid_frame.pack(pady=10, fill="both", expand=True)
            
            # Configureer de kolommen om zich gelijkmatig over de breedte te verdelen
            grid_frame.grid_columnconfigure(0, weight=1, minsize=200)  # Zorg ervoor dat kolommen goed worden verdeeld
            grid_frame.grid_columnconfigure(1, weight=1, minsize=200)
            grid_frame.grid_columnconfigure(2, weight=1, minsize=200)
            grid_frame.grid_columnconfigure(3, weight=1, minsize=200)

            row = 0  # Begin bij de eerste rij
            col = 0  # Begin bij de eerste kolom

            # Loop door de categorieën en toon ze in de grid
            for index, categorie in enumerate(categorieen):
                # Maak een "tree" structuur voor de categorie en items
                cat_item = ttk.Treeview(grid_frame)
                cat_item.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

                # Voeg de naam van de categorie als een root-item toe en zet open=False om standaard in te klappen
                cat_item.insert('', 'end', categorie['naam'], text=categorie['naam'], open=False)

                # Voeg elk item binnen deze categorie toe
                for item in categorie['items']:
                    item_text = f"{item['item']} - {item['hoeveelheid']} {item['eenheid']}"
                    cat_item.insert(categorie['naam'], 'end', item['item'], text=item_text, open=False)  # Standaard ingeklapt

                # Zet de tree items in een collapsible structuur
                cat_item.bind('<Double-1>', lambda e, item=cat_item: toggle_item(e, item))

                # Update de rij- en kolomindex voor de grid
                col += 1
                if col > 3:  # Plaats maximaal 4 categorieën per rij
                    col = 0
                    row += 1

        # Functie om sub-items in of uit te klappen bij dubbelklikken
        def toggle_item(event, item):
            if item.item(item.selection()[0], "open"):
                item.item(item.selection()[0], open=False)  # Sub-item inklappen
            else:
                item.item(item.selection()[0], open=True)  # Sub-item uitklappen

        # Controleer of de sleutel 'categorieën' bestaat in de geladen data
        if 'categorieën' in data.get('voorraadkamer', {}):
            # Toon de categorieën en items in de voorraadkamer
            toon_categorieen(voorraad_window, data['voorraadkamer']['categorieën'])
        else:
            # Foutmelding als de sleutel 'categorieën' niet aanwezig is
            error_label = tk.Label(voorraad_window, text="Er zijn geen categorieën beschikbaar.", font=("Arial", 12))
            error_label.pack(pady=10)

        # Een knop om het venster te sluiten
        close_button = tk.Button(voorraad_window, text="Sluiten", command=voorraad_window.destroy)
        close_button.pack(pady=10)

def open_wachtzaal(event, kamer):
    if kamer == "Wachtzaal":
        # Open a new window for the Wachtzaal camera feed
        wachtzaal_window = tk.Toplevel(window)
        wachtzaal_window.title("Wachtzaal Camera")
        wachtzaal_window.geometry("800x600")  # Set window size

        # Initialize the CameraApp inside this new window
        camera_app = CameraApp(wachtzaal_window) 

def open_user_add_window():
    user_add_window = Toplevel(window)
    user_add_window.title("User Add Window")
    user_add_window.geometry("800x400")
    user_add_window.grab_set()
    
    def save_patient():
        # Verzamel de gegevens
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        geboortedatum = geboortedatum_entry.get()
        geslacht = geslacht_var.get()

        # Adres samenstellen uit vier velden
        straat = straat_entry.get()
        nummer = nummer_entry.get()
        postcode = postcode_entry.get()
        stad = stad_entry.get()
        adres = f"{straat} {nummer}, {postcode} {stad}"

        operaties = "geen"

        # Maak de naam samen
        naam = first_name + " " + last_name

        # Voeg de patiënt toe aan de lijst en sla deze op in het JSON-bestand
        new_patient = {
            "naam": naam,
            "GeboorteDatum": geboortedatum,
            "geslacht": geslacht,
            "adres": adres,
            "vorige_operaties": operaties
        }

        # Laad het bestaande bestand en voeg de nieuwe patiënt toe
        try:
            # Zorg ervoor dat het pad naar het bestand correct is (en dat er geen fout optreedt bij het laden)
            with open("jsonfiles/patienten.json", "r") as file:
                data = json.load(file)
            
            # Voeg de nieuwe patiënt toe aan de lijst van patiënten
            data["patienten"].append(new_patient)

            # Schrijf de bijgewerkte gegevens terug naar het bestand
            with open("jsonfiles/patienten.json", "w") as file:
                json.dump(data, file, indent=4)
                messagebox.showinfo("Bevestiging", "De patiëntgegevens zijn succesvol opgeslagen!")

        except FileNotFoundError:
            # Als het bestand niet bestaat, maak dan een nieuw bestand met de nieuwe patiënt
            #with open("jsonfiles/patienten.json", "w") as file:
             #   json.dump({"patienten": [new_patient]}, file, indent=4)
              #  messagebox.showinfo("Bevestiging", "De patiëntgegevens zijn succesvol opgeslagen!")
            print("loser")

        user_add_window.destroy()  


    # Naam en voornaam invoeren
    Label(user_add_window, text="Voornaam:", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=10, pady=10, sticky="w")
    first_name_entry = Entry(user_add_window, font=("Arial", 10), width=30)
    first_name_entry.grid(row=0, column=1, padx=10, pady=10)

    Label(user_add_window, text="Achternaam:", font=("Arial", 12, "bold")).grid(row=1, column=0, padx=10, pady=10, sticky="w")
    last_name_entry = Entry(user_add_window, font=("Arial", 10), width=30)
    last_name_entry.grid(row=1, column=1, padx=10, pady=10)

    # Geboortedatum invoeren
    Label(user_add_window, text="Geboortedatum (dd-mm-jjjj):", font=("Arial", 12, "bold")).grid(row=2, column=0, padx=10, pady=10, sticky="w")
    geboortedatum_entry = Entry(user_add_window, font=("Arial", 10), width=30)
    geboortedatum_entry.grid(row=2, column=1, padx=10, pady=10)

    # Geslacht invoeren
    Label(user_add_window, text="Geslacht:", font=("Arial", 12, "bold")).grid(row=3, column=0, padx=10, pady=10, sticky="w")

    geslacht_var = tk.StringVar()  # Create a StringVar for storing the selected value
    geslacht_combo = ttk.Combobox(user_add_window, width=27, textvariable=geslacht_var)
    geslacht_combo['values'] = ('Man', 'Vrouw', 'Anders')  # Values in the combobox
    geslacht_combo.grid(row=3, column=1, padx=10, pady=10)
    geslacht_combo.current(None)  # Set default value to "Man"

    # Adres invoeren in vier velden
    Label(user_add_window, text="Adres:", font=("Arial", 12, "bold")).grid(row=4, column=0, padx=10, pady=10, sticky="w")

    # Straatnaam invoeren
    Label(user_add_window, text="Straatnaam:", font=("Arial", 12)).grid(row=5, column=0, padx=10, pady=10, sticky="w")
    straat_entry = Entry(user_add_window, font=("Arial", 10), width=30)
    straat_entry.grid(row=5, column=1, padx=10, pady=10, sticky="w")

    # Huisnummer invoeren
    Label(user_add_window, text="Huisnummer:", font=("Arial", 12)).grid(row=5, column=2, padx=10, pady=10, sticky="w")
    nummer_entry = Entry(user_add_window, font=("Arial", 10), width=10)
    nummer_entry.grid(row=5, column=3, padx=10, pady=10, sticky="w")

    # Postcode invoeren
    Label(user_add_window, text="Postcode:", font=("Arial", 12)).grid(row=6, column=0, padx=10, pady=10, sticky="w")
    postcode_entry = Entry(user_add_window, font=("Arial", 10), width=10)
    postcode_entry.grid(row=6, column=1, padx=10, pady=10, sticky="w")

    # Stad invoeren
    Label(user_add_window, text="Stad:", font=("Arial", 12)).grid(row=6, column=2, padx=10, pady=10, sticky="w")
    stad_entry = Entry(user_add_window, font=("Arial", 10), width=20)
    stad_entry.grid(row=6, column=3, padx=10, pady=10, sticky="w")

    # Opslaan knop
    submit_button = Button(user_add_window, text="Opslaan", font=("Arial", 12), bg="green", fg="white", command=save_patient)
    submit_button.grid(row=7, column=1, columnspan=2, pady=20, sticky="nsew")

def open_user_window():
    user_window = Toplevel(window)
    user_window.title("User Window")
    user_window.geometry("1200x300")
    user_window.grab_set()

    tree = ttk.Treeview(user_window, columns=("Naam", "GeboorteDatum", "Geslacht", "Adres", "Vorige operaties"), show="headings")
    tree.heading("Naam", text="Naam")
    tree.heading("GeboorteDatum", text="GeboorteDatum")
    tree.heading("Geslacht", text="Geslacht")
    tree.heading("Adres", text="Adres")
    tree.heading("Vorige operaties", text="Vorige operaties")

    scrollbar = ttk.Scrollbar(user_window, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    tree.pack(side="left", expand=True, fill="both")
    scrollbar.pack(side="right", fill="y")

    try:
        with open("jsonfiles/patienten.json", "r") as file:
            data = json.load(file)

        if "patienten" in data:
            for patient in data["patienten"]:
                naam = patient["naam"]
                GeboorteDatum = patient["GeboorteDatum"]
                geslacht = patient["geslacht"]
                adres = patient["adres"]
                vorige_operaties = patient["vorige_operaties"]
                tree.insert("", "end", values=(naam, GeboorteDatum, geslacht, adres, vorige_operaties))
        else:
            print("Geen patiënten gevonden in het JSON-bestand!")

    except FileNotFoundError:
        print("Het JSON-bestand is niet gevonden. Controleer het pad.")
    except json.JSONDecodeError:
        print("Fout bij het decoderen van het JSON-bestand. Controleer de syntax.")
    except Exception as e:
        print(f"Een onverwachte fout is opgetreden: {e}")

def open_dokter_window():
    dokter_window = Toplevel(window)
    dokter_window.title("dokter Window")
    dokter_window.geometry("900x300")
    dokter_window.grab_set()
    tree = ttk.Treeview(dokter_window, columns=("Naam", "Leeftijd", "Specialisaties", "Bureau"), show="headings")

    # Definieer de kolommen van de tabel
    tree.heading("Naam", text="Naam")
    tree.heading("Leeftijd", text="Leeftijd")
    tree.heading("Specialisaties", text="Specialisaties")
    tree.heading("Bureau", text="Bureau")

    # Voeg de tabel toe aan het venster
    tree.pack(expand=True, fill="both")

    # Lees het JSON-bestand in
    with open("jsonfiles/dokters.json", "r") as file:
        data = json.load(file)

    # Voeg de gegevens van elke dokter toe aan de tabel
    for dokter in data["dokters"]:
        naam = dokter["naam"]
        leeftijd = dokter["leeftijd"]
        specialisaties = ", ".join(dokter["specialisaties"])
        bureau = dokter["bureau"]
        
        # Voeg de dokterinformatie als een nieuw item in de Treeview
        tree.insert("", "end", values=(naam, leeftijd, specialisaties, bureau))

def open_Operatiezaal1():
    kalender_window = tk.Toplevel(window)
    kalender_window.title("Kalender - Operatiezaal Bezetting")
    kalender_window.geometry("900x500")

    # Frame voor kalender
    global kalender_frame
    kalender_frame = tk.Frame(kalender_window)
    kalender_frame.grid(pady=20)

    json_file2 = "jsonfiles/operatiezaal1.json"
    # Laad bestaande data of maak een nieuwe dictionary
    try:
        with open(json_file2, "r") as file:
            bezette_datums = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        bezette_datums = {}

    # Functie om een operatie toe te voegen
    def voeg_operatie_toe(datum):
        patiënt = simpledialog.askstring("Invoer", f"Naam van de patiënt voor {datum}:")
        if not patiënt:
            return
        dokter = simpledialog.askstring("Invoer", f"Naam van de dokter voor {datum}:")
        if not dokter:
            return
        operatie = simpledialog.askstring("Invoer", f"Type operatie voor {datum}:")
        if not operatie:
            return

        # Opslaan in de bezette_datums dictionary
        bezette_datums[datum] = {
            "patient": patiënt,
            "dokter": dokter,
            "operatie": operatie
        }

        # Update de JSON-bestand
        with open(json_file2, "w") as file:
            json.dump(bezette_datums, file, indent=4)

        messagebox.showinfo("Operatie toegevoegd", f"Operatie op {datum} is toegevoegd!")
        update_kalender()

    # Functie om een operatie te verwijderen
    def verwijder_operatie(datum):
        if datum in bezette_datums:
            del bezette_datums[datum]
            with open(json_file2, "w") as file:
                json.dump(bezette_datums, file, indent=4)
            messagebox.showinfo("Operatie verwijderd", f"Operatie op {datum} is verwijderd.")
            update_kalender()
        else:
            messagebox.showinfo("Geen operatie", f"Er staat geen operatie gepland op {datum}.")

    # Functie om een datum te toggelen (toevoegen of verwijderen)
    def toggle_datum(datum):
        """Schakel tussen het toevoegen of verwijderen van een operatie."""
        if datum in bezette_datums:
            bevestiging = messagebox.askyesno(
                "Verwijderen", f"Wil je de operatie op {datum} verwijderen?"
            )
            if bevestiging:
                verwijder_operatie(datum)
        else:
            voeg_operatie_toe(datum)
        update_kalender()  # Kalender opnieuw opbouwen

    # Functie om de kalender te updaten
    def update_kalender():
        """Update de kalenderweergave met operatiegegevens."""
        for widget in kalender_window.winfo_children():
            widget.destroy()  # Vernietig alle widgets in het frame
        maak_kalender()  # Bouw de kalender opnieuw op

    # Functie om de kalender voor december te maken
    def maak_kalender():
        """Maak een kalender voor december."""
        dagen_in_maand = 31
        eerste_dag = datetime(2024, 12, 1).weekday()  # Maandag=0, Zondag=6

        # Header: Dagen van de week
        dagen = ["Ma", "Di", "Wo", "Do", "Vr", "Za", "Zo"]
        for col, dag in enumerate(dagen):
            tk.Label(kalender_window, text=dag, font=("Arial", 12, "bold"), width=12, height=2).grid(row=0, column=col)

        # Datum knoppen
        row = 1
        col = eerste_dag
        for dag in range(1, dagen_in_maand + 1):
            datum = f"2024-12-{dag:02d}"
            if datum in bezette_datums:
                info = bezette_datums[datum]
                patiënt = info.get("patient", "Onbekend")
                dokter = info.get("dokter", "Onbekend")
                operatie = info.get("operatie", "Onbekend")
                tekst = f"{dag}\n{patiënt}\n{dokter}\n{operatie}"  # Voeg operatie toe
                kleur = "red"
            else:
                tekst = str(dag)
                kleur = "green"

            btn = tk.Button(
                kalender_window, text=tekst, bg=kleur, fg="white", width=12, height=4,
                command=lambda d=datum: toggle_datum(d)
            )
            btn.grid(row=row, column=col, padx=2, pady=2)

            col += 1
            if col > 6:  # Nieuwe rij na zondag
                col = 0
                row += 1

    # Maak de kalender
    maak_kalender()

def open_Operatiezaal2():
    kalender_window = tk.Toplevel(window)
    kalender_window.title("Kalender - Operatiezaal Bezetting")
    kalender_window.geometry("900x500")

    # Frame voor kalender
    global kalender_frame
    kalender_frame = tk.Frame(kalender_window)
    kalender_frame.grid(pady=20)

    json_file2 = "jsonfiles/operatiezaal2.json"
    # Laad bestaande data of maak een nieuwe dictionary
    try:
        with open(json_file2, "r") as file:
            bezette_datums = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        bezette_datums = {}

    # Functie om een operatie toe te voegen
    def voeg_operatie_toe(datum):
        patiënt = simpledialog.askstring("Invoer", f"Naam van de patiënt voor {datum}:")
        if not patiënt:
            return
        dokter = simpledialog.askstring("Invoer", f"Naam van de dokter voor {datum}:")
        if not dokter:
            return
        operatie = simpledialog.askstring("Invoer", f"Type operatie voor {datum}:")
        if not operatie:
            return

        # Opslaan in de bezette_datums dictionary
        bezette_datums[datum] = {
            "patient": patiënt,
            "dokter": dokter,
            "operatie": operatie
        }

        # Update de JSON-bestand
        with open(json_file2, "w") as file:
            json.dump(bezette_datums, file, indent=4)

        messagebox.showinfo("Operatie toegevoegd", f"Operatie op {datum} is toegevoegd!")
        update_kalender()

    # Functie om een operatie te verwijderen
    def verwijder_operatie(datum):
        if datum in bezette_datums:
            del bezette_datums[datum]
            with open(json_file2, "w") as file:
                json.dump(bezette_datums, file, indent=4)
            messagebox.showinfo("Operatie verwijderd", f"Operatie op {datum} is verwijderd.")
            update_kalender()
        else:
            messagebox.showinfo("Geen operatie", f"Er staat geen operatie gepland op {datum}.")

    # Functie om een datum te toggelen (toevoegen of verwijderen)
    def toggle_datum(datum):
        """Schakel tussen het toevoegen of verwijderen van een operatie."""
        if datum in bezette_datums:
            bevestiging = messagebox.askyesno(
                "Verwijderen", f"Wil je de operatie op {datum} verwijderen?"
            )
            if bevestiging:
                verwijder_operatie(datum)
        else:
            voeg_operatie_toe(datum)
        update_kalender()  # Kalender opnieuw opbouwen

    # Functie om de kalender te updaten
    def update_kalender():
        """Update de kalenderweergave met operatiegegevens."""
        for widget in kalender_window.winfo_children():
            widget.destroy()  # Vernietig alle widgets in het frame
        maak_kalender()  # Bouw de kalender opnieuw op

    # Functie om de kalender voor december te maken
    def maak_kalender():
        """Maak een kalender voor december."""
        dagen_in_maand = 31
        eerste_dag = datetime(2024, 12, 1).weekday()  # Maandag=0, Zondag=6

        # Header: Dagen van de week
        dagen = ["Ma", "Di", "Wo", "Do", "Vr", "Za", "Zo"]
        for col, dag in enumerate(dagen):
            tk.Label(kalender_window, text=dag, font=("Arial", 12, "bold"), width=12, height=2).grid(row=0, column=col)

        # Datum knoppen
        row = 1
        col = eerste_dag
        for dag in range(1, dagen_in_maand + 1):
            datum = f"2024-12-{dag:02d}"
            if datum in bezette_datums:
                info = bezette_datums[datum]
                patiënt = info.get("patient", "Onbekend")
                dokter = info.get("dokter", "Onbekend")
                operatie = info.get("operatie", "Onbekend")
                tekst = f"{dag}\n{patiënt}\n{dokter}\n{operatie}"  # Voeg operatie toe
                kleur = "red"
            else:
                tekst = str(dag)
                kleur = "green"

            btn = tk.Button(
                kalender_window, text=tekst, bg=kleur, fg="white", width=12, height=4,
                command=lambda d=datum: toggle_datum(d)
            )
            btn.grid(row=row, column=col, padx=2, pady=2)

            col += 1
            if col > 6:  # Nieuwe rij na zondag
                col = 0
                row += 1

    # Maak de kalender
    maak_kalender()

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
     
def open_bestel_window():
     def plaats_bestelling():
        dokter = dokter_combobox.get()
        menu = menu_combobox.get()
        bestelling = bestelling_entry.get()
        aantal = aantal_entry.get()

        # Validatie van invoer
        if not dokter or not menu or not bestelling or not aantal:
            messagebox.showwarning("Incompleet", "Vul alle velden in voordat u bestelt.")
            return

        if not aantal.isdigit() or int(aantal) <= 0:
            messagebox.showerror("Ongeldig aantal", "Voer een geldig aantal in (positief geheel getal).")
            return

        # Bestelling opslaan in JSON
        nieuwe_bestelling = {
            "dokter": dokter,
            "menu": menu,
            "bestelling": bestelling,
            "aantal": int(aantal)
        }

        try:
            with open("jsonfiles/bestellingen.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []

        data.append(nieuwe_bestelling)

        with open("jsonfiles/bestellingen.json", "w") as f:
            json.dump(data, f, indent=4)

        messagebox.showinfo("Succes", "De bestelling is geplaatst!")
        bestel_window.destroy()

     # Creëer een nieuw venster
     bestel_window = Toplevel(window)
     bestel_window.title("Bestel Window")
     bestel_window.geometry("600x500")
     bestel_window.grab_set()

     # Dokters (hardcoded in de GUI)
     dokters = [
         "Michiel Ooghe (Bureau 101)",
         "Thibo Terryn (Bureau 102)",
         "Ramsey Carpentier (Bureau 103)",
         "Florian Titiljon (Bureau 104)",
         "Jos de Vos (Bureau 105)"
     ]

     # Menus (hardcoded in de GUI)
     menus = [
         "Medicatie",
         "Kleding",
         "Materiaal",
         "Farmaceutische producten",
         "Diagnostische apparatuur",
         "Schoonmaakmateriaal",
         "Overig"
     ]

     # Label en combobox voor dokter
     tk.Label(bestel_window, text="Selecteer een dokter:", font=("Arial", 14)).pack(pady=10)
     dokter_combobox = ttk.Combobox(bestel_window, values=dokters, state="readonly", font=("Arial", 12))
     dokter_combobox.pack(pady=5, fill=tk.X, padx=20)

     # Label en combobox voor menu
     tk.Label(bestel_window, text="Selecteer een menu:", font=("Arial", 14)).pack(pady=10)
     menu_combobox = ttk.Combobox(bestel_window, values=menus, state="readonly", font=("Arial", 12))
     menu_combobox.pack(pady=5, fill=tk.X, padx=20)

     # Invoerveld voor bestelling
     tk.Label(bestel_window, text="Voer de bestelling in:", font=("Arial", 14)).pack(pady=10)
     bestelling_entry = tk.Entry(bestel_window, font=("Arial", 12))
     bestelling_entry.pack(pady=5, fill=tk.X, padx=20)

     # Invoerveld voor aantal
     tk.Label(bestel_window, text="Voer het aantal in:", font=("Arial", 14)).pack(pady=10)
     aantal_entry = tk.Entry(bestel_window, font=("Arial", 12))
     aantal_entry.pack(pady=5, fill=tk.X, padx=20)

     # Plaats bestelling knop
     tk.Button(bestel_window, text="Plaats Bestelling", command=plaats_bestelling, font=("Arial", 14), bg="green", fg="white").pack(pady=20)

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

def maak_afspraak(dokter, bureau):
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

def open_kamer_window():
    def voeg_bezetting_toe():
        print("Function aangeroepen")
        kamer = kamer_combobox.get()
        dokter = dokter_combobox.get()
        patient = patient_combobox.get()  # Naam geselecteerd uit de combobox
        datum = datum_entry.get()
        reden = reden_entry.get()

        # Validatie van invoer
        if not kamer or not dokter or not patient or not datum or not reden:
            messagebox.showwarning("Incompleet", "Vul alle velden in voordat u een bezetting toevoegt.")
            return

        nieuwe_bezetting = {
            "patient": patient,
            "dokter": dokter,
            "datum": datum,
            "waarom": reden
        }

        try:
            with open("jsonfiles/kamers.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {"Kamers": {"categorieën": []}}

        # Zoek de juiste kamer
        for kamer_data in data["Kamers"]["categorieen"]:
            if kamer_data["naam"] == kamer:
                kamer_data["bezetingen"].append(nieuwe_bezetting)
                break
        else:
            messagebox.showerror("Fout", f"Kamer {kamer} bestaat niet in de gegevens.")
            return

        # Sla de gegevens op in het JSON-bestand
        with open("jsonfiles/kamers.json", "w") as f:
            json.dump(data, f, indent=4)

        messagebox.showinfo("Succes", "De bezetting is toegevoegd!")
        bezetting_window.destroy()

    # Creëer een nieuw venster
    bezetting_window = tk.Tk()
    bezetting_window.title("Voeg Kamer Bezetting Toe")
    bezetting_window.geometry("600x500")

    # Kamers (101-108)
    kamers = [f"Kamer {i}" for i in range(101, 109)]

    # Dokters (hardcoded in de GUI)
    dokters = [
        "Michiel Ooghe (Bureau 101)",
        "Thibo Terryn (Bureau 102)",
        "Ramsey Carpentier (Bureau 103)",
        "Florian Titiljon (Bureau 104)",
        "Jos de Vos (Bureau 105)"
    ]

    # Label en combobox voor kamer
    tk.Label(bezetting_window, text="Selecteer een kamer:", font=("Arial", 14)).pack(pady=10)
    kamer_combobox = ttk.Combobox(bezetting_window, values=kamers, state="readonly", font=("Arial", 12))
    kamer_combobox.pack(pady=5, fill=tk.X, padx=20)

    # Label en combobox voor dokter
    tk.Label(bezetting_window, text="Selecteer een dokter:", font=("Arial", 14)).pack(pady=10)
    dokter_combobox = ttk.Combobox(bezetting_window, values=dokters, state="readonly", font=("Arial", 12))
    dokter_combobox.pack(pady=5, fill=tk.X, padx=20)

    # Laad patiëntengegevens uit JSON
    with open("jsonfiles/patienten.json", "r") as f:
        patienten_data = json.load(f)
    patiënt_namen = [patiënt["naam"] for patiënt in patienten_data["patienten"]]

    # Combobox met patiëntennamen
    tk.Label(bezetting_window, text="Selecteer een patiënt:", font=("Arial", 14)).pack(pady=10)
    patient_combobox = ttk.Combobox(bezetting_window, values=patiënt_namen, state="readonly", font=("Arial", 12))
    patient_combobox.pack(pady=5, fill=tk.X, padx=20)

    # Invoerveld voor datum
    tk.Label(bezetting_window, text="Voer de datum in (YYYY-MM-DD):", font=("Arial", 14)).pack(pady=10)
    datum_entry = tk.Entry(bezetting_window, font=("Arial", 12))
    datum_entry.pack(pady=5, fill=tk.X, padx=20)

    # Invoerveld voor reden
    tk.Label(bezetting_window, text="Voer de reden in:", font=("Arial", 14)).pack(pady=10)
    reden_entry = tk.Entry(bezetting_window, font=("Arial", 12))
    reden_entry.pack(pady=5, fill=tk.X, padx=20)

    # Voeg bezetting toe knop
    tk.Button(bezetting_window, text="Voeg Bezetting Toe", command=voeg_bezetting_toe, font=("Arial", 14), bg="green", fg="white").pack(pady=20)

def open_Kamer(kamer):
    kalender_window = tk.Toplevel(window)
    kalender_window.title(f"Kamer - {kamer}")
    kalender_window.geometry("1000x700")
    kalender_window.grab_set()

    # Frame voor kalender
    global kalender_frame
    kalender_frame = tk.Frame(kalender_window)
    kalender_frame.grid(pady=20)

    # Naam van het bureau bovenaan, de kalender verschuift iets naar beneden
    kamer_label = tk.Label(kalender_frame, text=f"{kamer}", font=("Arial", 22, "bold"))
    kamer_label.pack(pady=10)  # Plaats het label met wat ruimte bovenaan het frame

    json_file2 = f"jsonfiles/Kamers.json"
    # Laad bestaande data of maak een lege dictionary
    try:
        with open(json_file2, "r") as file:
            data = json.load(file)
        kamers = data["Kamers"]["categorieen"]
    except (FileNotFoundError, json.JSONDecodeError):
        kamers = []

    # Functie om de kalender te updaten
    def update_kalender():
        """Update de kalenderweergave met operatiegegevens."""
        for widget in kalender_window.winfo_children():
            widget.destroy()  # Vernietig alle widgets in het frame
        maak_kalender()  # Bouw de kalender opnieuw op

    # Functie om een operatie te verwijderen
    def verwijder_bezzeting(datum):
        if datum in data:
            for kamer_data in kamers:
                if kamer_data["naam"] == kamer:
                    bezetingen = kamer_data["bezetingen"]
                    bezetingen = [bez for bez in bezetingen if bez["datum"] != datum]
                    kamer_data["bezetingen"] = bezetingen
                    break
            with open(json_file2, "w") as file:
                json.dump(data, file, indent=4)
            messagebox.showinfo("Operatie verwijderd", f"Operatie op {datum} is verwijderd.")
            update_kalender()
        else:
            messagebox.showinfo("Geen operatie", f"Er staat geen operatie gepland op {datum}.")

    # Functie om een datum te toggelen (toevoegen of verwijderen)
    def toggle_datum(datum):
        """Schakel tussen het toevoegen of verwijderen van een operatie."""
        if datum in data:
            bevestiging = messagebox.askyesno(
                "Verwijderen", f"Wil je de operatie op {datum} verwijderen?"
            )
            if bevestiging:
                verwijder_bezzeting(datum)

    # Functie om de kalender voor december te maken
    def maak_kalender():
        """Maak een kalender voor december."""
        dagen_in_maand = 31
        eerste_dag = datetime(2024, 12, 1).weekday()  # Maandag=0, Zondag=6

        # Header: Dagen van de week
        dagen = ["Ma", "Di", "Wo", "Do", "Vr", "Za", "Zo"]
        for col, dag in enumerate(dagen):
            tk.Label(kalender_window, text=dag, font=("Arial", 12, "bold"), width=12, height=2).grid(row=2, column=col)

        # Datum knoppen
        row = 3
        col = eerste_dag
        for dag in range(1, dagen_in_maand + 1):
            datum = f"2024-12-{dag:02d}"
            bezetingen = []

            # Zoek bezetingen voor de specifieke kamer
            for kamer_data in kamers:
                if kamer_data["naam"] == kamer:
                    bezetingen = kamer_data["bezetingen"]
                    break

            datums = [bez["datum"] for bez in bezetingen]
            if datum in datums:
                info = next(bez for bez in bezetingen if bez["datum"] == datum)
                patient = info.get("patient", "Onbekend")
                dokter = info.get("dokter", "Onbekend")
                operatie = info.get("waarom", "Onbekend")
                tekst = f"{dag}\n{patient}\n{dokter}\n{operatie}"
                kleur = "red"
            else:
                tekst = str(dag)
                kleur = "green"

            btn = tk.Button(
                kalender_window, text=tekst, bg=kleur, fg="white", width=12, height=4,
                command=lambda d=datum: toggle_datum(d)
            )
            btn.grid(row=row, column=col, padx=2, pady=2)

            col += 1
            if col > 6:  # Nieuwe rij na zondag
                col = 0
                row += 1

    # Maak de kalender
    maak_kalender()

# Initialize main window
window = tk.Tk()
window.title("Ziekenhuis Visualisatie")
window.geometry("1300x1000")

# Create a canvas for drawing
canvas = tk.Canvas(window, width=1000, height=800)
canvas.pack()

# Draw the main hospital layout
teken_ziekenhuis()

# Run the tkinter main loop
window.mainloop()
