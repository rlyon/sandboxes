#!/bin/sh
source $1/functions.sh

FILE="pcre-8.35.tar.gz"
SRC="ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre-8.35.tar.gz"
download_unless_present $FILE $SRC
