#!/bin/sh
source $1/functions.sh

FILE="fontconfig-2.11.1.tar.gz"
SRC="http://www.freedesktop.org/software/fontconfig/release/fontconfig-2.11.1.tar.gz"
download_unless_present $FILE $SRC
