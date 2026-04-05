#!/bin/bash

grep -E "FAILED|DENIED" "$1"
grep -E "FAILED|DENIED" "$1" | wc -l    