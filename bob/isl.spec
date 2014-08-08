%define package_name 	isl
%define package_family	gcc48
%define package_type 	compilers
%define software_path	/opt/software
%define package_path	%{software_path}/%{package_type}/%{package_family}

Summary: A thread-safe C library for manipulating integer points
Name: %{package_type}-%{package_family}-%{package_name}
Version: 0.12.2
Release: 1%{?dist}
License: MIT
Group: System Environment/Libraries
Source: %{package_name}-%{version}.tar.gz
URL: ftp://gcc.gnu.org/pub/gcc/infrastructure
Vendor: CentOS
Packager: Rob Lyon <rob.lyon@wsu.edu>
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: Lmod
BuildRequires: compilers-%{package_family}-gmp
Requires: Lmod
Requires: compilers-%{package_family}-gmp

%description
Isl is a thread-safe C library for manipulating sets and relations
of integer points bounded by affine constraints.  The descriptions of
the sets and relations may involve both parameters and existentially
quantified variables.  All computations are performed in exact integer
arithmetic using GMP.

%prep
%setup -q -n %{package_name}-%{version}

%build
mkdir build ; pushd build
../configure 	--prefix=%{package_path} \
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
%{package_path}/include/isl/aff.h
%{package_path}/include/isl/aff_type.h
%{package_path}/include/isl/arg.h
%{package_path}/include/isl/ast.h
%{package_path}/include/isl/ast_build.h
%{package_path}/include/isl/band.h
%{package_path}/include/isl/blk.h
%{package_path}/include/isl/config.h
%{package_path}/include/isl/constraint.h
%{package_path}/include/isl/ctx.h
%{package_path}/include/isl/dim.h
%{package_path}/include/isl/flow.h
%{package_path}/include/isl/hash.h
%{package_path}/include/isl/id.h
%{package_path}/include/isl/ilp.h
%{package_path}/include/isl/int.h
%{package_path}/include/isl/list.h
%{package_path}/include/isl/local_space.h
%{package_path}/include/isl/lp.h
%{package_path}/include/isl/map.h
%{package_path}/include/isl/map_type.h
%{package_path}/include/isl/mat.h
%{package_path}/include/isl/multi.h
%{package_path}/include/isl/obj.h
%{package_path}/include/isl/options.h
%{package_path}/include/isl/point.h
%{package_path}/include/isl/polynomial.h
%{package_path}/include/isl/polynomial_type.h
%{package_path}/include/isl/printer.h
%{package_path}/include/isl/schedule.h
%{package_path}/include/isl/seq.h
%{package_path}/include/isl/set.h
%{package_path}/include/isl/set_type.h
%{package_path}/include/isl/space.h
%{package_path}/include/isl/stdint.h
%{package_path}/include/isl/stream.h
%{package_path}/include/isl/union_map.h
%{package_path}/include/isl/union_map_type.h
%{package_path}/include/isl/union_set.h
%{package_path}/include/isl/union_set_type.h
%{package_path}/include/isl/val.h
%{package_path}/include/isl/val_gmp.h
%{package_path}/include/isl/val_int.h
%{package_path}/include/isl/vec.h
%{package_path}/include/isl/version.h
%{package_path}/include/isl/vertices.h
%{package_path}/lib/libisl.a
%{package_path}/lib/libisl.la
%{package_path}/lib/libisl.so
%{package_path}/lib/libisl.so.10
%{package_path}/lib/libisl.so.10.2.2
%{package_path}/lib/libisl.so.10.2.2-gdb.py
%{package_path}/lib/libisl.so.10.2.2-gdb.pyc
%{package_path}/lib/libisl.so.10.2.2-gdb.pyo
%{package_path}/lib/pkgconfig/isl.pc
