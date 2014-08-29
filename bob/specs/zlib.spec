%define package_name 	zlib
%define package_version	1.2.8
%define package_type 	compilers

%define compiler_family		gcc
%define compiler_version 	4.8.3
%define compiler_prefix  	%{package_type}-%{compiler_family}-%{compiler_version}

%define software_path	/opt/software
%define package_path	%{software_path}/%{package_type}/%{compiler_family}/%{compiler_version}

Summary: The zlib compression and decompression library
Name: %{compiler_prefix}-%{package_name}
Version: %{package_version}
Release: 1%{?dist}
License: zlib and Boost
Group: System Environment/Libraries
Source: %{package_name}-%{version}.tar.gz
URL: http://www.gzip.org/zlib/
Vendor: CentOS
Packager: Rob Lyon <rob.lyon@wsu.edu>
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: environment-modules
BuildRequires: m4
Requires: environment-modules

%description
Zlib is a general-purpose, patent-free, lossless data compression
library which is used by many different programs.

%prep
%setup -q -n %{package_name}-%{version}

%build
export LDFLAGS="$LDFLAGS -Wl,-z,relro"
./configure --prefix=%{package_path}
make

%install
make DESTDIR=%{buildroot} install

%files
%defattr(-,software,software)
%{package_path}/include/zconf.h
%{package_path}/include/zlib.h
%{package_path}/lib/libz.a
%{package_path}/lib/libz.so
%{package_path}/lib/libz.so.1
%{package_path}/lib/libz.so.1.2.8
%{package_path}/lib/pkgconfig/zlib.pc
%{package_path}/share/man/man3/zlib.3