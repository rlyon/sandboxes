#!/bin/sh
source /vagrant/functions.sh

FILE="ncurses-5.9.tar.gz"
SRC="http://ftp.gnu.org/pub/gnu/ncurses/ncurses-5.9.tar.gz"
download_unless_present $FILE $SRC
