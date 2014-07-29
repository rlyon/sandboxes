#!/bin/sh

cd
if ! [[ -f epel-release-6-8.noarch.rpm ]] ; then
	wget http://download.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm
	yum -y localinstall epel-release-6-8.noarch.rpm
fi

yum -y install gcc make rpmdevtools rpmlint deltarpm rpm-build mock
usermod -G mock vagrant