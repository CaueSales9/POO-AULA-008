from campus import Campus

class Cursos:
    def __init__(self):
        self.contas = []
        
        self.lista_campus = [
            Campus("Itapajé", ["ADS", "Ciência de Dados", "Segurança da Informação"]),
            Campus("Russas", ["Engenharia de Software", "Ciência da Computação", "Engenharia Civil"]),
            Campus("Quixadá", ["Design Digital", "Engenharia de Computação", "Redes de Computadores"]),
            Campus("Sobral", ["Ciências Econômicas", "Engenharia Elétrica", "Medicina"])
        ]