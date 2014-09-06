#!/bin/sh
source $1/functions.sh

FILE="atlas3.10.2.tar.bz2"
SRC="http://downloads.sourceforge.net/project/math-atlas/Stable/3.10.2/atlas3.10.2.tar.bz2?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fmath-atlas%2Ffiles%2FStable%2F&ts=1409066288&use_mirror=softlayer-dal"
download_unless_present $FILE $SRC
