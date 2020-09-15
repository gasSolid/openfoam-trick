#!/bin/sh

rm -f *.data
rm -f *.png
rm -f *.pdf

./cut_data_Flu.sh

./post_Flu.py
