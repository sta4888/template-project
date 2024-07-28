
- статус о гите
```shell
git status
```

- добавление в гит файла
```shell
git add .
```

- убираем из гит файл
```shell
git reset <путь/имя.файла>
```

- делаем коммит
```shell
git commit -m "message"
```

- отправлем все закоммиченное в гитхаб
```shell
git push
```

- получаем все закоммиченное с гит
```shell
git pull
```

- вывод веток
```shell
git branch
```

- вывод только текущей ветки
```shell
git symbolic-ref --short HEAD
```
или
```shell
git branch | grep \* | cut -d ' ' -f2
```

- создаем новую ветку
```shell
git branch <new branch>
```
- переключаемся на другую ветку
```shell
git checkout <new branch>
```
- создаем и переключаемся на новую ветку
```shell
git checkout -b <new branch>
```

## .gitignore

с файлом .gitignore работаем так:

