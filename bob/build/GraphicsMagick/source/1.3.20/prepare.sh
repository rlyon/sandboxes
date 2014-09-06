#!/bin/sh
source $1/functions.sh

FILE="GraphicsMagick-1.3.20.tar.gz"
SRC="http://downloads.sourceforge.net/project/graphicsmagick/graphicsmagick/1.3.20/GraphicsMagick-1.3.20.tar.gz?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fgraphicsmagick%2Ffiles%2Fgraphicsmagick%2F1.3.20%2F&ts=1409067911&use_mirror=superb-dca3"
download_unless_present $FILE $SRC
