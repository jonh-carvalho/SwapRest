## Passo : Testar as Modificações

### Execute as migrações:

> python manage.py makemigrations
> python manage.py migrate

### Criar superusuário para o django-admin

> python manage.py createsuperuser

### Execute o servidor de desenvolvimento:

> python manage.py runserver

### Acessar o Django-Admin

> localhost:8000/admin

### Acessar a api

> localhost:8000/api/

Agora, o app REST está configurado para usar o modelo User do Django, integrando-o com o modelo Perfil para informações adicionais do usuário.
