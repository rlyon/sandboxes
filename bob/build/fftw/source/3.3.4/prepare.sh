#!/bin/sh
source $1/functions.sh

FILE="fftw-3.3.4.tar.gz"
SRC="http://www.fftw.org/fftw-3.3.4.tar.gz"
download_unless_present $FILE $SRC
