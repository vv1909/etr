#!/bin/bash


if [ -z "$1" ]; then
    read -e -p "Enter file path: " file
else
    file="$1"
fi

grep -o "failed" "$file" | wc -l