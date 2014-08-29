%define package_name 	lapack
%define package_version	3.5.0
%define package_type 	library

%define compiler_family		gcc
%define compiler_version 	4.8.3
%define compiler_prefix  	compilers-%{compiler_family}-%{compiler_version}
%define module_prefix  		module-%{compiler_family}-%{compiler_version}
%define library_prefix  	library-%{compiler_family}-%{compiler_version}

%define software_path	/opt/software
%define package_path	%{software_path}/%{package_type}/%{compiler_family}/%{compiler_version}

Summary: Numerical linear algebra package libraries
Name: %{library_prefix}-%{package_name}
Version: %{package_version}
Release: 1%{?dist}
License: BSD
Group: System Environment/Libraries
Vendor: CentOS
Packager: Rob Lyon <rob.lyon@wsu.edu>
URL: http://www.netlib.org/lapack/
Source: http://www.netlib.org/lapack/lapack-%{version}.tgz
Patch3: lapack-3.5.0-make.inc.patch
Patch4: lapack-3.5.0-makefile.blas.patch
Patch5: lapack-3.5.0-makefile.lapack.patch
Buildroot: %{_tmppath}/%{package_name}-%{package_version}-%{release}-root
BuildRequires: environment-modules
BuildRequires: %{module_prefix}
Requires: environment-modules
Requires: %{module_prefix}

%description
LAPACK (Linear Algebra PACKage) is a standard library for numerical
linear algebra. LAPACK provides routines for solving systems of
simultaneous linear equations, least-squares solutions of linear
systems of equations, eigenvalue problems, and singular value
problems. Associated matrix factorizations (LU, Cholesky, QR, SVD,
Schur, and generalized Schur) and related computations (i.e.,
reordering of Schur factorizations and estimating condition numbers)
are also included. LAPACK can handle dense and banded matrices, but
not general sparse matrices. Similar functionality is provided for
real and complex matrices in both single and double precision. LAPACK
is coded in Fortran77 and built with gcc.

%define blas_version 3.2.1
%package -n %{library_prefix}-blas
Version: %{blas_version}
Summary: The Basic Linear Algebra Subprograms library
Group: Development/Libraries
Requires: environment-modules
Requires: %{module_prefix}

%description -n %{library_prefix}-blas
BLAS (Basic Linear Algebra Subprograms) is a standard library which
provides a number of basic algorithms for numerical algebra. 

%prep
%setup -q -n %{package_name}-%{package_version}
%patch3 -p1
%patch4 -p1
%patch5 -p1
cp -f INSTALL/make.inc.gfortran make.inc

%build
. /usr/modules/init/sh
module load %{compiler_family}/%{compiler_version}
module list
RPM_OPT_O_FLAGS=$(echo $RPM_OPT_FLAGS | sed 's|-O2|-O0|')
export FC=gfortran

pushd BLAS/SRC
FFLAGS="$RPM_OPT_O_FLAGS" make dcabs1.o
FFLAGS="$RPM_OPT_FLAGS" CFLAGS="$RPM_OPT_FLAGS $M_CFLAGS" make static
make clean
FFLAGS="$RPM_OPT_O_FLAGS -fPIC" make dcabs1.o
FFLAGS="$RPM_OPT_FLAGS -fPIC" CFLAGS="$RPM_OPT_FLAGS -fPIC $M_CFLAGS" make shared
popd

cp BLAS/SRC/libblas* .
ln -s libblas.so.%{blas_version} libblas.so

pushd SRC
FFLAGS="$RPM_OPT_O_FLAGS" make slaruv.o
FFLAGS="$RPM_OPT_O_FLAGS" make dlaruv.o
FFLAGS="$RPM_OPT_O_FLAGS" make sla_wwaddw.o
FFLAGS="$RPM_OPT_O_FLAGS" make dla_wwaddw.o
FFLAGS="$RPM_OPT_O_FLAGS" make cla_wwaddw.o
FFLAGS="$RPM_OPT_O_FLAGS" make zla_wwaddw.o
FFLAGS="$RPM_OPT_FLAGS" CFLAGS="$RPM_OPT_FLAGS $M_CFLAGS" make static
make clean
popd
pushd INSTALL
make clean
popd
pushd SRC
FFLAGS="$RPM_OPT_O_FLAGS -fPIC" make slaruv.o
FFLAGS="$RPM_OPT_O_FLAGS -fPIC" make dlaruv.o
FFLAGS="$RPM_OPT_O_FLAGS -fPIC" make sla_wwaddw.o
FFLAGS="$RPM_OPT_O_FLAGS -fPIC" make dla_wwaddw.o
FFLAGS="$RPM_OPT_O_FLAGS -fPIC" make cla_wwaddw.o
FFLAGS="$RPM_OPT_O_FLAGS -fPIC" make zla_wwaddw.o
FFLAGS="$RPM_OPT_FLAGS -fPIC" CFLAGS="$RPM_OPT_FLAGS -fPIC $M_CFLAGS" make shared
popd

cp SRC/liblapack* .

%install
rm -fr ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}%{package_path}/%{_lib}

for f in liblapack.so.%{package_version} libblas.so.%{blas_version} libblas.a liblapack.a; do
  cp -f $f ${RPM_BUILD_ROOT}%{package_path}/%{_lib}/$f
done

cd ${RPM_BUILD_ROOT}%{package_path}/%{_lib}
ln -sf liblapack.so.%{version} liblapack.so
ln -sf liblapack.so.%{version} liblapack.so.3
ln -sf liblapack.so.%{version} liblapack.so.3.5
ln -sf libblas.so.%{blas_version} libblas.so
ln -sf libblas.so.%{blas_version} libblas.so.3
ln -sf libblas.so.%{blas_version} libblas.so.3.2

%clean
rm -fr ${RPM_BUILD_ROOT}

%files
%defattr(-,software,software)
%{package_path}/%{_lib}/liblapack.so.*
%{package_path}/%{_lib}/liblapack.so
%{package_path}/%{_lib}/liblapack*.a

%files -n %{library_prefix}-blas
%defattr(-,root,root)
%{package_path}/%{_lib}/libblas.so.*
%{package_path}/%{_lib}/libblas.so
%{package_path}/%{_lib}/libblas*.a
