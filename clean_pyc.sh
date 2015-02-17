#!/bin/sh
#
# Usage:
# Delele *.pyc *py-e and __pycache__ files recursively in the current directory:
# $ pyc  
# 
 
if [ "$1" ]; then
    WHERE="$1"
else
    WHERE="$PWD"
fi
 
find "$WHERE" \
    -name '__pycache__' -delete -print \
    -o \
    -name '*.pyc' -delete -print \
    -o \
    -name '*.py-e' -delete -print
