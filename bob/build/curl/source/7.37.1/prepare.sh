#!/bin/sh
source $1/functions.sh

FILE="curl-7.37.1.tar.gz"
SRC="http://curl.haxx.se/download/curl-7.37.1.tar.gz"
download_unless_present $FILE $SRC
