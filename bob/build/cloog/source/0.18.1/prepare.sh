#!/bin/sh
source $1/functions.sh

FILE="cloog-0.18.1.tar.gz"
SRC="http://www.bastoul.net/cloog/pages/download/count.php3?url=./cloog-0.18.1.tar.gz"
download_unless_present $FILE $SRC
