#!/bin/bash

#DEST="./public_html"
#html=".html"
#mkdir -p "$DEST/"
#
#for f in *; 
#do
#    cat $f > "$DEST/$f";
#    echo "Processing $f file..";
#done
#
#for f in *.php; 
#do
#    php $f | sed 's:\(<a.*href=".*\)\.php\(".*</a>\):\1\.html\2:g' > "$DEST/${f/.php/$html}";
#    echo "Processing $f into ${f/.php/$html}..";
#done

#pip install -r requirements.txt

#python index.py ./

python generate-index.py

echo "Process complete." ;