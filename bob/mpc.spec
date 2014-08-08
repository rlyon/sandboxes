%define package_name 	mpc
%define package_family	gcc48
%define package_type 	compilers
%define software_path	/opt/software
%define package_path	%{software_path}/%{package_type}/%{package_family}

Summary: A C library for the arithmetic of complex numbers
Name: %{package_type}-%{package_family}-%{package_name}
Version: 0.8.1
Release: 1%{?dist}
License: LGPLv2+ and GPLv2+ and GFDL
Group: System Environment/Libraries
Source: %{package_name}-%{version}.tar.gz
URL: http://www.multiprecision.org/
Vendor: CentOS
Packager: Rob Lyon <rob.lyon@wsu.edu>
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: Lmod
BuildRequires: compilers-%{package_family}-gmp
BuildRequires: compilers-%{package_family}-mpfr
Requires: Lmod
Requires: compilers-%{package_family}-gmp
Requires: compilers-%{package_family}-mpfr

%description
Gnu Mpc is a C library for the arithmetic of complex numbers with
arbitrarily high precision and correct rounding of the result. It
extends the principles of the IEEE-754 standard for fixed precision
real floating point numbers to complex numbers, providing well-defined
semantics for every operation. At the same time, speed of operation
at high precision is a major design goal. 

%prep
%setup -q -n %{package_name}-%{version}

%build
mkdir build ; pushd build
../configure 	--prefix=%{package_path} \
				--with-gmp=%{package_path} \
				--with-mpfr=%{package_path}
make
popd

%install
pushd build
make DESTDIR=%{buildroot} install
rm -rf %{buildroot}/%{package_path}/share/info/dir
popd

%files
%defattr(-,software,software)
%{package_path}/include/mpc.h
%{package_path}/lib/libmpc.a
%{package_path}/lib/libmpc.la
%{package_path}/lib/libmpc.so
%{package_path}/lib/libmpc.so.2
%{package_path}/lib/libmpc.so.2.0.0
%{package_path}/share/info/mpc.info
