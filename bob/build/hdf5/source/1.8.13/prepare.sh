#!/bin/sh
source $1/functions.sh

FILE="hdf5-1.8.13.tar.gz"
SRC="http://www.hdfgroup.org/ftp/HDF5/current/src/hdf5-1.8.13.tar.gz"
download_unless_present $FILE $SRC
