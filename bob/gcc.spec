%define debug_package %{nil}

%define package_name 	gcc
%define package_family	gcc48
%define package_type 	compilers
%define software_path	/opt/software
%define package_path	%{software_path}/%{package_type}/%{package_family}

Summary: Various compilers
Name: %{package_type}-%{package_family}-%{package_name}
Version: 4.8.3
Release: 1%{?dist}
License: GPLv3+ and GPLv3+ with exceptions and GPLv2+ with exceptions
Group: Development/Languages
Source: %{package_name}-%{version}.tar.gz
URL: http://gcc.gnu.org
Vendor: CentOS
Packager: Rob Lyon <rob.lyon@wsu.edu>
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: Lmod
BuildRequires: compilers-%{package_family}-gmp
BuildRequires: compilers-%{package_family}-mpfr
BuildRequires: compilers-%{package_family}-mpc
BuildRequires: compilers-%{package_family}-isl
BuildRequires: compilers-%{package_family}-cloog
BuildRequires: compilers-%{package_family}-zlib
Requires: Lmod
Requires: compilers-%{package_family}-gmp
Requires: compilers-%{package_family}-mpfr
Requires: compilers-%{package_family}-mpc
Requires: compilers-%{package_family}-isl
Requires: compilers-%{package_family}-cloog
Requires: compilers-%{package_family}-zlib

%description
The gcc package contains the GNU Compiler Collection

%prep
%setup -q -n %{package_name}-%{version}

%build
# export PATH=%{package_path}:$PATH
# export LD_LIBRARY_PATH=%{package_path}/lib:$LD_LIBRARY_PATH
# export CFLAGS="-L%{package_path}/lib -I%{package_path}/include %{optflags}"
# export CPPFLAGS="$CFLAGS -pedantic"
# export CXXFLAGS="$CFLAGS -pedantic"
# export LDFLAGS="-L%{package_path}/lib %{optflags}"

mkdir build ; pushd build
export LD_LIBRARY_PATH=%{package_path}/lib

CC="$CC" \
CFLAGS="$OPT_FLAGS -L%{package_path}/lib -I%{package_path}/include" \
CXXFLAGS="`echo " $CFLAGS " | sed 's/ -Wall / /g;s/ -fexceptions / /g' \
	| sed 's/ -Werror=format-security / -Wformat -Werror=format-security /'`" \
../configure 	--prefix=%{package_path} \
				--disable-multilib \
				--enable-shared \
				--enable-__cxa_atexit \
				--enable-checking=release \
				--enable-lto \
				--enable-threads=posix \
				--enable-languages=c,c++,objc,obj-c++,fortran \
				--disable-libunwind-exceptions \
				--disable-libstdcxx-pch \
				--disable-werror \
				--disable-libgcj \
				--disable-libmudflap \
				--disable-nls \
				--with-fpmath=sse \
				--with-system-zlib \
				--with-cpu=generic \
				--with-gmp=%{package_path} \
				--with-mpfr=%{package_path} \
				--with-mpc=%{package_path} \
				--with-isl=%{package_path} \
				--with-cloog=%{package_path} \
				--build=x86_64-redhat-linux
make -j3
popd

%install
# export PATH=%{package_path}:$PATH
# export LD_LIBRARY_PATH=%{package_path}/lib:$LD_LIBRARY_PATH
# export CFLAGS="-L%{package_path}/lib -I%{package_path}/include %{optflags}"
# export CPPFLAGS="$CFLAGS -pedantic"
# export CXXFLAGS="$CFLAGS -pedantic"
# export LDFLAGS="-L%{package_path}/lib %{optflags}"

pushd build
make DESTDIR=%{buildroot} install
rm -rf %{buildroot}/%{package_path}/share/info/dir
popd

# Add cpp and cc links

