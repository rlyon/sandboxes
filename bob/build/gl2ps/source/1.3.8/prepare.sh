#!/bin/sh
source $1/functions.sh

FILE="gl2ps-1.3.8.tgz"
SRC="http://geuz.org/gl2ps/src/gl2ps-1.3.8.tgz"
download_unless_present $FILE $SRC
