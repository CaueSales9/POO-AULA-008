from aluno import Aluno, Monitor
from cursos import Cursos


1
class Main(Cursos):
    def __init__(self, nome_sistema: str):
        super().__init__() 
        self.nome_sistema = nome_sistema

    def cadastrar_conta(self):
        print(f"Bem vindo ao {self.nome_sistema}!")
        print("Realize seu cadastro")
        
        cpf = input("Digite seu CPF:\n> ").strip()
        nome = input("Crie seu nome de usuário:\n> ").strip()
        senha = input("Crie sua senha:\n> ").strip()
        
        print("\nCampus disponíveis:")
        for i, campus in enumerate(self.lista_campus):
            print(f"{i + 1} - {campus.nome}")
    
    
        try:
            opcao_campus = int(input('\nEscolha o número do seu campus:\n> ')) - 1
            if opcao_campus < 0 or opcao_campus >= len(self.lista_campus):
                print("\nOpção inválida!\n")
                return
            
            campus_selecionado = self.lista_campus[opcao_campus]
        except ValueError:
            print("\nDigite um número válido!\n")
            return
    
        print(f"\nCursos disponíveis no campus {campus_selecionado.nome}:")
        for i, curso in enumerate(campus_selecionado.cursos):
            print(f"{i + 1} - {curso}")
    
        try:
            opcao_curso = int(input('\nEscolha o número do seu curso:\n> ')) - 1
            if opcao_curso < 0 or opcao_curso >= len(campus_selecionado.cursos):
                print("\nOpção inválida!\n")
                return
            
            curso_selecionado = campus_selecionado.cursos[opcao_curso]
        except ValueError:
            print("\nDigite um número válido!\n")
            return
        

        cpf_num = ''.join(filter(str.isdigit, cpf))
        
        for aluno in self.contas:
            if aluno.cpf == cpf_num:
                print("\nCPF já cadastrado!\n")
                return
            if aluno.nome == nome:
                print("\nNome de usuário já existe!\n")
                return

        aluno_novo = Aluno(nome, senha, cpf_num, curso_selecionado, campus_selecionado.nome)

        if not aluno_novo.validar_cpf():
            print("\nCPF inválido!\n")
            return

        self.contas.append(aluno_novo)
        print(f"\nConta criada com sucesso!\nUsuário: {aluno_novo.nome}\nCampus: {aluno_novo.campus}\nCurso: {aluno_novo.curso}")

    def login(self):
        print("\n== Tela de Login ==")
        nome = input('Digite seu nome de usuário:\n> ').strip()
        senha = input('Digite sua senha:\n> ').strip()
        
        aluno_logado = None
        curso_monitoria = 'Nenhuma'

        for aluno in self.contas:
            if aluno.nome == nome and aluno.senha == senha:
                aluno_logado = aluno
                break
        
        if aluno_logado is None:
            print('\nUsuário ou senha incorreta!\n')
            return

        print(f'\nLogin realizado com sucesso! Bem-vindo, {aluno_logado.nome}!\n')
        
        while True:
            print('\n==Menu do Aluno==')
            print('1 - Ver meu curso')
            print('2 - Trocar de curso')
            print('3 - Trancar curso')
            print('4 - Deletar conta')
            print('5 - Monitor')
            print('6 - Sair (Deslogar)')
            
            try:
                menu_login = int(input('O que deseja fazer:\n> '))
            except ValueError:
                print('Valor inválido')
                continue
            
            if menu_login == 1:
                print(f'\nSeu campus: {aluno_logado.campus}')
                print(f'Seu curso: {aluno_logado.curso}')
                print(f'Horas para se formar: {aluno_logado.get_horas_pendentes()}')
                print(f'Monitor: {curso_monitoria}')
                    
            elif menu_login == 2:
                print("\n== Troca de Curso ==")
                print("Campus disponíveis:")
                for i, campus in enumerate(self.lista_campus):
                    print(f"{i + 1} - {campus.nome}")

                try:
                    op_camp = int(input('Escolha o número do novo campus:\n> ')) - 1
                    if op_camp < 0 or op_camp >= len(self.lista_campus):
                        print("\nOpção inválida!\n")
                        continue
                    campus_obj = self.lista_campus[op_camp]
                except ValueError:
                    print("\nDigite um número válido!\n")
                    continue

                print(f"\nCursos disponíveis em {campus_obj.nome}:")
                for i, curso in enumerate(campus_obj.cursos):
                    print(f"{i + 1} - {curso}")

                try:
                    op_cur = int(input('Escolha o número do novo curso:\n> ')) - 1
                    if op_cur < 0 or op_cur >= len(campus_obj.cursos):
                        print("\nOpção inválida!\n")
                        continue
                    curso_nome = campus_obj.cursos[op_cur]
                except ValueError:
                    print("\nDigite um número válido!\n")
                    continue
                
                aluno_logado.campus = campus_obj.nome
                aluno_logado.curso = curso_nome
                print(f"\nSucesso! Você agora está matriculado em {curso_nome} no campus {campus_obj.nome}.")

            elif menu_login == 3:
                confirmar = input('\nTem certeza que deseja trancar seu curso? (s/n):\n> ').strip().lower()
                if confirmar == 's':
                    aluno_logado.curso = "Curso trancado"
                    print('\nCurso trancado com sucesso!\n')
                else:
                    print('\nOperação cancelada\n')
                
            elif menu_login == 4:
                confirmar = input('\nTem certeza que deseja deletar sua conta? (s/n):\n> ').strip().lower()
                if confirmar == 's':
                    self.contas.remove(aluno_logado)
                    print('\nConta deletada com sucesso!\n')
                    return
                else:
                    print('\nOperação cancelada\n')
                    
            elif menu_login == 5:
                print('1 - Virar monitor')
                print('2 - Registrar horas')
                print('3 - Cancelar ')
                
                try:
                    escolha_monitoria = int(input('O que deseja fazer:\n> '))
                except ValueError:
                    print('Valor inválido')
                    continue
                    
                if escolha_monitoria == 1:
                    print("\nCampus disponíveis:")
                    for i, campus in enumerate(self.lista_campus):
                        print(f"{i + 1} - {campus.nome}")
    
                    try:
                        opcao_campus = int(input('\nEscolha o campus para dar monitoria:\n> ')) - 1
                        if opcao_campus < 0 or opcao_campus >= len(self.lista_campus):
                             print("Opção inválida")
                             continue
                        campus_selecionado = self.lista_campus[opcao_campus]
                    except ValueError:
                        print("\nDigite um número válido!\n")
                        continue
    
                    print(f"\nCursos disponíveis no campus {campus_selecionado.nome}:")
                    for i, curso in enumerate(campus_selecionado.cursos):
                        print(f"{i + 1} - {curso}")
    
                    try:
                        opcao_curso = int(input('\nEscolha o curso para dar monitoria:\n> ')) - 1
                        if opcao_curso < 0 or opcao_curso >= len(campus_selecionado.cursos):
                             print("Opção inválida")
                             continue
                        curso_monitoria = campus_selecionado.cursos[opcao_curso]
                    except ValueError:
                        print("\nDigite um número válido!\n")
                        continue

                    novo_monitor = Monitor(
                        aluno_logado.nome, 
                        aluno_logado.senha, 
                        aluno_logado.cpf, 
                        aluno_logado.curso, 
                        aluno_logado.campus,
                        curso_monitoria 
                    )
                    
                    novo_monitor.horas_cumpridas = aluno_logado.horas_cumpridas

                    self.contas.remove(aluno_logado)
                    self.contas.append(novo_monitor)
                    aluno_logado = novo_monitor
                    
                    print(f"\nParabéns! Você agora é monitor de {curso_monitoria}!")

                elif escolha_monitoria == 2:
                    if isinstance(aluno_logado, Monitor):
                        try:
                            horas = int(input("Quantas horas você trabalhou hoje?\n> "))
                            if horas > 0:
                                aluno_logado.registrar_trabalho_monitoria(horas)
                            else:
                                print("\nDigite um valor positivo.")
                        except ValueError:
                            print("\nValor inválido.")
                    else:
                        print("\nVocê precisa virar monitor antes de registrar horas!")
                
                elif escolha_monitoria == 3:
                    print("\nVoltando ao menu principal...")
                    pass

            elif menu_login == 6:
                print("\nDeslogando...")
                return
            
            else:
                print("\nOpção inválida.")
        
    def menu(self):
        while True:
            print(f'==Bem vindo ao menu do {self.nome_sistema}==')
            print('\n1 - Cadastrar conta\n2 - Login\n3 - Ver cursos\n4 - Sair')
            try:
                escolha = int(input('O que deseja fazer:\n> '))
                if escolha == 1:
                    self.cadastrar_conta()
                elif escolha == 2:
                    self.login()
                elif escolha == 3:
                    self.listar_cursos_geral()
                elif escolha == 4:
                    break
                else:
                    print('\nEscolha inválida')
            except ValueError:
                print('\nOpção incorreta\n')

    def listar_cursos_geral(self):
        print("\n== Lista de Campus e Cursos ==")
        for campus in self.lista_campus:
            print(f"\nCampus: {campus.nome}")
            for curso in campus.cursos:
                print(f"  - {curso}")
        print("-" * 30)


if __name__ == "__main__":
    sistema = Main('Sistema UFC')
    sistema.menu()