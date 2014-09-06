#!/bin/sh
source $1/functions.sh

FILE="mpc-0.8.1.tar.gz"
SRC="http://www.multiprecision.org/mpc/download/mpc-0.8.1.tar.gz"
download_unless_present $FILE $SRC
