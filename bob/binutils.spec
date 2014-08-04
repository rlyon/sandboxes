%define package_name 	binutils
%define package_family	gcc49
%define package_type 	compilers
%define software_path	/opt/software
%define package_path	%{software_path}/%{package_type}/%{package_family}

Summary: A GNU collection of binary utilities
Name: %{package_type}-%{package_family}-%{package_name}
Version: 2.24
Release: 1%{?dist}
License: GPLv3+
Group: Development/Tools
Source: %{package_name}-%{version}.tar.gz
URL: http://sources.redhat.com/binutils
Vendor: CentOS
Packager: Rob Lyon <rob.lyon@wsu.edu>
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: flex
BuildRequires: bison
BuildRequires: Lmod
BuildRequires: compilers-gcc49-gmp
BuildRequires: compilers-gcc49-mpfr
BuildRequires: compilers-gcc49-mpc
BuildRequires: compilers-gcc49-isl
BuildRequires: compilers-gcc49-cloog
Requires: Lmod
Requires: compilers-gcc49-gmp
Requires: compilers-gcc49-mpfr
Requires: compilers-gcc49-mpc
Requires: compilers-gcc49-isl
Requires: compilers-gcc49-cloog

%description
Binutils is a collection of binary utilities, including ar (for
creating, modifying and extracting from archives), as (a family of GNU
assemblers), gprof (for displaying call graph profile data), ld (the
GNU linker), nm (for listing symbols from object files), objcopy (for
copying and translating object files), objdump (for displaying
information from object files), ranlib (for generating an index for
the contents of an archive), readelf (for displaying detailed
information about binary files), size (for listing the section sizes
of an object or archive file), strings (for listing printable strings
from files), strip (for discarding symbols), and addr2line (for
converting addresses to file and line).

%prep
%setup -q -n %{package_name}-%{version}

%build
export LD_LIBRARY_PATH=%{package_path}/lib
export CFLAGS="-L%{package_path}/lib -I%{package_path}/include %{optflags}"
export CPPFLAGS=$CFLAGS
export CXXFLAGS=$CFLAGS
export LDFLAGS="-L%{package_path}/lib %{optflags}"
ls %{package_path}/lib -al
ls %{package_path}/lib/cloog-isl -al 
ls %{package_path}/lib/isl -al 
ls %{package_path}/include -al
mkdir build ; pushd build
../configure 	--prefix=%{package_path} \
				--enable-gold=default \
				--enable-shared \
				--disable-werror \
				--build=x86_64-redhat-linux \
				LD_LIBRARY_PATH=%{package_path}/lib \
				CFLAGS="-L%{package_path}/lib -I%{package_path}/include %{optflags}" \
				CPPFLAGS="-L%{package_path}/lib -I%{package_path}/include %{optflags}" \
				CXXFLAGS="-L%{package_path}/lib -I%{package_path}/include %{optflags}" \
				LDFLAGS="--build-id -L%{package_path}/lib %{optflags}"
make -j3
popd

%install
export LD_LIBRARY_PATH=%{package_path}/lib:$LD_LIBRARY_PATH
export CFLAGS="-L%{package_path}/lib -I%{package_path}/include %{optflags}"
export CPPFLAGS=$CFLAGS
export CXXFLAGS=$CFLAGS
export LDFLAGS="-L%{package_path}/lib %{optflags}"

pushd build
make DESTDIR=%{buildroot} install
rm -rf %{buildroot}/%{package_path}/share/info/dir
popd

