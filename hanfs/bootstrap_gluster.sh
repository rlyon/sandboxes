#!/bin/sh

cp /vagrant/hosts /etc/hosts

cd
if ! [[ -f epel-release-6-8.noarch.rpm ]] ; then
	wget http://download.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm
	yum -y localinstall epel-release-6-8.noarch.rpm
fi

if ! [[ -f /etc/yum.repos.d/glusterfs.repo ]] ; then 
	curl http://download.gluster.org/pub/gluster/glusterfs/3.6/LATEST/EPEL.repo/glusterfs-epel.repo > /etc/yum.repos.d/glusterfs.repo
fi

sed -i -e 's/SELINUX=enforcing/SELINUX=disabled/' /etc/selinux/config

yum -y install glusterfs
yum -y install glusterfs-server
mkdir -p /data/brick1/gv0
/etc/init.d/glusterd start
chkconfig glusterd on

yum -y install corosync
yum -y install pacemaker
yum -y install cman

cp /vagrant/cluster.conf /etc/cluster/cluster.conf
cp /vagrant/corosync.conf /etc/corosync/corosync.conf
cp /vagrant/pcmk /etc/corosync/service.d/pcmk

/etc/init.d/cman start
chkconfig cman on


