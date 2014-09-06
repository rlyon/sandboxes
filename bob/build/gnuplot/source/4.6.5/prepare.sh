#!/bin/sh
source $1/functions.sh

FILE="gnuplot-4.6.5.tar.gz"
SRC="http://downloads.sourceforge.net/project/gnuplot/gnuplot/4.6.5/gnuplot-4.6.5.tar.gz?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fgnuplot%2Ffiles%2F&ts=1409067815&use_mirror=softlayer-dal"
download_unless_present $FILE $SRC
