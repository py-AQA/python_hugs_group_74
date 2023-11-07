set IMAGE=my-python-app
@echo ===== Build container =====
docker build -t %IMAGE% .
@echo ===== Run container =====
docker run %IMAGE%
