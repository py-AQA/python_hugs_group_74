#!/bin/bash
echo ===== Run Tetris =====
export PORT=81
docker run -d -p $PORT:80 --name tetris bsord/tetris
echo ===== Open http://localhost:80 =====
open "http://localhost:$PORT"


