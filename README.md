# Conquistas Diárias

Aplicação web full-stack desenvolvida com **Django**, voltada para o gerenciamento de conquistas diárias pessoais.  
O sistema permite que usuários cadastrados criem, visualizem, editem e excluam suas próprias conquistas, com autenticação e controle de acesso.

---

## Funcionalidades

- Cadastro e autenticação de usuários
- CRUD completo de conquistas
- Associação de conquistas ao usuário logado
- Interface em português
- Layout moderno com CSS customizado
- Proteção de rotas (login obrigatório)
- Separação clara entre backend e frontend

---

## Tecnologias Utilizadas

- **Python 3.12.10**
- **Django 6.0**
- HTML5
- CSS3
- SQLite (ambiente de desenvolvimento)
- Git e GitHub

---

## Requisitos

Antes de começar, você precisa ter instalado:

- **Python 3.12 ou superior**
- **pip** (já incluso no Python)
- **Git**

## Verifique as versões

```bash
python --version
pip --version
git --version


---

## Como rodar o projeto localmente

git clone https://github.com/SEU-USUARIO/conquistas-diarias.git
cd conquistas-diarias

---

## Criar e ativar o ambiente virtual

python -m venv venv
venv\Scripts\activate

---

## Instalar as dependências

pip install -r requirements.txt

---

## Aplicar as migrações

python manage.py migrate

---

## Criar um superusuário

python manage.py createsuperuser

---

## Iniciar o servidor

python manage.py runserver

http://127.0.0.1:8000

Área administrativa:

http://127.0.0.1:8000/admin
