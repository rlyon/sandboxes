#!/bin/sh
source $1/functions.sh

FILE="glpk-4.55.tar.gz"
SRC="http://ftp.gnu.org/gnu/glpk/glpk-4.55.tar.gz"
download_unless_present $FILE $SRC
