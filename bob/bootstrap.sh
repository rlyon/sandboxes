#!/bin/sh

cd
if ! [[ -f epel-release-6-8.noarch.rpm ]] ; then
	wget http://download.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm
	yum -y localinstall epel-release-6-8.noarch.rpm
fi

yum -y install createrepo yum-utils rpmdevtools rpmlint deltarpm rpm-build mock
yum -y install gcc make 

mkdir -p /yumrepo/wsurel/{el5,el6}/{i386,x86_64}
createrepo /yumrepo/wsurel/el5/i386
createrepo /yumrepo/wsurel/el5/x86_64
createrepo /yumrepo/wsurel/el6/i386
createrepo /yumrepo/wsurel/el6/x86_64
chown -R vagrant:vagrant /yumrepo
mkdir -p /etc/skel/buildroot.clean/{BUILD,RPMS,SOURCES,SRPMS,SPECS}

yum -y install nginx
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
service nginx start
chkconfig nginx on

cat > /etc/yum.repos.d/wsurel.repo << 'EOF'
[wsurel]
name=IBEST Enterprise Linux - $basearch
baseurl=http://localhost/wsurel/el$releasever/$basearch
failovermethod=priority
enabled=1
gpgcheck=0
EOF

usermod -G mock vagrant

echo "Configuring mock environments.  This will take a while"

echo "Configuring wsurel-5-i386"
head -n -1 /etc/mock/epel-5-i386.cfg | sed -e '$a\\' > /etc/mock/wsurel-5-i386.cfg
cat /etc/yum.repos.d/wsurel.repo | sed -e '$a\"""\' >> /etc/mock/wsurel-5-i386.cfg
sed -i -e 's/epel-5-i386/wsurel-5-i386/g' /etc/mock/wsurel-5-i386.cfg
/usr/bin/mock -r wsurel-5-i386 --init

echo "Configuring wsurel-5-x86_64"
head -n -1 /etc/mock/epel-5-x86_64.cfg | sed -e '$a\\' > /etc/mock/wsurel-5-x86_64.cfg
cat /etc/yum.repos.d/wsurel.repo | sed -e '$a\"""\' >> /etc/mock/wsurel-5-x86_64.cfg
sed -i -e 's/epel-5-x86_64/wsurel-5-x86_64/g' /etc/mock/wsurel-5-x86_64.cfg
/usr/bin/mock -r wsurel-5-x86_64 --init

echo "Configuring wsurel-6-i386"
head -n -1 /etc/mock/epel-6-i386.cfg | sed -e '$a\\' > /etc/mock/wsurel-6-i386.cfg
cat /etc/yum.repos.d/wsurel.repo | sed -e '$a\"""\' >> /etc/mock/wsurel-6-i386.cfg
sed -i -e 's/epel-6-i386/wsurel-6-i386/g' /etc/mock/wsurel-6-i386.cfg
/usr/bin/mock -r wsurel-6-i386 --init

echo "Configuring wsurel-6-x86_64"
head -n -1 /etc/mock/epel-6-x86_64.cfg | sed -e '$a\\' > /etc/mock/wsurel-6-x86_64.cfg
cat /etc/yum.repos.d/wsurel.repo | sed -e '$a\"""\' >> /etc/mock/wsurel-6-x86_64.cfg
sed -i -e 's/epel-6-x86_64/wsurel-6-x86_64/g' /etc/mock/wsurel-6-x86_64.cfg
/usr/bin/mock -r wsurel-6-x86_64 --init

sudo -u vagrant -i bash <<'EOL'
source /vagrant/functions.sh
mock_build_all /vagrant environment-modules 
EOL
