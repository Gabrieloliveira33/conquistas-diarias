#  Conquistas Diárias

> Aplicação web full-stack desenvolvida com **Django**, voltada para o gerenciamento de conquistas diárias pessoais.

[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

O sistema permite que usuários cadastrados criem, visualizem, editem e excluam suas próprias conquistas, com autenticação e controle de acesso total.

---

##  Funcionalidades

- ** Cadastro e autenticação:** Sistema seguro de login e registro de usuários.
- ** CRUD completo:** Gerenciamento total de conquistas (Criar, Ler, Atualizar e Excluir).
- ** Controle de Dono:** Associação automática de conquistas ao usuário logado.
- **🇧🇷 Interface em português:** Totalmente adaptada para o público brasileiro.
- ** Layout Moderno:** Estilização customizada com foco em usabilidade.
- ** Proteção de rotas:** Acesso restrito apenas para usuários autenticados.
- ** Arquitetura:** Separação clara entre as camadas de backend (Django) e frontend (Templates).

---

##  Tecnologias Utilizadas

| Tecnologia | Descrição |
| :--- | :--- |
| **Python 3.12.10** | Linguagem de programação principal |
| **Django 6.0** | Framework web de alto nível |
| **HTML5 / CSS3** | Estruturação e design visual |
| **SQLite** | Banco de dados para ambiente de desenvolvimento |
| **Git / GitHub** | Controle de versão e versionamento de código |

---

## 💻 Como Rodar o Projeto Localmente

### 1. Requisitos Prévios
Certifique-se de ter instalado:
- **Python 3.12** ou superior.
- **pip** (gerenciador de pacotes do Python).
- **Git**.

### 2. Instalação e Configuração

```bash
# Clone o repositório
git clone [https://github.com/Gabrieloliver33/conquistas-diarias.git](https://github.com/Gabrieloliver33/conquistas-diarias.git)
cd conquistas-diarias

# Crie e ative o ambiente virtual
python -m venv venv

# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

# Aplique as migrações ao banco de dados
python manage.py migrate

# Crie um superusuário para o painel administrativo
python manage.py createsuperuser
