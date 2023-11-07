set IMAGE=java-run-swing
@echo ===== Build container =====
docker build -t %IMAGE% .
@echo ===== Run container =====
docker run %IMAGE%
