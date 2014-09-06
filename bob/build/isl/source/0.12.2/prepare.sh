#!/bin/sh
source $1/functions.sh

FILE="isl-0.12.2.tar.gz"
SRC="http://isl.gforge.inria.fr/isl-0.12.2.tar.gz"
download_unless_present $FILE $SRC
