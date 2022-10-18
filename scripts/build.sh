#!/bin/bash

# This will build your dockerfile inside docker_build directory

docker build ../docker_build/Dockerfile -t myservice:latest

# This will store a temp image in jfrog artifactory

date_now=$(date "+%F-%H-%M-%S")

docker tag myservice:latest kchoijfrog.jfrog.io/jfrog/temp:$date_now

echo ====== Build Finished ========