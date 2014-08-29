%define package_name 	readline
%define package_version	6.3
%define package_type 	library

%define compiler_family		gcc
%define compiler_version 	4.8.3
%define compiler_prefix  	compilers-%{compiler_family}-%{compiler_version}
%define module_prefix  		module-%{compiler_family}-%{compiler_version}
%define library_prefix  	library-%{compiler_family}-%{compiler_version}

%define software_path	/opt/software
%define package_path	%{software_path}/%{package_type}/%{compiler_family}/%{compiler_version}

Summary: A library for editing typed command lines
Name: %{library_prefix}-%{package_name}
Version: %{package_version}
Release: 1%{?dist}
License: GPLv3+
Group: System Environment/Libraries
Vendor: CentOS
Packager: Rob Lyon <rob.lyon@wsu.edu>
URL: http://cnswww.cns.cwru.edu/php/chet/readline/rltop.html
Source: %{package_name}-%{package_version}.tar.gz
Buildroot: %{_tmppath}/%{package_name}-%{package_version}-%{release}-root
BuildRequires: environment-modules
BuildRequires: %{module_prefix}
Requires: environment-modules
Requires: %{module_prefix}

%description
The Readline library provides a set of functions that allow users to
edit command lines. Both Emacs and vi editing modes are available. The
Readline library includes additional functions for maintaining a list
of previously-entered command lines for recalling or editing those
lines, and for performing csh-like history expansion on previous
commands.


%prep
%setup -q -n %{package_name}-%{package_version}

%build
mkdir build ; pushd build
CFLAGS
../configure 	--prefix=%{package_path} \
				--libdir=%{package_path}/%{_lib} \
				--mandir=%{package_path}/share/man \
				--enable-shared \
				--enable-static \
				--with-curses
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