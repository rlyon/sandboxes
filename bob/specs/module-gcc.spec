%define package_name 	gcc
%define package_version	4.8.3
%define package_type 	module

%define compiler_family		gcc
%define compiler_version 	4.8.3
%define compiler_prefix  	%{package_type}-%{compiler_family}-%{compiler_version}

%define software_path	/opt/software
%define package_path	%{software_path}/%{package_type}/%{compiler_family}/%{compiler_version}
%define module_path		/opt/software/modulefiles


Summary: A module wrapper for %{package_name} version %{package_version}
Name: %{compiler_prefix}
Version: 2
Release: 0%{?dist}
License: MIT
Group: System Environment/Libraries
URL: ftp://gcc.gnu.org/pub/gcc/infrastructure
Vendor: CentOS
Packager: Rob Lyon <rob.lyon@wsu.edu>
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: environment-modules
Requires: environment-modules
Requires: compilers-gcc-4.8.3-core

%description
A module wrapper for %{package_name} version %{package_version}

%install
mkdir -p %{buildroot}%{module_path}/%{package_name}
cat > %{buildroot}%{module_path}/%{package_name}/%{package_version} << 'EOF'
#%Module######################################################################
proc ModulesHelp { } {
puts stderr "This modulefile defines the paths needed to use: "
puts stderr "%{package_name} version %{package_version}"
puts stderr ""
}

set %{package_name}_version %{package_version}
set software_dir /opt/software
set compilers_dir $software_dir/compilers
set module_dir $compilers_dir/%{package_name}/%{package_version}

prepend-path PATH $module_dir/bin
# prepend-path LD_LIBRARY_PATH $module_dir/lib
# prepend-path LD_LIBRARY_PATH $module_dir/lib64
prepend-path INFOPATH $module_dir/info
prepend-path MANPATH $module_dir/share/man

setenv M_CFLAGS 	"-I $module_dir/include -L $module_dir/lib"
setenv M_CXXFLAGS 	"-I $module_dir/include -L $module_dir/lib"
setenv M_LDFLAGS	"-Wl,-rpath=$module_dir/lib -L $module_dir/lib"
setenv M_INCLUDE	"-I $module_dir/include"
setenv M_OPTIMIZE	"-O2 -ffast-math -fomit-frame-pointer -funroll-loops -mtune=generic"
EOF

%files
%defattr(-,software,software)
%{module_path}/%{package_name}/%{package_version}