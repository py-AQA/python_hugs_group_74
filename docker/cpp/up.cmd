set USER=stden
set IMAGE=cpp
set TAG=latest
@echo ===== Build container =====
docker build -t %IMAGE% .
@echo ===== Tag container =====
docker tag %IMAGE%:%TAG% %USER%/%IMAGE%:%TAG%
@echo ===== Push to https://hub.docker.com/repository/docker/stden/cpp =====
docker push %USER%/%IMAGE%:%TAG%
