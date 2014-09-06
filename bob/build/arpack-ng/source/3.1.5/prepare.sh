#!/bin/sh
source $1/functions.sh

FILE="arpack-ng_3.1.5.tar.gz"
SRC="http://forge.scilab.org/index.php/p/arpack-ng/downloads/get/arpack-ng_3.1.5.tar.gz"
download_unless_present $FILE $SRC
