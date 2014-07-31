#!/bin/sh

cd
mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SRPMS,SPECS}
cp /vagrant/Lmod.spec ~/rpmbuild/SPECS/.
cp /vagrant/Lmod-* ~/rpmbuild/SOURCES/.

echo '%_topdir %(echo $HOME)/rpmbuild' > ~/.rpmmacros

cp /etc/mock/epel-5-i386 /etc/mock/wsurel-5-i386
cp /etc/mock/epel-5-x86_64 /etc/mock/wsurel-5-x86_64
cp /etc/mock/epel-6-i386 /etc/mock/wsurel-6-i386
cp /etc/mock/epel-6-x86_64 /etc/mock/wsurel-6-x86_64


echo "Initializing up mock.  This will take a while"
mock -r wsurel-5-i386 --init
mock -r wsurel-5-x86_64 --init
mock -r wsurel-6-i386 --init
mock -r wsurel-6-x86_64 --init

rpmbuild --nodeps -bs ~/rpmbuild/SPECS/Lmod.spec
mock -r wsurel-5-i386 --rebuild /home/vagrant/rpmbuild/SRPMS/Lmod-5.6.3-1.src.rpm

# push over to repo and create