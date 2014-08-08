%define package_name 	mpfr
%define package_family	gcc48
%define package_type 	compilers
%define software_path	/opt/software
%define package_path	%{software_path}/%{package_type}/%{package_family}

Summary: A C library for multiple-precision floating-point computations
Name: %{package_type}-%{package_family}-%{package_name}
Version: 2.4.2
Release: 1%{?dist}
License: LGPLv2+ and GPLv2+ and GFDL
Group: System Environment/Libraries
Source: %{package_name}-%{version}.tar.gz
URL: http://www.mpfr.org/
Vendor: CentOS
Packager: Rob Lyon <rob.lyon@wsu.edu>
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: Lmod
BuildRequires: compilers-%{package_family}-gmp
Requires: Lmod
Requires: compilers-%{package_family}-gmp

%description
The MPFR library is a C library for multiple-precision floating-point
computations with "correct rounding". The MPFR is efficient and
also has a well-defined semantics. It copies the good ideas from the
ANSI/IEEE-754 standard for double-precision floating-point arithmetic
(53-bit mantissa). MPFR is based on the GMP multiple-precision library.

%prep
%setup -q -n %{package_name}-%{version}

%build
mkdir build ; pushd build
../configure 	--prefix=%{package_path} \
				--with-gmp=%{package_path}
make
popd

%install
pushd build
make DESTDIR=%{buildroot} install
rm -rf %{buildroot}/%{package_path}/share/info/dir
popd

%files
%defattr(-,software,software)
%{package_path}/include/mpf2mpfr.h
%{package_path}/include/mpfr.h
%{package_path}/lib/libmpfr.a
%{package_path}/lib/libmpfr.la
%{package_path}/lib/libmpfr.so
%{package_path}/lib/libmpfr.so.1
%{package_path}/lib/libmpfr.so.1.2.2
%{package_path}/share/doc/mpfr/AUTHORS
%{package_path}/share/doc/mpfr/BUGS
%{package_path}/share/doc/mpfr/COPYING
%{package_path}/share/doc/mpfr/COPYING.LIB
%{package_path}/share/doc/mpfr/FAQ.html
%{package_path}/share/doc/mpfr/NEWS
%{package_path}/share/doc/mpfr/TODO
%{package_path}/share/doc/mpfr/examples/ReadMe
%{package_path}/share/doc/mpfr/examples/divworst.c
%{package_path}/share/doc/mpfr/examples/rndo-add.c
%{package_path}/share/doc/mpfr/examples/sample.c
%{package_path}/share/info/mpfr.info
