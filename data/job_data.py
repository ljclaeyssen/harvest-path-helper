class Harvestable:
    def __init__(self, name, level, image_url=""):
        self.name = name
        self.image_url = image_url
        self.level = level

    def __repr__(self):
        return f"Harvestable(name={self.name}, level={self.level}, image_url={self.image_url})"


class Job:
    def __init__(self, name, harvestables):
        self.name = name
        self.harvestables = harvestables

    def __repr__(self):
        return f"Job(name={self.name}, harvestables={self.harvestables})"


jobs_data = [
    Job("Bûcheron", [
        Harvestable("Frêne", 1),
        Harvestable("Châtaignier", 20),
        Harvestable("Noyer", 40),
        Harvestable("Chêne", 60),
        Harvestable("Bombu", 70),
        Harvestable("Érable", 80),
        Harvestable("Oliviolet", 90),
        Harvestable("Pin", 90),
        Harvestable("If", 100),
        Harvestable("Bambou", 110),
        Harvestable("Merisier", 120),
        Harvestable("Noisetier", 130),
        Harvestable("Ébène", 140),
        Harvestable("Kaliptus", 150),
        Harvestable("Charme", 160),
        Harvestable("Bambou Sombre", 170),
        Harvestable("Orme", 180),
        Harvestable("Bambou Sacré", 190),
        Harvestable("Aquajou", 200),
        Harvestable("Tremble", 200),
    ]),
    Job("Mineur", [
        Harvestable("Fer", 1),
        Harvestable("Cuivre", 20),
        Harvestable("Bronze", 40),
        Harvestable("Kobalte", 60),
        Harvestable("Manganèse", 80),
        Harvestable("Étain", 100),
        Harvestable("Silicate", 100),
        Harvestable("Argent", 120),
        Harvestable("Bauxite", 140),
        Harvestable("Or", 160),
        Harvestable("Dolomite", 180),
        Harvestable("Cendrepierre", 180),
        Harvestable("Obsidienne", 200),
        Harvestable("Ecume de mer", 200),
        Harvestable("Cristal pliable", 200),
        Harvestable("Cristal liquide", 200),
    ]),
    Job("Paysan", [
        Harvestable("Blé", 1),
        Harvestable("Orge", 20),
        Harvestable("Avoine", 40),
        Harvestable("Houblon", 60),
        Harvestable("Lin", 80),
        Harvestable("Seigle", 100),
        Harvestable("Riz", 100),
        Harvestable("Malt", 120),
        Harvestable("Chanvre", 140),
        Harvestable("Maïs", 160),
        Harvestable("Millet", 180),
        Harvestable("Frostiz", 200),
        Harvestable("Quisnoa", 200),
    ]),
    Job("Alchimiste", [
        Harvestable("Ortie", 1),
        Harvestable("Sauge", 20),
        Harvestable("Trèfle à 5 feuilles", 40),
        Harvestable("Menthe Sauvage", 60),
        Harvestable("Orchidée Freyesque", 80),
        Harvestable("Edelweiss", 100),
        Harvestable("Graine de Pandouille", 120),
        Harvestable("Ginseng", 140),
        Harvestable("Belladone", 160),
        Harvestable("Mandragore", 180),
        Harvestable("Perce-Neige", 200),
        Harvestable("Salikrone", 200),
        Harvestable("Tulipe en papier", 200),
    ]),
    Job("Pêcheur", [
        Harvestable("Goujon", 1),
        Harvestable("Greuvette", 10),
        Harvestable("Truite", 20),
        Harvestable("Crabe Sourimi", 30),
        Harvestable("Poisson-Chaton", 40),
        Harvestable("Poisson Pané", 50),
        Harvestable("Carpe d'Iem", 60),
        Harvestable("Sardine Brillante", 70),
        Harvestable("Brochet", 80),
        Harvestable("Kralamoure", 90),
        Harvestable("Anguille", 100),
        Harvestable("Dorade Grise", 110),
        Harvestable("Perche", 120),
        Harvestable("Raie Bleue", 130),
        Harvestable("Lotte", 140),
        Harvestable("Requin Marteau-Faucille", 150),
        Harvestable("Bar Rikain", 160),
        Harvestable("Morue", 170),
        Harvestable("Tanche", 180),
        Harvestable("Espadon", 190),
        Harvestable("Patelle", 200),
        Harvestable("Poisskaille", 200),
        Harvestable("Pichon d'encre", 200),
    ]),
]