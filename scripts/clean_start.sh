#!/bin/bash

docker version

docker ps -a

docker images

echo ============================================

docker stop $(docker ps -a -q)

docker rm $(docker ps -a -q)

docker rmi $(docker images -q)

docker system prune -f

echo ----- clean docker -----

date_now=$(date "+%F-%H-%M-%S")

echo "Your Docker environment is clean as of " $date_now