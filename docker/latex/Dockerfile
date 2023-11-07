FROM fermiumlabs/latex-docker:latest

RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN apt-get update -qq && apt-get install -y -qq sshpass
# Компилятор C++
RUN apt-get update && \
    apt-get install -y git cmake g++ libboost-filesystem1.81.0 gcovr lcov valgrind tree
# Не работает последняя версия libboost-filesystem1.83.0