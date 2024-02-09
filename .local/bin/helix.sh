#!/bin/bash
set -eu

path=$(pwd)

if [ -n "${1:-}" ]; then
    cd ~ || exit 1
    if [[ "$1" == \~* || "$1" == /home/vid* || "$1" == "$HOME"* ]]; then
        helix "$1"
    else
        helix "$path/$1"
    fi
else
    cd ~ || exit 1
    helix "$path"
fi

cd "$path" || exit 1
