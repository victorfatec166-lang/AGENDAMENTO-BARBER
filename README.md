# 💈 AGENDAMENTO-BARBER

> Sistema de agendamento para barbearia desenvolvido como projeto de estudo e prática em desenvolvimento de software.

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![Projeto](https://img.shields.io/badge/projeto-estudo-blue)
![GitHub](https://img.shields.io/badge/GitHub-victorfatec166--lang-black?logo=github)

---

## 📌 Sobre o projeto

O **AGENDAMENTO-BARBER** é um projeto desenvolvido com o objetivo de estudar e praticar conceitos de desenvolvimento de aplicações para gerenciamento e agendamento de serviços em uma barbearia.

A ideia do projeto é criar uma solução que permita organizar os processos de agendamento e, futuramente, evoluir para um sistema mais completo de gerenciamento de clientes, barbeiros, serviços e horários.

Este projeto está em **fase de desenvolvimento e aprendizado**, portanto novas funcionalidades, melhorias e correções serão adicionadas ao longo do desenvolvimento.

---

## 🎯 Objetivos

O projeto foi criado principalmente para colocar em prática conceitos como:

* Desenvolvimento de aplicações web
* Organização de projetos
* Estruturação de código
* Criação de APIs
* Manipulação de banco de dados
* Sistema de agendamentos
* Testes automatizados
* Migrações de banco de dados
* Boas práticas de desenvolvimento
* Versionamento utilizando Git e GitHub

---

## ✨ Funcionalidades

### Atualmente

O projeto está em desenvolvimento e possui uma estrutura preparada para evolução do sistema.

Entre os recursos trabalhados estão:

* 📅 Sistema de agendamento
* 👤 Gerenciamento de usuários/clientes
* 💈 Gerenciamento relacionado à barbearia
* 🗓️ Controle de horários
* 🗄️ Estrutura de banco de dados
* 🔄 Migrações utilizando Alembic
* 🧪 Estrutura para testes automatizados

### 🚧 Em desenvolvimento

Algumas funcionalidades ainda estão sendo implementadas e aprimoradas, como:

* [ ] Dashboard administrativo
* [ ] Cadastro completo de clientes
* [ ] Cadastro de barbeiros
* [ ] Cadastro de serviços
* [ ] Gerenciamento de horários
* [ ] Histórico de agendamentos
* [ ] Cancelamento de agendamentos
* [ ] Sistema de autenticação
* [ ] Melhorias na interface
* [ ] Relatórios
* [ ] Integração com banco de dados em ambiente de produção

---

## 🛠️ Tecnologias

O projeto utiliza tecnologias voltadas ao desenvolvimento de uma aplicação estruturada, incluindo:

* **Python**
* **API / Backend**
* **Alembic** para controle de migrações
* **Pytest** para testes
* **Git**
* **GitHub**

A estrutura atual do repositório também conta com diretórios separados para código-fonte e testes.

---

## 📂 Estrutura do projeto

```text
AGENDAMENTO-BARBER/
│
├── .vscode/
│
├── TESTE-AGENDAMENTO/
│
├── src/
│   └── Código principal da aplicação
│
├── tests/
│   └── Testes automatizados
│
├── alembic/
│   └── Migrações do banco de dados
│
├── alembic.ini
├── pytest.ini
├── .gitignore
└── README.md
```

> A estrutura poderá ser modificada conforme novas funcionalidades forem adicionadas ao projeto.

---

## 🚀 Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/victorfatec166-lang/AGENDAMENTO-BARBER.git
```

### 2. Entre na pasta

```bash
cd AGENDAMENTO-BARBER
```

### 3. Crie um ambiente virtual

No Windows:

```bash
python -m venv venv
```

Ative o ambiente:

```bash
venv\Scripts\activate
```

No Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

> Caso o arquivo `requirements.txt` ainda não esteja disponível na versão atual do projeto, instale as dependências utilizadas pelo ambiente de desenvolvimento.

### 5. Execute o projeto

O comando de inicialização pode variar conforme a estrutura atual da aplicação.

Consulte os arquivos dentro de `src/` para identificar o ponto de entrada da aplicação.

---

## 🧪 Testes

O projeto possui uma estrutura dedicada para testes utilizando **Pytest**.

Para executar os testes:

```bash
pytest
```

Ou:

```bash
python -m pytest
```

Os testes estão localizados no diretório:

```text
tests/
```

---

## 🗄️ Banco de dados

O projeto utiliza **Alembic** para gerenciamento das migrações do banco de dados.

As configurações estão relacionadas ao arquivo:

```text
alembic.ini
```

E as migrações ficam dentro de:

```text
alembic/
```

Para criar uma nova migração:

```bash
alembic revision --autogenerate -m "descrição da alteração"
```

Para aplicar as migrações:

```bash
alembic upgrade head
```

---

## 🧠 O que estou aprendendo com este projeto

Este projeto faz parte do meu processo de aprendizado em desenvolvimento de software.

Durante o desenvolvimento estou buscando entender melhor:

* Como estruturar uma aplicação
* Como criar APIs
* Como trabalhar com banco de dados
* Como utilizar ORM
* Como realizar migrações
* Como escrever testes
* Como organizar código
* Como utilizar Git e GitHub
* Como corrigir erros e melhorar uma aplicação existente
* Como transformar uma ideia em um software funcional

---

## 🔮 Próximos passos

O projeto continuará sendo desenvolvido gradualmente.

Algumas das próximas etapas planejadas são:

1. Melhorar o sistema de agendamentos
2. Implementar autenticação
3. Criar gerenciamento de clientes
4. Criar gerenciamento de barbeiros
5. Criar gerenciamento de serviços
6. Melhorar a interface do sistema
7. Implementar dashboard
8. Aumentar a cobertura de testes
9. Melhorar a documentação
10. Preparar o projeto para um ambiente de produção

---

## 📚 Projeto de aprendizado

Este projeto não tem como objetivo, neste momento, representar um sistema comercial finalizado.

Ele está sendo desenvolvido principalmente como uma forma de **aprender, experimentar tecnologias e evoluir minhas habilidades como desenvolvedor**.

Erros, refatorações e mudanças fazem parte do processo de desenvolvimento.

---

## 👨‍💻 Autor

Desenvolvido por **Victor Fatec**.

GitHub:

[![GitHub](https://img.shields.io/badge/GitHub-victorfatec166--lang-black?logo=github)](https://github.com/victorfatec166-lang)

---

## ⭐ Contribuição

Sugestões, melhorias e ideias são bem-vindas.

Caso encontre algum problema ou tenha uma sugestão para o projeto, você pode abrir uma **Issue** no GitHub.

---

## 📄 Licença

Este projeto ainda está em desenvolvimento. A definição de uma licença poderá ser adicionada posteriormente.

---

<div align="center">

### 💈 AGENDAMENTO-BARBER

**Projeto de estudo e evolução em desenvolvimento de software.**

</div>
