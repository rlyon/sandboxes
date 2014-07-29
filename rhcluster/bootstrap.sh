#!/bin/sh
yum -y install rgmanager lvm2-cluster gfs2-utils
yum -y install luci

cp /vagrant/cluster.conf /etc/cluster/cluster.conf
cp /vagrant/hosts /etc/hosts
