set USER=stden
set IMAGE=java-run-swing
set TAG=latest
@echo ===== Build container =====
docker build -t %IMAGE% .
@echo ===== Tag container =====
docker tag %IMAGE%:%TAG% %USER%/%IMAGE%:%TAG%
@echo ===== Push to https://hub.docker.com/repository/docker/stden/java-run-swing =====
docker push %USER%/%IMAGE%:%TAG%
@echo ===== Show files in container --rm - remove container =====
docker run --rm %IMAGE% ls /app
@echo ===== Show files tree in container =====
docker run %IMAGE% tree /app
@echo ===== Run container =====
docker run %IMAGE%
