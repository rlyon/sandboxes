%define package_name 	ncurses
%define package_version	5.9
%define package_type 	library

%define compiler_family		gcc
%define compiler_version 	4.8.3
%define compiler_prefix  	compilers-%{compiler_family}-%{compiler_version}
%define module_prefix  		module-%{compiler_family}-%{compiler_version}
%define library_prefix  	library-%{compiler_family}-%{compiler_version}

%define software_path	/opt/software
%define package_path	%{software_path}/%{package_type}/%{compiler_family}/%{compiler_version}

Summary: Ncurses support utilities
Name: %{library_prefix}-%{package_name}
Version: %{package_version}
Release: 1%{?dist}
License: MIT
Group: System Environment/Libraries
Vendor: CentOS
Packager: Rob Lyon <rob.lyon@wsu.edu>
URL: http://invisible-island.net/ncurses/ncurses.html
Source: %{package_name}-%{package_version}.tar.gz
Buildroot: %{_tmppath}/%{package_name}-%{package_version}-%{release}-root
BuildRequires: environment-modules
BuildRequires: %{module_prefix}
Requires: environment-modules
Requires: %{module_prefix}

%description
The curses library routines are a terminal-independent method of
updating character screens with reasonable optimization.  The ncurses
(new curses) library is a freely distributable replacement for the
discontinued 4.4 BSD classic curses library.

This package contains support utilities, including a terminfo compiler
tic, a decompiler infocmp, clear, tput, tset, and a termcap conversion
tool captoinfo.

%prep
%setup -q -n %{package_name}-%{package_version}

%build
mkdir build ; pushd build
../configure 	--prefix=%{package_path} \
				--libdir=%{package_path}/%{_lib} \
				--mandir=%{package_path}/share/man \
				--datadir=%{package_path}/share \
				--with-shared \
				--with-default-terminfo-dir=%{package_path}/share/terminfo \
				--with-termpath=%{package_path}/share/terminfo \
				--enable-pc-files \
				--enable-overwrite \
				--enable-hard-tabs --enable-xmc-glitch --enable-colorfgbg \
				--without-ada --with-ospeed=unsigned \
				--with-termlib=tinfo \
				--with-chtype=long \
				--with-ticlib
make
popd

%install
pushd build
make DESTDIR=%{buildroot} install
popd

# Get the files
find %{buildroot}%{package_path}/share/man/man1 -type f -printf "%{package_path}/share/man/man1/%f\n" > manfiles
find %{buildroot}%{package_path}/share/man/man3 -type f -printf "%{package_path}/share/man/man3/%f\n" >> manfiles
find %{buildroot}%{package_path}/share/man/man5 -type f -printf "%{package_path}/share/man/man5/%f\n" >> manfiles
find %{buildroot}%{package_path}/share/man/man7 -type f -printf "%{package_path}/share/man/man7/%f\n" >> manfiles
# Get the links
find %{buildroot}%{package_path}/share/man/man1 -type l -printf "%{package_path}/share/man/man1/%f\n" >> manfiles
find %{buildroot}%{package_path}/share/man/man3 -type l -printf "%{package_path}/share/man/man3/%f\n" >> manfiles
find %{buildroot}%{package_path}/share/man/man5 -type l -printf "%{package_path}/share/man/man5/%f\n" >> manfiles
find %{buildroot}%{package_path}/share/man/man7 -type l -printf "%{package_path}/share/man/man7/%f\n" >> manfiles

%clean
rm -fr ${RPM_BUILD_ROOT}

%files -f manfiles
%defattr(-,software,software)
%{package_path}/bin/captoinfo
%{package_path}/bin/clear
%{package_path}/bin/infocmp
%{package_path}/bin/infotocap
%{package_path}/bin/ncurses5-config
%{package_path}/bin/reset
%{package_path}/bin/tabs
%{package_path}/bin/tic
%{package_path}/bin/toe
%{package_path}/bin/tput
%{package_path}/bin/tset
%{package_path}/include/curses.h
%{package_path}/include/cursesapp.h
%{package_path}/include/cursesf.h
%{package_path}/include/cursesm.h
%{package_path}/include/cursesp.h
%{package_path}/include/cursesw.h
%{package_path}/include/cursslk.h
%{package_path}/include/eti.h
%{package_path}/include/etip.h
%{package_path}/include/form.h
%{package_path}/include/menu.h
%{package_path}/include/nc_tparm.h
%{package_path}/include/ncurses.h
%{package_path}/include/ncurses_dll.h
%{package_path}/include/panel.h
%{package_path}/include/term.h
%{package_path}/include/term_entry.h
%{package_path}/include/termcap.h
%{package_path}/include/tic.h
%{package_path}/include/unctrl.h
%{package_path}/%{_lib}/libcurses.a
%{package_path}/%{_lib}/libcurses.so
%{package_path}/%{_lib}/libtic.a
%{package_path}/%{_lib}/libtic.so
%{package_path}/%{_lib}/libtic.so.5
%{package_path}/%{_lib}/libtic.so.5.9
%{package_path}/%{_lib}/libtic_g.a
%{package_path}/%{_lib}/libtinfo.a
%{package_path}/%{_lib}/libtinfo.so
%{package_path}/%{_lib}/libtinfo.so.5
%{package_path}/%{_lib}/libtinfo.so.5.9
%{package_path}/%{_lib}/libtinfo_g.a
%{package_path}/%{_lib}/libform.a
%{package_path}/%{_lib}/libform_g.a
%{package_path}/%{_lib}/libmenu.a
%{package_path}/%{_lib}/libmenu_g.a
%{package_path}/%{_lib}/libncurses++.a
%{package_path}/%{_lib}/libncurses.a
%{package_path}/%{_lib}/libncurses_g.a
%{package_path}/%{_lib}/libpanel.a
%{package_path}/%{_lib}/libpanel_g.a
%{package_path}/%{_lib}/libform.so
%{package_path}/%{_lib}/libform.so.5
%{package_path}/%{_lib}/libform.so.5.9
%{package_path}/%{_lib}/libmenu.so
%{package_path}/%{_lib}/libmenu.so.5
%{package_path}/%{_lib}/libmenu.so.5.9
%{package_path}/%{_lib}/libncurses.so
%{package_path}/%{_lib}/libncurses.so.5
%{package_path}/%{_lib}/libncurses.so.5.9
%{package_path}/%{_lib}/libpanel.so
%{package_path}/%{_lib}/libpanel.so.5
%{package_path}/%{_lib}/libpanel.so.5.9
%dir %{package_path}/share/tabset
%dir %{package_path}/share/terminfo
%{package_path}/share/tabset/*
%{package_path}/share/terminfo/*
# Pick up that pesky symlink
%ifarch i386 i686
%{package_path}/%{_lib}/terminfo
%endif