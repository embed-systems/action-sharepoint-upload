#!/bin/sh -l

python main.py
[ $? -eq 0 ]  || exit 1
