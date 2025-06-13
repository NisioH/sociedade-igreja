# sociedade-igreja

# 📌 Sistema de Gestão de Sociedades da Igreja

Este é um aplicativo para **gerenciar programações das sociedades** da igreja, permitindo organização eficiente de eventos e membros.

## 🚀 Tecnologias Utilizadas
- **Back-end:** Django + Django REST Framework
- **Front-end:** Flet (para app mobile e web)
- **Banco de Dados:** SQLite (inicialmente) → PostgreSQL (futuramente)
- **Autenticação:** Firebase (Google/Facebook) + JWT (login manual)
- **Hospedagem:** Railway (API) + Vercel (Front-end)

## 📌 Funcionalidades
✅ Cadastro e gerenciamento de sociedades (UPA, UMP, SAF, UPH, UCP, CONSELHO)  
✅ Sistema de permissões (Presidente, Vice, Secretários, Membros)  
✅ Autenticação via Google/Facebook e login manual  
✅ Gestão de eventos mensais para cada sociedade  
✅ Notificações para lembrar eventos futuros  

## 🔧 Como Rodar o Projeto
### 1️⃣ **Clone o repositório**
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py runserver
