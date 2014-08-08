%define package_family	gcc48
%define package_type 	compilers
%define software_path	/opt/software
%define modulefiles_path %{software_path}/modulefiles
%define package_path	%{software_path}/%{package_type}/%{package_family}

Summary: Metapackage for the GCC %{version} compiler family
Name: %{package_type}-%{package_family}
Version: 4.8.3
Release: 1%{?dist}
License: Various
Group: Development/Languages
Vendor: CentOS
Packager: Rob Lyon <rob.lyon@wsu.edu>
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: Lmod
Requires: Lmod
Requires: %{name}-gmp
Requires: %{name}-mpfr
Requires: %{name}-mpc
Requires: %{name}-isl
Requires: %{name}-cloog
Requires: %{name}-zlib


%description
Metapackage for the GCC %{version} compiler family.  Installs GCC and
the required libraries.  Also installs the modulefile.

%prep
%setup -q -n %{package_name}-%{version}

%build

%install

%files
%defattr(-,root,root)
