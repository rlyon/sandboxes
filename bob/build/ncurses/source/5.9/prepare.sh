#!/bin/sh
source $1/functions.sh

FILE="ncurses.tar.gz"
SRC="ftp://invisible-island.net/ncurses/ncurses.tar.gz"
download_unless_present $FILE $SRC
