#!/bin/sh
source $1/functions.sh

FILE="MesaLib-10.2.2.tar.gz"
SRC="ftp://ftp.freedesktop.org/pub/mesa/10.2.2/MesaLib-10.2.2.tar.gz"
download_unless_present $FILE $SRC
