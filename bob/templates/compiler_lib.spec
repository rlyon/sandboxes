Summary: 
Name: 
Version: 
Release: 1%{?dist}
License: 
Group: System Environment/Libraries
Source: %{name}-%{version}.tar.gz
Source99: defines.inc
URL: 
Vendor: CentOS
Packager: Rob Lyon <rob.lyon@wsu.edu>
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root

%include %{_sourcedir}/defines.inc

%package -n %{package_name}
Summary: 
Version: 
Release: 1%{?dist}
Group: System Environment/Libraries
BuildRequires: environment-modules
BuildRequires: %{compiler-family}-core
Requires: environment-modules
Requires: %{compiler-family}-core

%description
%description -n %{package_name}
Description is here

%prep
%setup -q -n %{name}-%{version}

%build
mkdir build ; pushd build

CFLAGS="${CFLAGS:-%optflags}"
CFLAGS="${CFLAGS} -I%{_includedir} -L%{_libdir}"     ; export CFLAGS
CXXFLAGS="${CXXFLAGS:-%optflags}"
CXXFLAGS="${CXXFLAGS} -I%{_includedir} -L%{_libdir}" ; export CXXFLAGS
FFLAGS="${FFLAGS:-%optflags}"
FFLAGS="${FFLAGS} -I%{_includedir} -L%{_libdir}"     ; export FFLAGS
LDFLAGS="${LDFLAGS} -L%{_libdir}"                    ; export LDFLAGS

../configure 	--host=%{_host} --build=%{_build} \
    			--prefix=%{_prefix} \
    			--exec-prefix=%{_exec_prefix} \
    			--bindir=%{_bindir} \
    			--sbindir=%{_sbindir} \
    			--sysconfdir=%{_sysconfdir} \
    			--datadir=%{_datadir} \
    			--includedir=%{_includedir} \
    			--libdir=%{_libdir} \
    			--libexecdir=%{_libexecdir} \
    			--localstatedir=%{_localstatedir} \
    			--sharedstatedir=%{_sharedstatedir} \
    			--mandir=%{_mandir} \
    			--infodir=%{_infodir}
make %{_smp_mflags}
popd

%install
pushd build
make DESTDIR=%{buildroot} install
rm -rf %{buildroot}/%{_infodir}/dir
popd

%files -n %{package_name}
%defattr(-,software,software)
