class Benutzer(object):
    def __init__(self, name):
        self.name = name
        self.email = ""
        self.artikel = []

    def setzeEmail(self, email):
        self.email = email

    def arbeitAnArtikel(self, artikel):
        if not artikel in self.artikel:
            self.artikel += [artikel]

class Artikel(object):
    def __init__(self, stichwort):
         self.stichwort = stichwort
         self.erlaeuterung = ""
         self.autor = []

    def schreibeErlaeuterung(self, text, autor):
        self.erlaeuterung = text
        self.autor += [autor]
        autor.arbeitAnArtikel(self)


    # Das folgende ist unnötig
    def aendereErlauterung(self, text, autor):
        self.erlaeuterung = text
        if not autor in self.autor:
            self.autor += [autor]
            autor.arbeitAnArtikel(self)


helmut03 = Benutzer("helmut03")
loreley = Benutzer("loreley")

html = Artikel("HTML")
html.schreibeErlaeuterung("HTML ist keine Programmiersprache, es ist eine Markup Language", helmut03)

css = Artikel("CSS")
css.schreibeErlaeuterung("CSS ist eine Erweiterung für HTML", loreley)

barrierefreiheit = Artikel("Berrierefreiheit")
barrierefreiheit.schreibeErlaeuterung("Rollstuhlfahrer scheiß", loreley)

css.aendereErlauterung("HTML ist keine Programmiersprache, es ist eine Markup Language. Es ist schrecklich damit arbeiten zu müssen", helmut03)