%files
%defattr(-,root,root)
%{package_path}/bin/c++
%{package_path}/bin/cpp
%{package_path}/bin/g++
%{package_path}/bin/gcc
%{package_path}/bin/gcc-ar
%{package_path}/bin/gcc-nm
%{package_path}/bin/gcc-ranlib
%{package_path}/bin/gcov
%{package_path}/bin/gfortran
%{package_path}/bin/x86_64-redhat-linux-c++
%{package_path}/bin/x86_64-redhat-linux-g++
%{package_path}/bin/x86_64-redhat-linux-gcc
%{package_path}/bin/x86_64-redhat-linux-gcc-4.8.3
%{package_path}/bin/x86_64-redhat-linux-gcc-ar
%{package_path}/bin/x86_64-redhat-linux-gcc-nm
%{package_path}/bin/x86_64-redhat-linux-gcc-ranlib
%{package_path}/bin/x86_64-redhat-linux-gfortran
%{package_path}/include/c++
%{package_path}/lib/gcc
%{package_path}/lib64/libasan.a
%{package_path}/lib64/libasan.la
%{package_path}/lib64/libasan.so
%{package_path}/lib64/libasan.so.0
%{package_path}/lib64/libasan.so.0.0.0
%{package_path}/lib64/libasan_preinit.o
%{package_path}/lib64/libatomic.a
%{package_path}/lib64/libatomic.la
%{package_path}/lib64/libatomic.so
%{package_path}/lib64/libatomic.so.1
%{package_path}/lib64/libatomic.so.1.0.0
%{package_path}/lib64/libgcc_s.so
%{package_path}/lib64/libgcc_s.so.1
%{package_path}/lib64/libgfortran.a
%{package_path}/lib64/libgfortran.la
%{package_path}/lib64/libgfortran.so
%{package_path}/lib64/libgfortran.so.3
%{package_path}/lib64/libgfortran.so.3.0.0
%{package_path}/lib64/libgfortran.spec
%{package_path}/lib64/libgomp.a
%{package_path}/lib64/libgomp.la
%{package_path}/lib64/libgomp.so
%{package_path}/lib64/libgomp.so.1
%{package_path}/lib64/libgomp.so.1.0.0
%{package_path}/lib64/libgomp.spec
%{package_path}/lib64/libiberty.a
%{package_path}/lib64/libitm.a
%{package_path}/lib64/libitm.la
%{package_path}/lib64/libitm.so
%{package_path}/lib64/libitm.so.1
%{package_path}/lib64/libitm.so.1.0.0
%{package_path}/lib64/libitm.spec
%{package_path}/lib64/libobjc.a
%{package_path}/lib64/libobjc.la
%{package_path}/lib64/libobjc.so
%{package_path}/lib64/libobjc.so.4
%{package_path}/lib64/libobjc.so.4.0.0
%{package_path}/lib64/libquadmath.a
%{package_path}/lib64/libquadmath.la
%{package_path}/lib64/libquadmath.so
%{package_path}/lib64/libquadmath.so.0
%{package_path}/lib64/libquadmath.so.0.0.0
%{package_path}/lib64/libssp.a
%{package_path}/lib64/libssp.la
%{package_path}/lib64/libssp.so
%{package_path}/lib64/libssp.so.0
%{package_path}/lib64/libssp.so.0.0.0
%{package_path}/lib64/libssp_nonshared.a
%{package_path}/lib64/libssp_nonshared.la
%{package_path}/lib64/libstdc++.a
%{package_path}/lib64/libstdc++.la
%{package_path}/lib64/libstdc++.so
%{package_path}/lib64/libstdc++.so.6
%{package_path}/lib64/libstdc++.so.6.0.19
%{package_path}/lib64/libstdc++.so.6.0.19-gdb.py
%{package_path}/lib64/libstdc++.so.6.0.19-gdb.pyc
%{package_path}/lib64/libstdc++.so.6.0.19-gdb.pyo
%{package_path}/lib64/libsupc++.a
%{package_path}/lib64/libsupc++.la
%{package_path}/lib64/libtsan.a
%{package_path}/lib64/libtsan.la
%{package_path}/lib64/libtsan.so
%{package_path}/lib64/libtsan.so.0
%{package_path}/lib64/libtsan.so.0.0.0
%{package_path}/libexec/gcc
%{package_path}/share/gcc-4.8.3
%{package_path}/share/info/libgomp.info
%{package_path}/share/info/libitm.info
%{package_path}/share/info/libquadmath.info
%{package_path}/share/man/man1/cpp.1
%{package_path}/share/man/man1/g++.1
%{package_path}/share/man/man1/gcc.1
%{package_path}/share/man/man1/gcov.1
%{package_path}/share/man/man1/gfortran.1
%{package_path}/share/man/man7/fsf-funding.7
%{package_path}/share/man/man7/gfdl.7
%{package_path}/share/man/man7/gpl.7
