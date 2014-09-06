#!/bin/sh
source /vagrant/bin/functions.sh

NAME="gcc"
VERSION="4.8.3"
FILE="gcc-4.8.3.tar.gz"
SRC="http://www.netgull.com/gcc/releases/gcc-4.8.3/gcc-4.8.3.tar.gz"
dir_init $NAME $VERSION $FILE $SRC

NAME="mpfr"
VERSION="2.4.2"
FILE="mpfr-2.4.2.tar.gz"
SRC="http://www.mpfr.org/mpfr-2.4.2/mpfr-2.4.2.tar.gz"
dir_init $NAME $VERSION $FILE $SRC

NAME="mpc"
VERSION="0.8.1"
FILE="mpc-0.8.1.tar.gz"
SRC="http://www.multiprecision.org/mpc/download/mpc-0.8.1.tar.gz"
dir_init $NAME $VERSION $FILE $SRC

NAME="isl"
VERSION="0.12.2"
FILE="isl-0.12.2.tar.gz"
SRC="http://isl.gforge.inria.fr/isl-0.12.2.tar.gz"
dir_init $NAME $VERSION $FILE $SRC

NAME="cloog"
VERSION="0.18.1"
FILE="cloog-0.18.1.tar.gz"
SRC="http://www.bastoul.net/cloog/pages/download/count.php3?url=./cloog-0.18.1.tar.gz"
dir_init $NAME $VERSION $FILE $SRC

NAME="zlib"
VERSION="1.2.8"
FILE="zlib-1.2.8.tar.gz"
SRC="http://zlib.net/zlib-1.2.8.tar.gz"
dir_init $NAME $VERSION $FILE $SRC

BLAS="3.5.0"
VERISON="3.5.0"
FILE="blas.tgz"
SRC="http://www.netlib.org/blas/blas.tgz"
dir_init $NAME $VERSION $FILE $SRC

NAME="atlas"
VERSION="3.10.2"
FILE="atlas3.10.2.tar.bz2"
SRC="http://downloads.sourceforge.net/project/math-atlas/Stable/3.10.2/atlas3.10.2.tar.bz2?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fmath-atlas%2Ffiles%2FStable%2F&ts=1409066288&use_mirror=softlayer-dal"
dir_init $NAME $VERSION $FILE $SRC

NAME="lapack"
VERSION="3.5.0"
FILE="lapack-3.5.0.tgz"
SRC="http://www.netlib.org/lapack/lapack-3.5.0.tgz"
dir_init $NAME $VERSION $FILE $SRC

NAME="pcre"
VERSION="8.35"
FILE="pcre-8.35.tar.gz"
SRC="ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre-8.35.tar.gz"
dir_init $NAME $VERSION $FILE $SRC

NAME="readline"
VERSION="6.3"
FILE="readline-6.3.tar.gz"
SRC="ftp://ftp.cwru.edu/pub/bash/readline-6.3.tar.gz"
dir_init $NAME $VERSION $FILE $SRC

NAME="arpack-ng"
VERSION="3.1.5"
FILE="arpack-ng_3.1.5.tar.gz"
SRC="http://forge.scilab.org/index.php/p/arpack-ng/downloads/get/arpack-ng_3.1.5.tar.gz"
dir_init $NAME $VERSION $FILE $SRC

NAME="curl"
VERSION="7.37.1"
FILE="curl-7.37.1.tar.gz"
SRC="http://curl.haxx.se/download/curl-7.37.1.tar.gz"
dir_init $NAME $VERSION $FILE $SRC

NAME="fftw"
VERSION="3.3.4"
FILE="fftw-3.3.4.tar.gz"
SRC="http://www.fftw.org/fftw-3.3.4.tar.gz"
dir_init $NAME $VERSION $FILE $SRC

NAME="fltk"
VERSION="1.3.2"
FILE="fltk-1.3.2-source.tar.gz"
SRC="http://www.fltk.org/software.php?VERSION=1.3.2&FILE=fltk/1.3.2/fltk-1.3.2-source.tar.gz"
dir_init $NAME $VERSION $FILE $SRC

