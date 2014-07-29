#!/bin/sh

cd
if ! [[ -f epel-release-5-4.noarch.rpm ]] ; then
	wget http://download.fedoraproject.org/pub/epel/5/i386/epel-release-5-4.noarch.rpm
	yum -y localinstall epel-release-5-4.noarch.rpm
fi

yum -y install gcc make rpmdevtools rpmlint deltarpm rpm-build mock
usermod -G mock vagrant
