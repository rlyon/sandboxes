#!/bin/sh
source $1/functions.sh

FILE="qhull-2012.1-src.tgz"
SRC="http://www.qhull.org/download/qhull-2012.1-src.tgz"
download_unless_present $FILE $SRC
