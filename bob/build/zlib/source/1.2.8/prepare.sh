#!/bin/sh
source $1/functions.sh

FILE="zlib-1.2.8.tar.gz"
SRC="http://zlib.net/zlib-1.2.8.tar.gz"
download_unless_present $FILE $SRC
