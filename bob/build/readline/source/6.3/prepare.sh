#!/bin/sh
source $1/functions.sh

FILE="readline-6.3.tar.gz"
SRC="ftp://ftp.cwru.edu/pub/bash/readline-6.3.tar.gz"
download_unless_present $FILE $SRC
