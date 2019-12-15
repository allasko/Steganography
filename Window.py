from tkinter import *
from tkinter import ttk
from Stega import steganography, reading

class Window(Frame):
    def __init__(self, master=None):

        Frame.__init__(self, master)
        self.master = master
        # Setting title
        self.master.title("Steganografia")
        # Allowing the widget to take full space of the root window
        self.pack(fill=BOTH, expand=1)
        # Creating button
        submitButton = Button(self, text="Prześlij", command=self.buttonHandler)
        submitButton2 = Button(self, text="Prześlij", command=self.buttonHandler2)
        # Placing button
        submitButton.grid(column=3, row=2, padx=10)
        submitButton2.grid(column=3, row=5, padx=10)
        # Creating labels
        txtpathLabel = Label(self, text="Podaj ścieżkę do pliku, który chcesz ukryć: ")
        txtpathLabel.grid(column=0, row=1)
        photopathLabel = Label(self, text="Podaj ścieżkę do zdjęcia: ")
        photopathLabel.grid(column=0, row=2)
        readLabel = Label(self, text="Odczytaj ze zdjęcia: ")
        readLabel.grid(column=0, row=5)
        # Creating entries
        self.txtpathEntry = Entry(self)
        self.txtpathEntry.grid(column=1, row=1, columnspan=2)
        self.photopathEntry = Entry(self)
        self.photopathEntry.grid(column=1, row=2, columnspan=2)
        self.photoEntry = Entry(self)
        self.photoEntry.grid(column=1, row=5, columnspan=2)
        # Creating info textbox
        infoBox = Text(self, height=7, width=70, wrap=WORD)
        infoBox.grid(column=1, row=0, pady=10)
        info = """\t\t\tINFO
* możesz podać jedynie pliki w formacie *.txt
* pamiętaj, aby długość szyfrogramu nie była dłuższa niż (wysokość zdjęcia * szerokość zdjęcia * 3) - 32
* zdjęcie będące wynikiem zostanie zapisane w folderze z programem z nazwą "zaszyfrowany.png"
* ukrywanie informacji zaczyna się od lewego górnego rogu """
        infoBox.insert(END, info)
        self.readBox = Text(self, height=10, width=70, wrap=CHAR)
        self.readBox.grid(column=1, row=6, pady=10)
        # Creating eparator
        separator = ttk.Separator(self, orient=HORIZONTAL)
        separator.grid(column=0, row=3, sticky="we", pady=5, columnspan=7)

    def buttonHandler(self):
        file = self.txtpathEntry.get()
        photo = self.photopathEntry.get()
        steganography(file,photo)
    def buttonHandler2(self):
        photo = self.photoEntry.get()
        text = reading(photo)
        self.readBox.insert(END, text)


