# Используем официальный образ Python как родительский образ
FROM python:latest
# Установим команду tree внутрь контейнера
RUN apt-get update && apt-get install -y tree
# Установим рабочий каталог ВНУТРИ контейнера
WORKDIR /x
# Скопируем файл с зависимостями в рабочий каталог
COPY requirements.txt ./
# Установим все необходимые библиотеки из файла requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Копируем файл скрипта в рабочую директорию
COPY my-test.py ./
# Скопируем содержимое локального каталога в рабочий каталог контейнера
# Скопируем все файлы из текущего каталога (где мы собираем контейнер) в WORKDIR внутри
COPY . .
# Команда, которая будет выполнена при запуске контейнера
#CMD ["python", "./my-test.py"]
#CMD python ./my-test.py
CMD ./my-test.py
