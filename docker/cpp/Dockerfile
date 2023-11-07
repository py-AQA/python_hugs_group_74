# Официальный образ GNU C++ как базовый
FROM gcc:latest

# Компилятор C++
RUN apt-get update && \
    apt-get install -y git cmake g++ libboost-filesystem1.81.0 gcovr lcov valgrind tree
# Не работает последняя версия libboost-filesystem1.83.0