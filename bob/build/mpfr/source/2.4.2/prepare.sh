#!/bin/sh
source $1/functions.sh

FILE="mpfr-2.4.2.tar.gz"
SRC="http://www.mpfr.org/mpfr-2.4.2/mpfr-2.4.2.tar.gz"
download_unless_present $FILE $SRC
