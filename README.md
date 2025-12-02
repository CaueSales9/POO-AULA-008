📘 Sistema UFC — Gerenciamento de Alunos, Cursos e Monitoria

Este projeto implementa um sistema de cadastro e gerenciamento de alunos da UFC, permitindo criar contas, realizar login, trocar de curso, trancar curso, virar monitor e registrar horas de monitoria.
O sistema é totalmente feito em Python, utilizando classes e herança para organizar suas funcionalidades.

📂 Estrutura do Projeto
📁 Projeto/
 ├── aluno.py       # Classe Aluno e Monitor
 ├── campus.py      # Classe Campus
 ├── cursos.py      # Classe Cursos (lista de campus e cursos)
 ├── main.py        # Lógica principal do sistema e menus
 └── README.md      # Documentação

🧠 Funcionalidades
👤 Cadastro de Aluno

CPF validado automaticamente

Nome de usuário único

Escolha de campus e curso

Armazena carga horária obrigatória (3200h)

🔐 Login

Login por nome de usuário e senha

Menu completo para gerenciar sua conta

🎓 Funções do Menu do Aluno

Ver curso e informações

Trocar de curso

Trancar curso

Deletar conta

Sistema de Monitoria

Deslogar

🛠️ Sistema de Monitoria

Qualquer aluno pode:

Escolher campus e curso para virar monitor

Registrar horas trabalhadas como monitor

Horas registradas entram como horas cumpridas

A classe Monitor é herdada de Aluno, adicionando:

Disciplina de monitoria

Controle de horas trabalhadas

🧩 Classes Principais
Aluno

✔ Armazena dados pessoais
✔ Valida CPF
✔ Calcula horas pendentes para formação

Monitor (Aluno)

✔ Possui disciplina de monitoria
✔ Registra horas trabalhadas

Campus

✔ Representa um campus com sua lista de cursos

Cursos

✔ Contém todos os campus e cursos disponíveis
✔ Armazena contas cadastradas

Main

✔ Controla o menu
✔ Cadastro, login e operações do aluno

▶️ Como executar

Certifique-se de que todos os arquivos .py estão no mesmo diretório.

Execute o comando:

python main.py


O menu principal será exibido:

==Bem vindo ao menu do Sistema UFC==

1 - Cadastrar conta
2 - Login
3 - Ver cursos
4 - Sair

✔️ Requisitos

Python 3.8+

Terminal / CMD

📌 Observações

O CPF é sanitizado e validado conforme o algoritmo original.

O sistema roda totalmente no terminal.

Monitoria funciona como uma “promoção” de aluno → monitor.

📄 Licença

Este projeto é livre para estudo e modificação.
