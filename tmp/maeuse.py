class Simulator(object):
    def __init__(self, p):
        self.schritte = 0
        self.population = p
    def setSchritte(self, s):
        self.schritte = s
    def simulieren(self):
        for i in range(self.schritte):
            self.population.naechstePopulation()

class Population(object):
    def __init__(self, j, e, a):
        self.jung = j
        self.erwachsen = e
        self.alt = a
    def naechstePopulation(self):
        h = self.erwachsen
        self.erwachsen = self.jung / 2
        self.jung = h*4 + self.alt*2
        self.alt = h / 3
