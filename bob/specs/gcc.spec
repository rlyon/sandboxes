%define debug_package %{nil}

%define package_name    gcc
%define package_version	4.8.3
%define package_type 	compilers

%define compiler_family		gcc
%define compiler_version 	4.8.3
%define compiler_prefix  	%{package_type}-%{compiler_family}-%{compiler_version}

%define software_path	/opt/software
%define package_path	%{software_path}/%{package_type}/%{compiler_family}/%{compiler_version}


Summary: Various compilers
Name: %{compiler_prefix}-core
Version: %{compiler_version}
Release: 1%{?dist}
License: GPLv3+ and GPLv3+ with exceptions and GPLv2+ with exceptions
Group: Development/Languages
Source: %{package_name}-%{version}.tar.gz
URL: http://gcc.gnu.org
Vendor: CentOS
Packager: Rob Lyon <rob.lyon@wsu.edu>
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: environment-modules
BuildRequires: %{compiler_prefix}-gmp
BuildRequires: %{compiler_prefix}-mpfr
BuildRequires: %{compiler_prefix}-mpc
BuildRequires: %{compiler_prefix}-isl
BuildRequires: %{compiler_prefix}-cloog
BuildRequires: %{compiler_prefix}-zlib
Requires: environment-modules
Requires: %{compiler_prefix}-gmp
Requires: %{compiler_prefix}-mpfr
Requires: %{compiler_prefix}-mpc
Requires: %{compiler_prefix}-isl
Requires: %{compiler_prefix}-cloog
Requires: %{compiler_prefix}-zlib

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
				
				--libdir=%{package_path}/lib \
				--build=%{_arch}-redhat-linux
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
%defattr(-,software,software)
%{package_path}/bin/c++
%{package_path}/bin/cpp
%{package_path}/bin/g++
%{package_path}/bin/gcc
%{package_path}/bin/gcc-ar
%{package_path}/bin/gcc-nm
%{package_path}/bin/gcc-ranlib
%{package_path}/bin/gcov
%{package_path}/bin/gfortran
%{package_path}/bin/%{_arch}-redhat-linux-c++
%{package_path}/bin/%{_arch}-redhat-linux-g++
%{package_path}/bin/%{_arch}-redhat-linux-gcc
%{package_path}/bin/%{_arch}-redhat-linux-gcc-4.8.3
%{package_path}/bin/%{_arch}-redhat-linux-gcc-ar
%{package_path}/bin/%{_arch}-redhat-linux-gcc-nm
%{package_path}/bin/%{_arch}-redhat-linux-gcc-ranlib
%{package_path}/bin/%{_arch}-redhat-linux-gfortran
%{package_path}/include/c++
%{package_path}/lib/gcc
%{package_path}/%{_lib}/libasan.a
%{package_path}/%{_lib}/libasan.la
%{package_path}/%{_lib}/libasan.so
%{package_path}/%{_lib}/libasan.so.0
%{package_path}/%{_lib}/libasan.so.0.0.0
%{package_path}/%{_lib}/libasan_preinit.o
%{package_path}/%{_lib}/libatomic.a
%{package_path}/%{_lib}/libatomic.la
%{package_path}/%{_lib}/libatomic.so
%{package_path}/%{_lib}/libatomic.so.1
%{package_path}/%{_lib}/libatomic.so.1.0.0
%{package_path}/%{_lib}/libgcc_s.so
%{package_path}/%{_lib}/libgcc_s.so.1
%{package_path}/%{_lib}/libgfortran.a
%{package_path}/%{_lib}/libgfortran.la
%{package_path}/%{_lib}/libgfortran.so
%{package_path}/%{_lib}/libgfortran.so.3
%{package_path}/%{_lib}/libgfortran.so.3.0.0
%{package_path}/%{_lib}/libgfortran.spec
%{package_path}/%{_lib}/libgomp.a
%{package_path}/%{_lib}/libgomp.la
%{package_path}/%{_lib}/libgomp.so
%{package_path}/%{_lib}/libgomp.so.1
%{package_path}/%{_lib}/libgomp.so.1.0.0
%{package_path}/%{_lib}/libgomp.spec
%{package_path}/%{_lib}/libiberty.a
%{package_path}/%{_lib}/libitm.a
%{package_path}/%{_lib}/libitm.la
%{package_path}/%{_lib}/libitm.so
%{package_path}/%{_lib}/libitm.so.1
%{package_path}/%{_lib}/libitm.so.1.0.0
%{package_path}/%{_lib}/libitm.spec
%{package_path}/%{_lib}/libobjc.a
%{package_path}/%{_lib}/libobjc.la
%{package_path}/%{_lib}/libobjc.so
%{package_path}/%{_lib}/libobjc.so.4
%{package_path}/%{_lib}/libobjc.so.4.0.0
%{package_path}/%{_lib}/libquadmath.a
%{package_path}/%{_lib}/libquadmath.la
%{package_path}/%{_lib}/libquadmath.so
%{package_path}/%{_lib}/libquadmath.so.0
%{package_path}/%{_lib}/libquadmath.so.0.0.0
%{package_path}/%{_lib}/libssp.a
%{package_path}/%{_lib}/libssp.la
%{package_path}/%{_lib}/libssp.so
%{package_path}/%{_lib}/libssp.so.0
%{package_path}/%{_lib}/libssp.so.0.0.0
%{package_path}/%{_lib}/libssp_nonshared.a
%{package_path}/%{_lib}/libssp_nonshared.la
%{package_path}/%{_lib}/libstdc++.a
%{package_path}/%{_lib}/libstdc++.la
%{package_path}/%{_lib}/libstdc++.so
%{package_path}/%{_lib}/libstdc++.so.6
%{package_path}/%{_lib}/libstdc++.so.6.0.19
%{package_path}/%{_lib}/libstdc++.so.6.0.19-gdb.py
%{package_path}/%{_lib}/libstdc++.so.6.0.19-gdb.pyc
%{package_path}/%{_lib}/libstdc++.so.6.0.19-gdb.pyo
%{package_path}/%{_lib}/libsupc++.a
%{package_path}/%{_lib}/libsupc++.la
# libtsan isn't installed on i386 due to invalid linker internals
%ifarch x86_64
%{package_path}/%{_lib}/libtsan.a
%{package_path}/%{_lib}/libtsan.la
%{package_path}/%{_lib}/libtsan.so
%{package_path}/%{_lib}/libtsan.so.0
%{package_path}/%{_lib}/libtsan.so.0.0.0
%endif
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
