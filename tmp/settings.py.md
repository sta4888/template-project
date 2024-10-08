# Файл настроек Django

## settings.py

тестирование и настройка

по настройке settings.py мы возьмем статью 


### SECRET_KEY
генерация секретного ключа 
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```
или [отсюда](https://djecrety.ir)


https://demoqa.com/
для корректных настроек, лучшие практики говорят о том, чтоб мы настройки разделяли для каждого окружения отдельно



- внутри корневого пакета мы создаем пакет settings
- в нем будут лежать базовые настройки для 
  - тестов (test)
  - прод (prod)
  - разработка (dev)


## варианты
- можно распределить так, и будет вроде бы удобно, но не совсем
- можно просто создавать файлы .env для каждого типа развертывания и будет на много удобнее
- самый базовый вариант, оставить все как есть(но тогда нужно будет для каждого создавать новый файл настроек)
- можно для каждого докеркомпозера прописывать команду запуска ```python manage.py runserver --settings=settings.local``` (что так же не удобно)



В зависимости от вашей среды вам может потребоваться настроить ряд параметров :

- ```STATIC_URL``` : URL, по которому пользователь может получить доступ к вашим статическим файлам в браузере. Значение по умолчанию — /static/, что означает, что ваши файлы будут доступны http://127.0.0.1:8000/static/в режиме разработки — например, http://127.0.0.1:8000/static/css/main.css.
- ```STATIC_ROOT``` : Абсолютный путь к каталогу, из которого ваше приложение Django будет обслуживать ваши статические файлы. Когда вы запускаете команду управления collectstatic (подробнее об этом чуть позже), она найдет все статические файлы и скопирует их в этот каталог.
- ```STATICFILES_DIRS``` : По умолчанию статические файлы хранятся на уровне приложения в <APP_NAME>/static/. Команда collectstatic будет искать статические файлы в этих каталогах. Вы также можете указать Django искать статические файлы в дополнительных местах с помощью STATICFILES_DIRS.
- ```STORAGES``` : Он определяет способ настройки различных бэкэндов хранения для управления файлами. Каждому бэкэнду хранения может быть назначен псевдоним, и есть два специальных псевдонима: defaultдля управления файлами (с использованием FileSystemStorageв качестве механизма хранения по умолчанию) и staticfilesдля управления статическими файлами (использование StaticFilesStorageпо умолчанию).
- ```STATICFILES_FINDERS``` : Этот параметр определяет бэкэнды поиска файлов, которые будут использоваться для автоматического поиска статических файлов. По умолчанию используются FileSystemFinderи искатели:AppDirectoriesFinder
- ```FileSystemFinder```- использует STATICFILES_DIRSнастройку для поиска файлов.
- ```AppDirectoriesFinder```- ищет файлы в «статической» папке в каждом приложении Django в проекте.
все подробные объяснения хранятся [здесь](https://testdriven.io/blog/django-static-files/).