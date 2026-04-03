#!/bin/bash

touch "$1"
chown "$(whoami)" "$1"
chmod 600 "$1"