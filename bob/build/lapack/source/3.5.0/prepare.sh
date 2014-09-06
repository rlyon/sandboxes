#!/bin/sh
source $1/functions.sh

FILE="lapack-3.5.0.tgz"
SRC="http://www.netlib.org/lapack/lapack-3.5.0.tgz"
download_unless_present $FILE $SRC
