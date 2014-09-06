#!/bin/sh
source $1/functions.sh

FILE="qt-everywhere-opensource-src-5.3.1.tar.gz"
SRC="http://download.qt-project.org/official_releases/qt/5.3/5.3.1/single/qt-everywhere-opensource-src-5.3.1.tar.gz"
download_unless_present $FILE $SRC
