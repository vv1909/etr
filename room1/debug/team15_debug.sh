#!/bin/bash


if [ -z "$1" ]; then
    echo "Error. Pass file path as an argument"
    exit 1
fi

cat "$1"