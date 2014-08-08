%define package_name 	cloog
%define package_family	gcc48
%define package_type 	compilers
%define software_path	/opt/software
%define package_path	%{software_path}/%{package_type}/%{package_family}

Summary: A C library for generate code for scanning Z-polyhedra
Name: %{package_type}-%{package_family}-%{package_name}
Version: 0.18.1
Release: 1%{?dist}
License: GNU
Group: System Environment/Libraries
Source: %{package_name}-%{version}.tar.gz
URL: http://www.cloog.org/
Vendor: CentOS
Packager: Rob Lyon <rob.lyon@wsu.edu>
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: Lmod
BuildRequires: compilers-%{package_family}-gmp
BuildRequires: compilers-%{package_family}-isl
Requires: Lmod
Requires: compilers-%{package_family}-gmp
Requires: compilers-%{package_family}-isl

%description
CLooG is a free software and library to generate code for scanning 
Z-polyhedra. That is, it finds a code (e.g. in C, FORTRAN...) that 
reaches each integral point of one or more parameterized polyhedra. 
CLooG has been originally written to solve the code generation 
problem for optimizing compilers based on the polytope model. 
Nevertheless it is used now in various area e.g. to build control 
automata for high-level synthesis or to find the best polynomial 
approximation of a function. CLooG may help in any situation where 
scanning polyhedra matters. While the user has full control on 
generated code quality, CLooG is designed to avoid control overhead 
and to produce a very effective code. 

%prep
%setup -q -n %{package_name}-%{version}

%build
mkdir build ; pushd build
../configure 	--prefix=%{package_path} \
				--with-isl=system \
				--with-isl-prefix=%{package_path} \
				--with-gmp=system \
				--with-gmp-prefix=%{package_path}
make
popd

%install
pushd build
make DESTDIR=%{buildroot} install
# rm -rf %{buildroot}/%{package_path}/share/info/dir
popd

%files
%defattr(-,software,software)
%{package_path}/bin/cloog
%{package_path}/include/cloog/block.h
%{package_path}/include/cloog/clast.h
%{package_path}/include/cloog/cloog.h
%{package_path}/include/cloog/constraints.h
%{package_path}/include/cloog/domain.h
%{package_path}/include/cloog/input.h
%{package_path}/include/cloog/int.h
%{package_path}/include/cloog/isl/backend.h
%{package_path}/include/cloog/isl/cloog.h
%{package_path}/include/cloog/isl/constraintset.h
%{package_path}/include/cloog/isl/domain.h
%{package_path}/include/cloog/loop.h
%{package_path}/include/cloog/matrix.h
%{package_path}/include/cloog/matrix/constraintset.h
%{package_path}/include/cloog/names.h
%{package_path}/include/cloog/options.h
%{package_path}/include/cloog/pprint.h
%{package_path}/include/cloog/program.h
%{package_path}/include/cloog/state.h
%{package_path}/include/cloog/statement.h
%{package_path}/include/cloog/stride.h
%{package_path}/include/cloog/union_domain.h
%{package_path}/include/cloog/version.h
%{package_path}/lib/cloog-isl/cloog-isl-config.cmake
%{package_path}/lib/isl/isl-config.cmake
%{package_path}/lib/libcloog-isl.a
%{package_path}/lib/libcloog-isl.la
%{package_path}/lib/libcloog-isl.so
%{package_path}/lib/libcloog-isl.so.4
%{package_path}/lib/libcloog-isl.so.4.0.0
%{package_path}/lib/pkgconfig/cloog-isl.pc
