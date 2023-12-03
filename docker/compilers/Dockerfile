# Официальный образ Mono как базовый
FROM mono:latest

# LaTeX, компилятор C++ и FreePascal
# Установим команду tree внутрь контейнера
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    texlive texlive-latex-extra texlive-fonts-recommended \
    g++ fp-compiler \
    python3 python-pip \
    tree wget \
    && rm -rf /var/lib/apt/lists/*
RUN wget https://netcologne.dl.sourceforge.net/project/d-apt/files/d-apt.list -O /etc/apt/sources.list.d/d-apt.list
RUN apt-get update --allow-insecure-repositories
RUN apt-get -y --allow-unauthenticated install --reinstall d-apt-keyring
RUN apt-get -y --allow-unauthenticated install dmd-compiler dub

# Дополнительные Python библиотеки если необходимо
RUN pip install --no-cache-dir numpy pandas
# Папка для нашего кода
WORKDIR /x
# Копируем наш код в контейнер
COPY . /x
RUN chmod +x /x/test.sh
# Команда по умолчанию, когда контейнер запускается
CMD /x/test.sh
