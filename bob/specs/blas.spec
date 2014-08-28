%define package_name 	blas
%define package_version	3.5.0
%define package_type 	library

%define compiler_family		gcc
%define compiler_version 	4.8.3
%define compiler_prefix  	compilers-%{compiler_family}-%{compiler_version}
%define library_prefix  	library-%{compiler_family}-%{compiler_version}

%define software_path	/opt/software
%define package_path	%{software_path}/%{package_type}/%{compiler_family}/%{compiler_version}


Summary: Routines that provide standard building blocks for performing basic vector and matrix operations.
Name: %{library_prefix}-%{package_name}
Version: %{package_version}
Release: 1%{?dist}
License: MIT
Group: System Environment/Libraries
Source: %{package_name}.tgz
URL: http://www.netlib.org/blas/
Vendor: CentOS
Packager: Rob Lyon <rob.lyon@wsu.edu>
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: environment-modules
BuildRequires: %{compiler_prefix}-core
Requires: environment-modules
Requires: %{compiler_prefix}-core

%description
The BLAS (Basic Linear Algebra Subprograms) are routines that provide standard
building blocks for performing basic vector and matrix operations. The Level 1
BLAS perform scalar, vector and vector-vector operations, the Level 2 BLAS
perform matrix-vector operations, and the Level 3 BLAS perform matrix-matrix
operations. Because the BLAS are efficient, portable, and widely available,
they are commonly used in the development of high quality linear algebra
software, LAPACK for example.

%prep
%setup -q -n BLAS

%build
mkdir build ; pushd build
../configure 	--prefix=%{package_path}
make
popd

%install
pushd build
make DESTDIR=%{buildroot} install
# rm -rf %{buildroot}/%{package_path}/share/info/dir
popd

%files
%defattr(-,software,software)