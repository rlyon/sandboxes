%define package_name 	gmp
%define package_family	gcc49
%define package_type 	compilers
%define software_path	/opt/software
%define package_path	%{software_path}/%{package_type}/%{package_family}

Summary: A GNU arbitrary precision library
Name: %{package_type}-%{package_family}-%{package_name}
Version: 4.3.2
Release: 1%{?dist}
License: LGPLv2+ and  GPLv3+ and LGPLv3+
Group: System Environment/Libraries
Source: %{package_name}-%{version}.tar.gz
URL: http://gmplib.org/
Vendor: CentOS
Packager: Rob Lyon <rob.lyon@wsu.edu>
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: Lmod
BuildRequires: m4
Requires: Lmod

%description
The gmp package contains GNU MP, a library for arbitrary precision
arithmetic, signed integers operations, rational numbers and floating
point numbers. GNU MP is designed for speed, for both small and very
large operands. GNU MP is fast because it uses fullwords as the basic
arithmetic type, it uses fast algorithms, it carefully optimizes
assembly code for many CPUs' most common inner loops, and it generally
emphasizes speed over simplicity/elegance in its operations.

Install the gmp package if you need a fast arbitrary precision
library.

%prep
%setup -q -n %{package_name}-%{version}

%build
mkdir build ; pushd build
../configure --prefix=%{package_path}
make
popd

%install
pushd build
make DESTDIR=%{buildroot} install
rm -rf %{buildroot}/%{package_path}/share/info/dir
popd

%files
%defattr(-,root,root)
%{package_path}/include/gmp.h
%{package_path}/lib/libgmp.a
%{package_path}/lib/libgmp.la
%{package_path}/lib/libgmp.so
%{package_path}/lib/libgmp.so.3
%{package_path}/lib/libgmp.so.3.5.2
%{package_path}/share/info/gmp.info
%{package_path}/share/info/gmp.info-1
%{package_path}/share/info/gmp.info-2
