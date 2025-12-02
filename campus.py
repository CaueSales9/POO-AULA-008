class Campus:
    def __init__(self, nome, cursos):
        self.nome = nome
        self.cursos = cursos

    def __str__(self):
        return self.nome