%define package_name 	zlib
%define package_family	gcc48
%define package_type 	compilers
%define software_path	/opt/software
%define package_path	%{software_path}/%{package_type}/%{package_family}

Summary: The zlib compression and decompression library
Name: %{package_type}-%{package_family}-%{package_name}
Version: 1.2.8
Release: 1%{?dist}
License: zlib and Boost
Group: System Environment/Libraries
Source: %{package_name}-%{version}.tar.gz
URL: http://www.gzip.org/zlib/
Vendor: CentOS
Packager: Rob Lyon <rob.lyon@wsu.edu>
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: Lmod
BuildRequires: m4
Requires: Lmod

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
