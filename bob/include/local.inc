%global _prefix             /usr/local
%global _exec_prefix        %{_prefix}
%global _bindir             %{_exec_prefix}/bin
%global _sbindir            %{_exec_prefix}/sbin      
%global _datadir            %{_prefix}/share
%global _defaultdocdir      %{_prefix}/share/doc
%global _includedir         %{_prefix}/include
%global _infodir            %{_prefix}/share/info
%global _libdir             %{_exec_prefix}/%{_lib}
%global _libexecdir         %{_exec_prefix}/libexec
%global _localstatedir      %{_prefix}/var
%global _mandir             %{_prefix}/share/man
%global _sharedstatedir     %{_prefix}/com
%global _sysconfdir         %{_prefix}/etc

%if "%{dist}" == ".el5.centos"
	%define dist .el5
%endif
