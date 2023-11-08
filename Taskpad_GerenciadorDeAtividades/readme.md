### Passo a passo para rodar o projeto:

1. Crie seu ambiente virtual:

```bash
python -m venv venv
```

2. Ative seu venv:

```bash
# Linux:
source venv/bin/activate

# Windows:
.\venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Crie o arquivo .env:

```bash
# Linux:
cp .env.example .env

# Windows:
copy .env.example .env
```

Configure o arquivo .env com suas variáveis de ambiente.

5. Rode as migrações:

```bash
python manage.py makemigrations
python manage.py migrate
```

6. Rode o servidor:

```bash
python manage.py runserver
```
