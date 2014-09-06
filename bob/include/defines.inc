%define  debug_package %{nil}

%global software_path 	/opt/software
%global modulefile_path %{software_path}/modulefiles
%global compilers compilers

%if "%{family}" == "gcc48"
	%define compiler_family 	gcc48
	%define compiler_name   	gcc
	%define compiler_version 	4.8
%endif

%if "%{is_library}" == "1"
	%define package_name %{compiler_family}-%{name}
	%define install_path %{software_path}/compilers/%{compiler_family}
%endif

%global _prefix             %{install_path}
%global _exec_prefix        %{install_path}
%global _bindir             %{install_path}/bin
%global _sbindir            %{install_path}/sbin      
%global _datadir            %{install_path}/share
%global _defaultdocdir      %{install_path}/doc
%global _includedir         %{install_path}/include
%global _infodir            %{install_path}/info
%global _libdir             %{install_path}/lib
%global _libexecdir         %{install_path}/libexec
%global _localstatedir      %{install_path}/var
%global _mandir             %{install_path}/man
%global _sharedstatedir     %{install_path}/com
%global _sysconfdir         %{install_path}/etc
%global _modulefiledir		%{software_path}/modulefiles

%if "%{dist}" == ".el5.centos"
	%define dist .el5
%endif