NAME="fontconfig"
VERSION="2.11.1"
FILE="fontconfig-2.11.1.tar.gz"
SRC="http://www.freedesktop.org/software/fontconfig/release/fontconfig-2.11.1.tar.gz"
dir_init $NAME $VERSION $FILE $SRC

NAME="glpk"
VERSION="4.55"
FILE="glpk-4.55.tar.gz"
SRC="http://ftp.gnu.org/gnu/glpk/glpk-4.55.tar.gz"
dir_init $NAME $VERSION $FILE $SRC

NAME="gl2ps"
VERSION="1.3.8"
FILE="gl2ps-1.3.8.tgz"
SRC="http://geuz.org/gl2ps/src/gl2ps-1.3.8.tgz"
dir_init $NAME $VERSION $FILE $SRC

NAME="gnuplot"
VERSION="4.6.5"
FILE="gnuplot-4.6.5.tar.gz"
SRC="http://downloads.sourceforge.net/project/gnuplot/gnuplot/4.6.5/gnuplot-4.6.5.tar.gz?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fgnuplot%2Ffiles%2F&ts=1409067815&use_mirror=softlayer-dal"
dir_init $NAME $VERSION $FILE $SRC

NAME="GraphicsMagick"
VERSION="1.3.20"
FILE="GraphicsMagick-1.3.20.tar.gz"
SRC="http://downloads.sourceforge.net/project/graphicsmagick/graphicsmagick/1.3.20/GraphicsMagick-1.3.20.tar.gz?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fgraphicsmagick%2Ffiles%2Fgraphicsmagick%2F1.3.20%2F&ts=1409067911&use_mirror=superb-dca3"
dir_init $NAME $VERSION $FILE $SRC

NAME="hdf5"
VERSION="1.8.13"
FILE="hdf5-1.8.13.tar.gz"
SRC="http://www.hdfgroup.org/ftp/HDF5/current/src/hdf5-1.8.13.tar.gz"
dir_init $NAME $VERSION $FILE $SRC

NAME="MesaLib"
VERSION="10.2.2"
FILE="MesaLib-10.2.2.tar.gz"
SRC="ftp://ftp.freedesktop.org/pub/mesa/10.2.2/MesaLib-10.2.2.tar.gz"
dir_init $NAME $VERSION $FILE $SRC

NAME="qhull"
VERSION="2012.1"
FILE="qhull-2012.1-src.tgz"
SRC="http://www.qhull.org/download/qhull-2012.1-src.tgz"
dir_init $NAME $VERSION $FILE $SRC

NAME="qrupdate"
VERSION="1.1.2"
FILE="qrupdate-1.1.2.tar.gz"
SRC="http://downloads.sourceforge.net/project/qrupdate/qrupdate/1.2/qrupdate-1.1.2.tar.gz?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fqrupdate%2F&ts=1409072545&use_mirror=iweb"
dir_init $NAME $VERSION $FILE $SRC

NAME="QScintilla"
VERSION="2.8.3"
FILE="QScintilla-gpl-2.8.3.tar.gz"
SRC="http://sourceforge.net/projects/pyqt/files/QScintilla2/QScintilla-2.8.3/QScintilla-gpl-2.8.3.tar.gz"
dir_init $NAME $VERSION $FILE $SRC

NAME="qt"
VERSION="5.3.1"
FILE="qt-everywhere-opensource-src-5.3.1.tar.gz"
SRC="http://download.qt-project.org/official_releases/qt/5.3/5.3.1/single/qt-everywhere-opensource-src-5.3.1.tar.gz"
dir_init $NAME $VERSION $FILE $SRC

# FILE=""
# SRC=""
# download_unless_present $FILE $SRC

# http://glaros.dtc.umn.edu/gkhome/fetch/sw/metis/metis-5.1.0.tar.gz
# http://github.com/xianyi/OpenBLAS/tarball/v0.2.11
# https://www.tacc.utexas.edu/documents/13601/b58aeb8c-9d8d-4ec2-b5f1-5a5843b4d47b
