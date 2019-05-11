#!/bin/bash

target=${2:-"/sdcard/Movies/PC"}
source=${1}

if [ -n "${source}" ]; then
    echo adb push --sync ${source} ${target}
else
    echo "Enter source!"
fi

