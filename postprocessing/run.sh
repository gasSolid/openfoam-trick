#!/bin/sh

wmake
rm -f *.out
rm -f *.png

./postprocessing

./post.py
