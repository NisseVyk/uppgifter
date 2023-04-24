import random

class Lotteri:

    def __init__(self):

        self.list_vinster =[

            "en solstol", 
            "en Iphone", 
            "en apelsin",
            "Senapsgas",
            "Termit",
            "F22",
            "en tandborste",
            "en ballong",
            "37 mongoliska barn",
            "4kg kokain",
            "AIDS",
            "en stol",
            "absolut vodka",
            "en gammal tant",
            "Arvids keps",
            "down syndrom",
            "en plastpåse",
            "reverse Michael Jackson",
            "en rysk ubåt",
            "Joseph Stalins lårbenshals",
            "två tuber mystisk salva",
            "två träd",
            "en polsk människosmugglare",
            "3st halvätna bananer"


        ]

    def get_vinst(self):

        slumptal = random.randint(0,23)

        return self.list_vinster[slumptal]
