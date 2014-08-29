%define package_name 	pcre
%define package_version	8.35
%define package_type 	library

%define compiler_family		gcc
%define compiler_version 	4.8.3
%define compiler_prefix  	compilers-%{compiler_family}-%{compiler_version}
%define module_prefix  		module-%{compiler_family}-%{compiler_version}
%define library_prefix  	library-%{compiler_family}-%{compiler_version}

%define software_path	/opt/software
%define package_path	%{software_path}/%{package_type}/%{compiler_family}/%{compiler_version}

Summary: Perl-compatible regular expression library
Name: %{library_prefix}-%{package_name}
Version: %{package_version}
Release: 1%{?dist}
License: BSD
Group: System Environment/Libraries
Vendor: CentOS
Packager: Rob Lyon <rob.lyon@wsu.edu>
URL: http://www.pcre.org/
Source: %{package_name}-%{package_version}.tar.gz
Buildroot: %{_tmppath}/%{package_name}-%{package_version}-%{release}-root
BuildRequires: environment-modules
BuildRequires: %{module_prefix}
Requires: environment-modules
Requires: %{module_prefix}

%description
Perl-compatible regular expression library.
PCRE has its own native API, but a set of "wrapper" functions that are based on
the POSIX API are also supplied in the library libpcreposix. Note that this
just provides a POSIX calling interface to PCRE: the regular expressions
themselves still follow Perl syntax and semantics. The header file
for the POSIX-style functions is called pcreposix.h.

%prep
%setup -q -n %{package_name}-%{package_version}

%build
mkdir build ; pushd build
../configure 	--prefix=%{package_path} \
				--libdir=%{package_path}/%{_lib}
make
popd

%install
pushd build
make DESTDIR=%{buildroot} install
rm -rf %{buildroot}%{package_path}/share/doc
popd

%clean
rm -fr ${RPM_BUILD_ROOT}

%files
%defattr(-,software,software)
%{package_path}/bin/pcre-config
%{package_path}/bin/pcregrep
%{package_path}/bin/pcretest
%{package_path}/include/pcre.h
%{package_path}/include/pcre_scanner.h
%{package_path}/include/pcre_stringpiece.h
%{package_path}/include/pcrecpp.h
%{package_path}/include/pcrecpparg.h
%{package_path}/include/pcreposix.h
%{package_path}/%{_lib}/libpcre.a
%{package_path}/%{_lib}/libpcre.la
%{package_path}/%{_lib}/libpcre.so
%{package_path}/%{_lib}/libpcre.so.1
%{package_path}/%{_lib}/libpcre.so.1.2.3
%{package_path}/%{_lib}/libpcrecpp.a
%{package_path}/%{_lib}/libpcrecpp.la
%{package_path}/%{_lib}/libpcrecpp.so
%{package_path}/%{_lib}/libpcrecpp.so.0
%{package_path}/%{_lib}/libpcrecpp.so.0.0.0
%{package_path}/%{_lib}/libpcreposix.a
%{package_path}/%{_lib}/libpcreposix.la
%{package_path}/%{_lib}/libpcreposix.so
%{package_path}/%{_lib}/libpcreposix.so.0
%{package_path}/%{_lib}/libpcreposix.so.0.0.2
%{package_path}/%{_lib}/pkgconfig/libpcre.pc
%{package_path}/%{_lib}/pkgconfig/libpcrecpp.pc
%{package_path}/%{_lib}/pkgconfig/libpcreposix.pc
%{package_path}/share/man/man1/pcre*
%{package_path}/share/man/man3/pcre*