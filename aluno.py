class Aluno:
    
    def __init__(self, nome, senha, cpf, curso, campus):
        self.nome = nome
        self.senha = senha
        self.cpf = cpf
        self.curso = curso
        self.campus = campus
        self.horas_totais = 3200
        self.horas_cumpridas = 0
        
        
    def get_nome(self):
        return self.nome
    
    def get_horas_pendentes(self):
        return self.horas_totais - self.horas_cumpridas

    def validar_cpf(self):
        cpf = ''.join(filter(str.isdigit, self.cpf))

        if len(cpf) != 11:
            return False

        if cpf == cpf[0] * 11:
            return False

        soma = 0
        for i in range(9):
            soma += int(cpf[i]) * (10 - i)
        dig1 = (soma * 10) % 11
        dig1 = 0 if dig1 == 10 else dig1

        soma = 0
        for i in range(10):
            soma += int(cpf[i]) * (11 - i)
        dig2 = (soma * 10) % 11
        dig2 = 0 if dig2 == 10 else dig2

        return cpf[-2:] == f"{dig1}{dig2}"
    
    
    
class Monitor(Aluno):
    def __init__(self, nome, senha, cpf, curso, campus, disciplina_monitoria):
        super().__init__(nome, senha, cpf, curso, campus)
        self.disciplina_monitoria = disciplina_monitoria
        self.horas_monitoria_trabalhadas = 0

    def registrar_trabalho_monitoria(self, horas):
        self.horas_monitoria_trabalhadas += horas
        self.horas_cumpridas += horas
        print(f"Registrado {horas} horas de monitoria em {self.disciplina_monitoria}")