#!/bin/bash
# RUNS local container
eval `ssh-agent`
ssh-add ~/.ssh/$1

if [ "$2" == "build" ]; then
    docker compose -f local.yml up -d --no-deps --build
else
    docker compose -f local.yml up -d --no-deps
fi
