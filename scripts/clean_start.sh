#!/bin/bash

docker version

docker ps -a

docker images

echo ============================================

docker stop $(docker ps -a -q)

docker rm $(docker ps -a -q)

docker rmi $(docker images -q)

echo ----- clean docker -----

date_now=$(date "+%F-%H-%M-%S")

echo $date_now