%files
%defattr(-,root,root)
%{package_path}/bin/addr2line
%{package_path}/bin/ar
%{package_path}/bin/as
%{package_path}/bin/c++filt
%{package_path}/bin/dwp
%{package_path}/bin/elfedit
%{package_path}/bin/gprof
%{package_path}/bin/ld
%{package_path}/bin/ld.bfd
%{package_path}/bin/ld.gold
%{package_path}/bin/nm
%{package_path}/bin/objcopy
%{package_path}/bin/objdump
%{package_path}/bin/ranlib
%{package_path}/bin/readelf
%{package_path}/bin/size
%{package_path}/bin/strings
%{package_path}/bin/strip
%{package_path}/include/ansidecl.h
%{package_path}/include/bfd.h
%{package_path}/include/bfdlink.h
%{package_path}/include/dis-asm.h
%{package_path}/include/symcat.h
%{package_path}/lib/libbfd-2.24.so
%{package_path}/lib/libbfd.a
%{package_path}/lib/libbfd.la
%{package_path}/lib/libbfd.so
%{package_path}/lib/libopcodes-2.24.so
%{package_path}/lib/libopcodes.a
%{package_path}/lib/libopcodes.la
%{package_path}/lib/libopcodes.so
%{package_path}/share/info/as.info
%{package_path}/share/info/bfd.info
%{package_path}/share/info/binutils.info
%{package_path}/share/info/configure.info
%{package_path}/share/info/gprof.info
%{package_path}/share/info/ld.info
%{package_path}/share/info/standards.info
%{package_path}/share/locale/bg/LC_MESSAGES/binutils.mo
%{package_path}/share/locale/bg/LC_MESSAGES/gprof.mo
%{package_path}/share/locale/bg/LC_MESSAGES/ld.mo
%{package_path}/share/locale/da/LC_MESSAGES/bfd.mo
%{package_path}/share/locale/da/LC_MESSAGES/binutils.mo
%{package_path}/share/locale/da/LC_MESSAGES/gprof.mo
%{package_path}/share/locale/da/LC_MESSAGES/ld.mo
%{package_path}/share/locale/da/LC_MESSAGES/opcodes.mo
%{package_path}/share/locale/de/LC_MESSAGES/gprof.mo
%{package_path}/share/locale/de/LC_MESSAGES/opcodes.mo
%{package_path}/share/locale/eo/LC_MESSAGES/gprof.mo
%{package_path}/share/locale/es/LC_MESSAGES/bfd.mo
%{package_path}/share/locale/es/LC_MESSAGES/binutils.mo
%{package_path}/share/locale/es/LC_MESSAGES/gas.mo
%{package_path}/share/locale/es/LC_MESSAGES/gold.mo
%{package_path}/share/locale/es/LC_MESSAGES/gprof.mo
%{package_path}/share/locale/es/LC_MESSAGES/ld.mo
%{package_path}/share/locale/es/LC_MESSAGES/opcodes.mo
%{package_path}/share/locale/fi/LC_MESSAGES/bfd.mo
%{package_path}/share/locale/fi/LC_MESSAGES/binutils.mo
%{package_path}/share/locale/fi/LC_MESSAGES/gas.mo
%{package_path}/share/locale/fi/LC_MESSAGES/gold.mo
%{package_path}/share/locale/fi/LC_MESSAGES/gprof.mo
%{package_path}/share/locale/fi/LC_MESSAGES/ld.mo
%{package_path}/share/locale/fi/LC_MESSAGES/opcodes.mo
%{package_path}/share/locale/fr/LC_MESSAGES/bfd.mo
%{package_path}/share/locale/fr/LC_MESSAGES/binutils.mo
%{package_path}/share/locale/fr/LC_MESSAGES/gas.mo
%{package_path}/share/locale/fr/LC_MESSAGES/gprof.mo
%{package_path}/share/locale/fr/LC_MESSAGES/ld.mo
%{package_path}/share/locale/fr/LC_MESSAGES/opcodes.mo
%{package_path}/share/locale/ga/LC_MESSAGES/gprof.mo
%{package_path}/share/locale/ga/LC_MESSAGES/ld.mo
%{package_path}/share/locale/ga/LC_MESSAGES/opcodes.mo
%{package_path}/share/locale/hr/LC_MESSAGES/binutils.mo
%{package_path}/share/locale/id/LC_MESSAGES/bfd.mo
%{package_path}/share/locale/id/LC_MESSAGES/binutils.mo
%{package_path}/share/locale/id/LC_MESSAGES/gas.mo
%{package_path}/share/locale/id/LC_MESSAGES/gold.mo
%{package_path}/share/locale/id/LC_MESSAGES/gprof.mo
%{package_path}/share/locale/id/LC_MESSAGES/ld.mo
%{package_path}/share/locale/id/LC_MESSAGES/opcodes.mo
%{package_path}/share/locale/it/LC_MESSAGES/binutils.mo
%{package_path}/share/locale/it/LC_MESSAGES/gold.mo
%{package_path}/share/locale/it/LC_MESSAGES/gprof.mo
%{package_path}/share/locale/it/LC_MESSAGES/ld.mo
%{package_path}/share/locale/it/LC_MESSAGES/opcodes.mo
%{package_path}/share/locale/ja/LC_MESSAGES/bfd.mo
%{package_path}/share/locale/ja/LC_MESSAGES/binutils.mo
%{package_path}/share/locale/ja/LC_MESSAGES/gas.mo
%{package_path}/share/locale/ja/LC_MESSAGES/gprof.mo
%{package_path}/share/locale/ja/LC_MESSAGES/ld.mo
%{package_path}/share/locale/ms/LC_MESSAGES/gprof.mo
%{package_path}/share/locale/nl/LC_MESSAGES/gprof.mo
%{package_path}/share/locale/nl/LC_MESSAGES/opcodes.mo
%{package_path}/share/locale/pt_BR/LC_MESSAGES/gprof.mo
%{package_path}/share/locale/pt_BR/LC_MESSAGES/opcodes.mo
%{package_path}/share/locale/ro/LC_MESSAGES/bfd.mo
%{package_path}/share/locale/ro/LC_MESSAGES/binutils.mo
%{package_path}/share/locale/ro/LC_MESSAGES/gprof.mo
%{package_path}/share/locale/ro/LC_MESSAGES/opcodes.mo
%{package_path}/share/locale/ru/LC_MESSAGES/bfd.mo
%{package_path}/share/locale/ru/LC_MESSAGES/binutils.mo
%{package_path}/share/locale/ru/LC_MESSAGES/gas.mo
%{package_path}/share/locale/ru/LC_MESSAGES/gprof.mo
%{package_path}/share/locale/rw/LC_MESSAGES/bfd.mo
%{package_path}/share/locale/rw/LC_MESSAGES/binutils.mo
%{package_path}/share/locale/rw/LC_MESSAGES/gas.mo
%{package_path}/share/locale/rw/LC_MESSAGES/gprof.mo
%{package_path}/share/locale/sk/LC_MESSAGES/binutils.mo
%{package_path}/share/locale/sr/LC_MESSAGES/gprof.mo
%{package_path}/share/locale/sv/LC_MESSAGES/bfd.mo
%{package_path}/share/locale/sv/LC_MESSAGES/binutils.mo
%{package_path}/share/locale/sv/LC_MESSAGES/gprof.mo
%{package_path}/share/locale/sv/LC_MESSAGES/ld.mo
%{package_path}/share/locale/sv/LC_MESSAGES/opcodes.mo
%{package_path}/share/locale/tr/LC_MESSAGES/bfd.mo
%{package_path}/share/locale/tr/LC_MESSAGES/binutils.mo
%{package_path}/share/locale/tr/LC_MESSAGES/gas.mo
%{package_path}/share/locale/tr/LC_MESSAGES/gprof.mo
%{package_path}/share/locale/tr/LC_MESSAGES/ld.mo
%{package_path}/share/locale/tr/LC_MESSAGES/opcodes.mo
%{package_path}/share/locale/uk/LC_MESSAGES/bfd.mo
%{package_path}/share/locale/uk/LC_MESSAGES/binutils.mo
%{package_path}/share/locale/uk/LC_MESSAGES/gprof.mo
%{package_path}/share/locale/uk/LC_MESSAGES/ld.mo
%{package_path}/share/locale/uk/LC_MESSAGES/opcodes.mo
%{package_path}/share/locale/vi/LC_MESSAGES/bfd.mo
%{package_path}/share/locale/vi/LC_MESSAGES/binutils.mo
%{package_path}/share/locale/vi/LC_MESSAGES/gold.mo
%{package_path}/share/locale/vi/LC_MESSAGES/gprof.mo
%{package_path}/share/locale/vi/LC_MESSAGES/ld.mo
%{package_path}/share/locale/vi/LC_MESSAGES/opcodes.mo
%{package_path}/share/locale/zh_CN/LC_MESSAGES/bfd.mo
%{package_path}/share/locale/zh_CN/LC_MESSAGES/binutils.mo
%{package_path}/share/locale/zh_CN/LC_MESSAGES/ld.mo
%{package_path}/share/locale/zh_CN/LC_MESSAGES/opcodes.mo
%{package_path}/share/locale/zh_TW/LC_MESSAGES/binutils.mo
%{package_path}/share/locale/zh_TW/LC_MESSAGES/ld.mo
%{package_path}/share/man/man1/addr2line.1
%{package_path}/share/man/man1/ar.1
%{package_path}/share/man/man1/as.1
%{package_path}/share/man/man1/c++filt.1
%{package_path}/share/man/man1/dlltool.1
%{package_path}/share/man/man1/elfedit.1
%{package_path}/share/man/man1/gprof.1
%{package_path}/share/man/man1/ld.1
%{package_path}/share/man/man1/nlmconv.1
%{package_path}/share/man/man1/nm.1
%{package_path}/share/man/man1/objcopy.1
%{package_path}/share/man/man1/objdump.1
%{package_path}/share/man/man1/ranlib.1
%{package_path}/share/man/man1/readelf.1
%{package_path}/share/man/man1/size.1
%{package_path}/share/man/man1/strings.1
%{package_path}/share/man/man1/strip.1
%{package_path}/share/man/man1/windmc.1
%{package_path}/share/man/man1/windres.1
%{package_path}/x86_64-redhat-linux/bin/ar
%{package_path}/x86_64-redhat-linux/bin/as
%{package_path}/x86_64-redhat-linux/bin/ld
%{package_path}/x86_64-redhat-linux/bin/ld.bfd
%{package_path}/x86_64-redhat-linux/bin/ld.gold
%{package_path}/x86_64-redhat-linux/bin/nm
%{package_path}/x86_64-redhat-linux/bin/objcopy
%{package_path}/x86_64-redhat-linux/bin/objdump
%{package_path}/x86_64-redhat-linux/bin/ranlib
%{package_path}/x86_64-redhat-linux/bin/strip
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf32_x86_64.x
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf32_x86_64.xbn
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf32_x86_64.xc
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf32_x86_64.xd
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf32_x86_64.xdc
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf32_x86_64.xdw
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf32_x86_64.xn
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf32_x86_64.xr
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf32_x86_64.xs
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf32_x86_64.xsc
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf32_x86_64.xsw
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf32_x86_64.xu
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf32_x86_64.xw
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf_i386.x
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf_i386.xbn
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf_i386.xc
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf_i386.xd
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf_i386.xdc
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf_i386.xdw
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf_i386.xn
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf_i386.xr
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf_i386.xs
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf_i386.xsc
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf_i386.xsw
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf_i386.xu
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf_i386.xw
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf_k1om.x
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf_k1om.xbn
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf_k1om.xc
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf_k1om.xd
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf_k1om.xdc
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf_k1om.xdw
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf_k1om.xn
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf_k1om.xr
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf_k1om.xs
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf_k1om.xsc
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf_k1om.xsw
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf_k1om.xu
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf_k1om.xw
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf_l1om.x
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf_l1om.xbn
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf_l1om.xc
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf_l1om.xd
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf_l1om.xdc
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf_l1om.xdw
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf_l1om.xn
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf_l1om.xr
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf_l1om.xs
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf_l1om.xsc
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf_l1om.xsw
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf_l1om.xu
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf_l1om.xw
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf_x86_64.x
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf_x86_64.xbn
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf_x86_64.xc
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf_x86_64.xd
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf_x86_64.xdc
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf_x86_64.xdw
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf_x86_64.xn
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf_x86_64.xr
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf_x86_64.xs
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf_x86_64.xsc
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf_x86_64.xsw
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf_x86_64.xu
%{package_path}/x86_64-redhat-linux/lib/ldscripts/elf_x86_64.xw
%{package_path}/x86_64-redhat-linux/lib/ldscripts/i386linux.x
%{package_path}/x86_64-redhat-linux/lib/ldscripts/i386linux.xbn
%{package_path}/x86_64-redhat-linux/lib/ldscripts/i386linux.xn
%{package_path}/x86_64-redhat-linux/lib/ldscripts/i386linux.xr
%{package_path}/x86_64-redhat-linux/lib/ldscripts/i386linux.xu
