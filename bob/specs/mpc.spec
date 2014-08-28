%define package_name 	mpc
%define package_version 0.8.1
%define package_type 	compilers

%define compiler_family		gcc
%define compiler_version 	4.8.3
%define compiler_prefix  	%{package_type}-%{compiler_family}-%{compiler_version}

%define software_path	/opt/software
%define package_path	%{software_path}/%{package_type}/%{compiler_family}/%{compiler_version}

Summary: A C library for the arithmetic of complex numbers
Name: %{compiler_prefix}-%{package_name}
Version: %{package_version}
Release: 1%{?dist}
License: LGPLv2+ and GPLv2+ and GFDL
Group: System Environment/Libraries
Source: %{package_name}-%{version}.tar.gz
URL: http://www.multiprecision.org/
Vendor: CentOS
Packager: Rob Lyon <rob.lyon@wsu.edu>
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: environment-modules
BuildRequires: %{compiler_prefix}-gmp
BuildRequires: %{compiler_prefix}-mpfr
Requires: environment-modules
Requires: %{compiler_prefix}-gmp
Requires: %{compiler_prefix}-mpfr

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
