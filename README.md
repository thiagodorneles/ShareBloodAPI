# ShareBloodAPI

API para ShareBlood

## Requisitos

* virtualenv
* sqlite3

## Ambiente Python

Crie um virtualenv:

    virtualenv env
    source env/bin/activate
    
Após criar o virtualenv e ativar ele, instale as dependências:

    pip install -r requirements
    
Para criar o banco execute:

    python manage.py syncdb
    
E rode as migrações de banco de dados:

    python manage.py migrate
