#!/bin/sh
source $1/functions.sh

FILE="QScintilla-gpl-2.8.3.tar.gz"
SRC="http://sourceforge.net/projects/pyqt/files/QScintilla2/QScintilla-2.8.3/QScintilla-gpl-2.8.3.tar.gz"
download_unless_present $FILE $SRC
