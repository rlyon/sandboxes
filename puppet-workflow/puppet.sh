#!/bin/sh

cd /tmp

curl http://yum.puppetlabs.com/puppetlabs-release-el-7.noarch.rpm -O puppetlabs-release-el-7.noarch.rpm

yum -y install puppetlabs-release-el-7.noarch.rpm
yum -y update
yum -y install puppet-server

puppet apply /vagrant/puppet.pp
puppet module install puppetlabs/inifile
puppet module install zack/r10k

git clone https://github.com/rlyon/puppet-control.git
puppet apply puppet-control/configure_r10k.pp
puppet apply puppet-control/configure_directory_environments.pp

r10k deploy environment -pv
