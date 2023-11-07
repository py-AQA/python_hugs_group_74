@echo ===== Run Tetris =====
set PORT=81
docker run -d -p %PORT%:80 --name tetris bsord/tetris
@echo ===== Open http://localhost:80 =====
start chrome "http://localhost:%PORT%"


