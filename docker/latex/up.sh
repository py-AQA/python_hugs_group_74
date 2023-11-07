export USER=stden
export IMAGE=latex
export TAG=latest
echo ===== Build container =====
docker build -t $IMAGE .
echo ===== Tag container =====
docker tag $IMAGE:$TAG $USER/$IMAGE:$TAG
echo ===== Push to https://hub.docker.com/repository/docker/stden/latex =====
docker push $USER/$IMAGE:$TAG