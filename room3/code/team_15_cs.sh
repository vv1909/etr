#!/bin/bash


if [ -z "$1" ]; then
    echo "pass file as an argument"
    exit 1
fi

file="$1"

if [ ! -f "$file" ]; then
    echo "no such file"
    exit 1
fi


grep -E "FAILED|DENIED" "$file"

count=$(grep -E "FAILED|DENIED" "$file" | wc -l)

echo "found $count entries"