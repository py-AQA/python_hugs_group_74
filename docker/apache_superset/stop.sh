#!/bin/bash
echo -- Останавливаем все запущенные контейнеры --
docker stop $(docker ps -q)