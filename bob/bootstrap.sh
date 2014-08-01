#!/bin/sh

cd
if ! [[ -f epel-release-6-8.noarch.rpm ]] ; then
	wget http://download.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm
	yum -y localinstall epel-release-6-8.noarch.rpm
fi

yum -y install yum-utils rpmdevtools rpmlint deltarpm rpm-build mock
yum -y install gcc make 
yum -y install nginx

usermod -G mock vagrant

cp /etc/mock/epel-5-i386.cfg /etc/mock/wsurel-5-i386.cfg
cp /etc/mock/epel-5-x86_64.cfg /etc/mock/wsurel-5-x86_64.cfg
cp /etc/mock/epel-6-i386.cfg /etc/mock/wsurel-6-i386.cfg
cp /etc/mock/epel-6-x86_64.cfg /etc/mock/wsurel-6-x86_64.cfg

sudo -u vagrant -i bash <<'EOL'
cd
mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SRPMS,SPECS}
cp /vagrant/Lmod.spec ~/rpmbuild/SPECS/.
cp /vagrant/Lmod-* ~/rpmbuild/SOURCES/.

echo '%_topdir %(echo $HOME)/rpmbuild' > ~/.rpmmacros

echo "Initializing up mock.  This will take a while"
/usr/bin/mock -r wsurel-5-i386 --init
/usr/bin/mock -r wsurel-5-x86_64 --init
/usr/bin/mock -r wsurel-6-i386 --init
/usr/bin/mock -r wsurel-6-x86_64 --init
EOL

# rpmbuild --nodeps -bs ~/rpmbuild/SPECS/Lmod.spec
# mock -r wsurel-5-i386 --rebuild /home/vagrant/rpmbuild/SRPMS/Lmod-5.6.3-1.src.rpm

# push over to repo and create
