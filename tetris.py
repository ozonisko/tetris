from tkinter import *
import time
import random
import copy
from tkinter import messagebox

top = Tk()
kolor_tla = "black"
kolor_ziemi = "red"
kwad = []
lista_kolorow = ["yellow", "blue", "green", "purple"]
lista_ksztaltow = ["L", "O", "I", "T", "Z"]
x, y = 10, 20
rozmiar_klocka = 20
punkt_startu = int(1.5 * x)
obrot_I = [[1,1], [-1,1], [-1,-1], [1,-1]]
obrot_L = [[0,-2], [2, 0], [0, 2], [-2, 0]]
punkty = 0

C = Canvas(top, bg=kolor_tla, height=y * rozmiar_klocka, width=x * rozmiar_klocka, bd=0)
for i in range(y):
    for j in range(x):
        kwad.append(C.create_rectangle(j * rozmiar_klocka, i * rozmiar_klocka, (j + 1) * rozmiar_klocka, (i + 1) * rozmiar_klocka, fill=kolor_tla, outline=kolor_tla))


class Plansza():
    def __init__(self, master):
        koniec_gry = False


class Klocek():
    def __init__(self, master):
        self.kolor = random.choice(lista_kolorow)
        self.ksztalt = random.choice(lista_ksztaltow)
        self.lezacy = False
        self.master = master
        self.master.bind('<Down>', self.turndown)
        self.master.bind('<Left>', self.turnleft)
        self.master.bind('<Right>', self.turnright)
        self.master.bind('<Up>', self.obroc)
        self.ruszaj_sie = True
        self.ilosc_obrotow = 0
        if self.ksztalt == "L":
            self.pozycja_startowa = [punkt_startu, punkt_startu+1, punkt_startu+2, punkt_startu-x+2]
        elif self.ksztalt == "O":
            self.pozycja_startowa = [punkt_startu, punkt_startu+1, punkt_startu-x, punkt_startu-x+1]
        elif self.ksztalt == "I":
            self.pozycja_startowa = [punkt_startu, punkt_startu+1, punkt_startu+2, punkt_startu+3]
        elif self.ksztalt == "T":
            self.pozycja_startowa = [punkt_startu, punkt_startu+1, punkt_startu+2, punkt_startu-x+1]
        elif self.ksztalt == "Z":
            self.pozycja_startowa = [punkt_startu, punkt_startu+1, punkt_startu+x+1, punkt_startu+x+2]
        for i in self.pozycja_startowa:
            C.itemconfig(kwad[i], fill=self.kolor)
        self.nowa_pozycja = [0, 0, 0, 0]

    def porusz_klockiem(self, kierunek=x):
        print("ide", self.kolor)
        if self.ruszaj_sie:
            self.wyczysc_stara_pozycje()
            for i in range(len(self.pozycja_startowa)):
                self.nowa_pozycja[i] = copy.deepcopy(self.pozycja_startowa[i] + kierunek)
            self.narysuj_nowa_pozycje()
            for i in self.nowa_pozycja:  # sprawdzanie czy nie dotknal ziemi
                if i >= (y - 1) * x or C.itemcget(kwad[i + x], "fill") == kolor_ziemi:
                    self.ruszaj_sie = False
                    for i in self.nowa_pozycja:
                        C.itemconfig(kwad[i], fill=kolor_ziemi)
                        sprawdz_linie()
                        if i < 20:
                            koniec()
                            return
                    stworz_klocek()
                    return
            if kierunek == x:
                self.master.after(700, self.porusz_klockiem)
            else:
                return



    def turnleft(self, event):
        self.porusz_klockiem(-1)

    def turnright(self, event):
        self.porusz_klockiem(1)

    def turndown(self, event):
        self.porusz_klockiem(x)

    def wyczysc_stara_pozycje(self):
        for i in self.pozycja_startowa:
            C.itemconfig(kwad[i], fill=kolor_tla)

    def narysuj_nowa_pozycje(self):
        for i in self.nowa_pozycja:
             C.itemconfig(kwad[i], fill=self.kolor)
        self.pozycja_startowa = self.nowa_pozycja

    def obroc(self, event):
        self.wyczysc_stara_pozycje()
        if self.ksztalt == "I":
            self.nowa_pozycja[0] = copy.deepcopy(self.pozycja_startowa[0] + x*obrot_I[self.ilosc_obrotow%4][0] + obrot_I[self.ilosc_obrotow%4][1])
            self.nowa_pozycja[2] = copy.deepcopy(self.pozycja_startowa[2] + x*obrot_I[(self.ilosc_obrotow+2)%4][0] + obrot_I[(self.ilosc_obrotow+2)%4][1])
            self.nowa_pozycja[3] = copy.deepcopy(self.pozycja_startowa[3] + x*obrot_I[(self.ilosc_obrotow+2)%4][0]*2 + obrot_I[(self.ilosc_obrotow+2)%4][1]*2)
        elif self.ksztalt == "L":
            self.nowa_pozycja[0] = copy.deepcopy(self.pozycja_startowa[0] + x * obrot_I[self.ilosc_obrotow % 4][0] +obrot_I[self.ilosc_obrotow % 4][1])
            self.nowa_pozycja[2] = copy.deepcopy(self.pozycja_startowa[2] + x * obrot_I[(self.ilosc_obrotow + 2) % 4][0] +obrot_I[(self.ilosc_obrotow + 2) % 4][1])
            self.nowa_pozycja[3] = copy.deepcopy(self.pozycja_startowa[3] + x * obrot_L[self.ilosc_obrotow % 4][0] +obrot_L[self.ilosc_obrotow % 4][1])
        elif self.ksztalt == "T":
            self.nowa_pozycja[0] = copy.deepcopy(self.pozycja_startowa[0] + x * obrot_I[self.ilosc_obrotow % 4][0] + obrot_I[self.ilosc_obrotow % 4][1])
            self.nowa_pozycja[2] = copy.deepcopy(self.pozycja_startowa[2] + x * obrot_I[(self.ilosc_obrotow + 2) % 4][0] + obrot_I[(self.ilosc_obrotow + 2) % 4][1])
            self.nowa_pozycja[3] = copy.deepcopy(self.pozycja_startowa[3] + x * obrot_I[(self.ilosc_obrotow + 3) % 4][0] + obrot_I[(self.ilosc_obrotow + 3) % 4][1])
        elif self.ksztalt == "Z":
            self.nowa_pozycja[0] = copy.deepcopy(self.pozycja_startowa[0] + x * obrot_I[self.ilosc_obrotow % 4][0] + obrot_I[self.ilosc_obrotow % 4][1])
            self.nowa_pozycja[2] = copy.deepcopy(self.pozycja_startowa[2] + x * obrot_I[(self.ilosc_obrotow + 1) % 4][0] + obrot_I[(self.ilosc_obrotow + 1) % 4][1])
            self.nowa_pozycja[3] = copy.deepcopy(self.pozycja_startowa[3] + x * obrot_L[(self.ilosc_obrotow + 3) % 4][0] + obrot_L[(self.ilosc_obrotow + 3) % 4][1])

        self.narysuj_nowa_pozycje()
        self.ilosc_obrotow += 1


def sprawdz_linie():
    for i in range(y):
        flaga = True
        for j in range(x):
            if C.itemcget(kwad[i * x + j], "fill") != kolor_ziemi:
                flaga = False
                break
        if flaga:
            # punkty += 10
            for j in range(i, 1, -1):
                print(j)
                for q in range(x):
                    C.itemconfig(kwad[j * x + q], fill=C.itemcget(kwad[(j - 1) * x + q], "fill"))


def koniec():
    messagebox.showinfo("Game Over", "Score: " + str(punkty))

def stworz_klocek():
    k = Klocek(top)
    k.porusz_klockiem()


kloc = stworz_klocek()

C.pack()
top.mainloop()
