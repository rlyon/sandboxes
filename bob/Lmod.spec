Summary: Provides dynamic modification of a user's environment
Name: Lmod
Version: 5.6.3
Release: 1%{?dist}
License: MIT
Group: Applications/System
Source: %{name}-%{version}.tar.bz2
URL: http://sourceforge.net/projects/lmod
Vendor: TACC
Packager: Rob Lyon <rob.lyon@wsu.edu>
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: rsync
BuildRequires: lua-devel
BuildRequires: lua-filesystem
BuildRequires: lua-posix
Requires: tcsh
Requires: lua
Requires: lua-filesystem
Requires: lua-posix

%description
Lmod is a Lua based module system that easily handles the MODULEPATH Hierarchical problem. Environment Modules provide a convenient way to dynamically change the users' environment through modulefiles. This includes easily adding or removing directories to the PATH environment variable. Modulefiles for Library packages provide environment variables that specify where the library and header files can be found.

%prep
%setup -q -n %{name}-%{version}

%build
echo "RPM_BUILD_ROOT=$RPM_BUILD_ROOT"
./configure --prefix=/usr \
			--with-module-root-path=/opt/software/modulefiles \
			--with-spiderCacheDir=/opt/software/moduledata/cache \
			--with-updateSystemFn=/opt/software/moduledata/system.txt

%install
echo "INSTALLING"
mkdir -p $RPM_BUILD_ROOT/opt/software/modulefiles
mkdir -p $RPM_BUILD_ROOT/opt/software/moduledata/cache
make DESTDIR=$RPM_BUILD_ROOT install
rm $RPM_BUILD_ROOT/usr/lmod/lmod

%post
# If /usr/modules doesn't exist or it is a link, change it
if [ ! -e /usr/modules ] || [ -L /usr/modules ] ; then
	rm -rf /usr/modules
	ln -s /usr/lmod/%{version} /usr/modules
fi
rm /usr/lmod/lmod
ln -s /usr/lmod/%{version} /usr/lmod/lmod

%files
%defattr(-,root,root)
%config(noreplace) /usr/lmod/5.6.3/init/*
%dir /opt/software/modulefiles
%dir /opt/software/moduledata/cache
/usr/lmod/5.6.3/lib
/usr/lmod/5.6.3/libexec
/usr/lmod/5.6.3/modulefiles
/usr/lmod/5.6.3/settarg
/usr/lmod/5.6.3/shells
/usr/lmod/5.6.3/tools


