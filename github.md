GitHub
------

**Регистрация на GitHub:**

* Откройте сайт GitHub https://github.com
* Создайте аккаунт: Нажмите на кнопку "Sign up" (Зарегистрироваться) в правом верхнем углу страницы. Заполните
  необходимые данные:
    * имя пользователя
    * электронную почту
    * пароль
    * выберите план (бесплатный или платный)
* Подтвердите адрес электронной почты:
  GitHub отправит e-mail с подтверждением на указанный вами. Перейдите по ссылке в письме, чтобы подтвердить свой
  аккаунт.

**Создание репозитория и загрузка проекта:**

* Создайте новый репозиторий:
    * После успешной регистрации и входа на GitHub, нажмите на кнопку **New** (Создать) в верхнем меню.
    * Затем выберите **Repository** (Репозиторий)
* Заполните данные о репозитории:
    * Введите имя репозитория, описание и выберите настройки видимости (публичный или приватный)
    * Вы также можете выбрать опции для инициализации README-файла, лицензии и файлов .gitignore.
* Клонируйте репозиторий на свой компьютер:
    * После создания репозитория, скопируйте URL репозитория.
    * Откройте терминал (или командную строку), перейдите в папку, где хотите хранить проект, и выполните команду:

Для генерации ключей прямо в командной строке должна работать команда:

```shell
ssh-keygen -t rsa -b 4096 -C "super.denis@gmail.com"
```

В процессе генерации просто нажимаешь Enter много до конца и вывод должен быть примерно таким:

```shell
Generating public/private rsa key pair.
Enter file in which to save the key (C:\Users\denis.stepulenok/.ssh/id_rsa):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in C:\Users\denis.stepulenok/.ssh/id_rsa.
Your public key has been saved in C:\Users\denis.stepulenok/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:ASR9badqoOdCQ1xV4famC2+ZXK7pgWtHdrb4mxf5SdQ super.denis@gmail.com
The key's randomart image is:
+---[RSA 4096]----+
|    .oo..oo.     |
|     .o...o .    |
|   . . ...oo    .|
|    o .  o..   .E|
|   . . .S.  o .. |
|    + . o.oo+ o. |
|   . + .o+oO ..o.|
|    . . .+B+o....|
|     . ..+*o+o   |
+----[SHA256]-----+
```

Вывод ключа:

```shell
cat ~/.ssh/id_rsa.pub
```

Затем копируем текст из файла C:\Users\denis.stepulenok\.ssh\id_rsa.pub на сайт GitLab

И используем SSH ссылки на репозиторий, ссылка выглядит так:
ssh://git@gitlab.com/stden/my_project.git

```shell
git clone <URL_репозитория>
```

**Добавьте исходный код**
Поместите файлы своего проекта в склонированную папку. Затем в терминале перейдите в эту папку и выполните команды:

```shell
git add .
git commit -m "Первый коммит"
git push origin master
```

**Исправление коммитов**

Как редактировать коммиты в TortoiseGit?

Скачать https://tortoisegit.org/download
