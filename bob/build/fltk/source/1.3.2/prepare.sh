#!/bin/sh
source $1/functions.sh

FILE="fltk-1.3.2-source.tar.gz"
SRC="http://www.fltk.org/software.php?VERSION=1.3.2&FILE=fltk/1.3.2/fltk-1.3.2-source.tar.gz"
download_unless_present $FILE $SRC
