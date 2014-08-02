# GCC Build

wget http://www.netgull.com/gcc/releases/gcc-4.9.1/gcc-4.9.1.tar.gz
wget ftp://ftp.gnu.org/gnu/gmp/gmp-4.3.2.tar.gz
wget http://www.mpfr.org/mpfr-2.4.2/mpfr-2.4.2.tar.gz
wget http://www.multiprecision.org/mpc/download/mpc-0.8.1.tar.gz
wget http://ftp.gnu.org/gnu/binutils/binutils-2.24.tar.gz
wget http://isl.gforge.inria.fr/isl-0.12.2.tar.gz
wget http://www.bastoul.net/cloog/pages/download/count.php3?url=./cloog-0.18.1.tar.gz

### Requirements

* ISO C++98 compiler
* C standard library and headers
* GNAT
* Newer binutils?
* make sure to disable java
* GMP >= 4.3.2
* MPFR >= 2.4.2
* MPC >= 0.8.1
* ISL >= 0.12.2
* CLooG >= 0.18.1 (built against isl --with-isl=system)

### Configure
cd build
../configure --prefix=/opt/software/compilers/gcc/4.9.2 \
--disable-multilib \
--without-multilib-list \
--enable-shared \
--enable-bootstrap \
--with-system-zlib \
--mandir=/opt/software/compilers/gcc/4.9.2/man \
--infodir=/opt/software/compilers/gcc/4.9.2/info \
--enable-threads=posix \
--enable-languages=c,c++,objc,obj-c++,fortran \
--disable-libunwind-exceptions \
--enable-gnu-unique-object \
--enable-lto \
--disable-libgcj \
--enable-__cxa_atexit \
--enable-checking=release \
--with-cpu=generic \
--with-cloog \
--build=x86_64-redhat-linux


--with-gmp=/opt/software/compilers/gcc/4.9.2 \
--with-mpfr=/opt/software/compilers/gcc/4.9.2 \
--with-mpc=/opt/software/compilers/gcc/4.9.2 \
--with-islc=/opt/software/compilers/gcc/4.9.2 \
--with-cloog=/opt/software/compilers/gcc/4.9.2 \

--with-gmp-include=/opt/software/compilers/gcc/4.9.2/include
--with-gmp-lib=/opt/software/compilers/gcc/4.9.2/lib
--with-mpfr-include=/opt/software/compilers/gcc/4.9.2/include
--with-mpfr-lib=/opt/software/compilers/gcc/4.9.2/lib
--with-mpc-include=/opt/software/compilers/gcc/4.9.2/include
--with-mpc-lib=/opt/software/compilers/gcc/4.9.2/lib