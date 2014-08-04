%define package_name 	mpc
%define package_family	gcc49
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
BuildRequires: compilers-gcc49-gmp
BuildRequires: compilers-gcc49-mpfr
Requires: Lmod
Requires: compilers-gcc49-gmp
Requires: compilers-gcc49-mpfr

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
%defattr(-,root,root)
/opt/software/compilers/gcc49/include/mpc.h
/opt/software/compilers/gcc49/lib/libmpc.a
/opt/software/compilers/gcc49/lib/libmpc.la
/opt/software/compilers/gcc49/lib/libmpc.so
/opt/software/compilers/gcc49/lib/libmpc.so.2
/opt/software/compilers/gcc49/lib/libmpc.so.2.0.0
/opt/software/compilers/gcc49/share/info/mpc.info
