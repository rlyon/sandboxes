#!/bin/sh
source $1/functions.sh

FILE="gcc-4.8.3.tar.gz"
SRC="http://www.netgull.com/gcc/releases/gcc-4.8.3/gcc-4.8.3.tar.gz"
download_unless_present $FILE $SRC
