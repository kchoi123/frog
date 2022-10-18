#!/bin/bash

# This will build your dockerfile inside docker_build directory

date_now=$(date "+%F-%H-%M-%S")

docker build ../docker_build/ -t kchoijfrog.jfrog.io/jfrog/temp:$date_now

# This will store a temp image in jfrog artifactory (backup)

echo Be sure to authenticate to your jfrog instance!!!

docker login -u k3vinch0i@gmail.com kchoijfrog.jfrog.io

docker push kchoijfrog.jfrog.io/jfrog/temp:$date_now

echo ====== Build Finished ========