class Simulator(object):
    def __init__(self,p):
        self.schritt = None
        self.population = Population()
    def setSchritte(self,s):
        self.schritt = s
    def simulieren(self):
        
class Population(object):
    def __init__(self,j,e,a)
        self.jung = j
        self.erwachsen = e
        self.alt = a
    def naechstePopulation(self):
        j = 4 * self.erwachsen + 2 * self.alt
        e = 0.5 * self.jung
        a = (1/3) * self.erwachsen
    
