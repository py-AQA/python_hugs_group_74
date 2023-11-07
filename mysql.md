Установка и настройка MySQL на MacOS
====================================

**Установка Homebrew (если у вас его нет)**

Если у вас еще нет Homebrew (популярный пакетный менеджер для MacOS), установите его, выполнив:

```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**Установка MySQL:**

```sh
brew install mysql
```

**Запуск MySQL:**

```sh
brew services start mysql
```

Эта команда автоматически запустит MySQL и настроит его так, чтобы сервер MySQL запускался автоматически при загрузке
вашего компьютера.

По умолчанию MySQL устанавливается без пароля для пользователя root. Чтобы настроить пароль для пользователя root,
выполните следующие команды:

```sh
mysql_secure_installation
```

Во время выполнения этой команды вы можете настроить пароль, удалить анонимных пользователей и т. д.

**Вход в MySQL:**

```sh
mysql -u root -p
```

Остановка MySQl сервера:

```sh
brew services stop mysql
```
