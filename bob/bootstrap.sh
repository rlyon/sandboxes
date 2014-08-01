#!/bin/sh

cd
if ! [[ -f epel-release-6-8.noarch.rpm ]] ; then
	wget http://download.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm
	yum -y localinstall epel-release-6-8.noarch.rpm
fi

yum -y install yum-utils rpmdevtools rpmlint deltarpm rpm-build mock
yum -y install gcc make 
yum -y install nginx

mkdir -p /yumrepo/wsurel/{el5,el6}/{i386,x86_64}
chown -R vagrant:vagrant /yumrepo

cat > /etc/nginx/nginx.conf << 'EOF'
user              vagrant;
worker_processes  1;
error_log  /var/log/nginx/error.log;
pid        /var/run/nginx.pid;

events {
    worker_connections  1024;
}

http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;
    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';
    access_log  /var/log/nginx/access.log  main;
    sendfile        on;
    keepalive_timeout  65;
    
    server {
    	listen 80 default_server; 
    	index index.html;
    	root /yumrepo;
    	autoindex on;
    }
}
EOF

cat > /etc/yum.repos.d/wsurel << 'EOF'
name=IBEST Enterprise Linux - $basearch
baseurl=http://localhost/wsurel/el$releasever/$basearch
failovermethod=priority
enabled=1
gpgcheck=0
EOF

usermod -G mock vagrant
cp /etc/mock/epel-5-i386.cfg /etc/mock/wsurel-5-i386.cfg
sed -i -e 's/epel-5-i386/wsurel-5-i386/g' /etc/mock/wsurel-5-i386.cfg
cp /etc/mock/epel-5-x86_64.cfg /etc/mock/wsurel-5-x86_64.cfg
sed -i -e 's/epel-5-x86_64/wsurel-5-x86_64/g' /etc/mock/wsurel-5-x86_64.cfg
cp /etc/mock/epel-6-i386.cfg /etc/mock/wsurel-6-i386.cfg
sed -i -e 's/epel-6-i386/wsurel-6-i386/g' /etc/mock/wsurel-6-i386.cfg
cp /etc/mock/epel-6-x86_64.cfg /etc/mock/wsurel-6-x86_64.cfg
sed -i -e 's/epel-6-x86_64/wsurel-6-x86_64/g' /etc/mock/wsurel-6-x86_64.cfg

mkdir -p /etc/skel/buildroot.clean/{BUILD,RPMS,SOURCES,SRPMS,SPECS}
sudo -u vagrant -i bash <<'EOL'
cd
cp -r /etc/skel/buildroot.clean ~/lmod 
cp /vagrant/Lmod.spec ~/lmod/SPECS/.
cp /vagrant/Lmod-* ~/lmod/SOURCES/.

echo '%_topdir %(pwd)' > ~/.rpmmacros

echo "Initializing up mock.  This will take a while"

echo "Initializing wsurel-5-i386"
/usr/bin/mock -r wsurel-5-i386 --init
echo "Initializing wsurel-5-x86_64"
/usr/bin/mock -r wsurel-5-x86_64 --init
echo "Initializing wsurel-6-i386"
/usr/bin/mock -r wsurel-6-i386 --init
echo "Initializing wsurel-6-x86_64"
/usr/bin/mock -r wsurel-6-x86_64 --init

cd lmod
rpmbuild --nodeps -bs ~/rpmbuild/SPECS/Lmod.spec -D 'dist 0'
/usr/bin/mock -r wsurel-5-i386 --rebuild ~/rpmbuild/SRPMS/Lmod-5.6.3-1.src.rpm
/usr/bin/mock -r wsurel-5-x86_64 --rebuild ~/rpmbuild/SRPMS/Lmod-5.6.3-1.src.rpm
/usr/bin/mock -r wsurel-6-i386 --rebuild ~/rpmbuild/SRPMS/Lmod-5.6.3-1.src.rpm
/usr/bin/mock -r wsurel-6-x86_64 --rebuild ~/rpmbuild/SRPMS/Lmod-5.6.3-1.src.rpm

# next create the repo

EOL

# rpmbuild --nodeps -bs ~/rpmbuild/SPECS/Lmod.spec
# mock -r wsurel-5-i386 --rebuild /home/vagrant/rpmbuild/SRPMS/Lmod-5.6.3-1.src.rpm

# push over to repo and create
