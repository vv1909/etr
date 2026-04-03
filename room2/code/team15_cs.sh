#!/bin/bash

if [ -z "$1" ]; then
    echo "pass s file as an argument.."
    exit 1
fi

if [ ! -f "$1" ]; then
    touch "$1"
fi

chmod 600 "$1"
ls -l "$1"