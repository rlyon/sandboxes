Summary: Provides dynamic modification of a user's environment
Name: Lmod
Version: 5.6.3
Release: 1
License: MIT
Group: Applications/System
Source: Lmod-5.6.3.tar.bz2
URL: http://sourceforge.net/projects/lmod
Vendor: TACC
Packager: Rob Lyon <rob.lyon@wsu.edu>
BuildRequires: lua-devel
BuildRequires: lua-filesystem
BuildRequires: lua-posix

%description
Lmod is a Lua based module system that easily handles the MODULEPATH Hierarchical problem. Environment Modules provide a convenient way to dynamically change the users' environment through modulefiles. This includes easily adding or removing directories to the PATH environment variable. Modulefiles for Library packages provide environment variables that specify where the library and header files can be found.

%prep
%setup

%build
./configure --prefix=/usr \
			--with-module-root-path=/opt/software/modulefiles \
			--with-spiderCacheDir=/opt/software/moduledata/cache \
			--with-updateSystemFn=/opt/software/moduledata/system.txt

%install
mkdir -p %{buildroot}/opt/software/modulefiles
mkdir -p %{buildroot}/opt/software/moduledata/cache
make install DESTDIR=$RPM_BUILD_ROOT

%files

