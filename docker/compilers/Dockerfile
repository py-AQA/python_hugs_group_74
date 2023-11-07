# Официальный образ Python как базовый
FROM python:latest

# LaTeX, компилятор C++ и FreePascal
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    texlive \
    texlive-latex-extra \
    texlive-fonts-recommended \
    g++ \
    fp-compiler \
    && rm -rf /var/lib/apt/lists/*

# Дополнительные Python библиотеки если необходимо
RUN pip install --no-cache-dir numpy pandas
# Установим команду tree внутрь контейнера
RUN apt-get update && apt-get install -y tree
# Папка для нашего кода
WORKDIR /x
# Копируем наш код в контейнер
COPY . /x
RUN chmod +x /x/test.sh
# Команда по умолчанию, когда контейнер запускается
CMD /x/test.sh
