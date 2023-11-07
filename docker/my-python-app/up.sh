#!/bin/bash
export USER=stden
export IMAGE=my-python-app
export TAG=latest
echo ===== Build container =====
docker build -t $IMAGE .
echo ===== Tag container =====
docker tag $IMAGE:$TAG $USER/$IMAGE:$TAG
echo ===== Push to https://hub.docker.com/repository/docker/stden/my-python-app =====
docker push $USER/$IMAGE:$TAG
echo ===== Show files in container --rm - remove container =====
docker run --rm $IMAGE ls /x
echo ===== Show files tree in container =====
docker run $IMAGE tree /x
echo ===== Run container =====
docker run $IMAGE
