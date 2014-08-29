#!/bin/sh
source /vagrant/functions.sh

FILE="gmp-4.3.2.tar.gz"
SRC="ftp://ftp.gnu.org/gnu/gmp/gmp-4.3.2.tar.gz"
download_unless_present $FILE $SRC
