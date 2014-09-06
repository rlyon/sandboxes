#!/bin/sh
source $1/functions.sh

FILE="qrupdate-1.1.2.tar.gz"
SRC="http://downloads.sourceforge.net/project/qrupdate/qrupdate/1.2/qrupdate-1.1.2.tar.gz?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fqrupdate%2F&ts=1409072545&use_mirror=iweb"
download_unless_present $FILE $SRC
