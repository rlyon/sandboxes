#!/bin/sh

cat > /etc/hosts << 'EOF'
127.0.0.1   gitlab.local gitlab localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
EOF

cd
if ! [[ -f epel-release-6-8.noarch.rpm ]] ; then
	wget http://download.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm
	yum -y localinstall epel-release-6-8.noarch.rpm
fi

yum -y install openssh-server
yum -y install postfix
yum -y install cronie

service postfix start
chkconfig postfix on


mkdir -p /mnt/nas/gitlab-data

if ! [[ -f gitlab-7.5.3_omnibus.5.2.1.ci-1.el6.x86_64.rpm ]] ; then
	curl -O https://downloads-packages.s3.amazonaws.com/centos-6.6/gitlab-7.5.3_omnibus.5.2.1.ci-1.el6.x86_64.rpm
	yum -y localinstall gitlab-7.5.3_omnibus.5.2.1.ci-1.el6.x86_64.rpm
fi

mkdir -p /etc/gitlab/ssl
cp /vagrant/ssl-insecure/* /etc/gitlab/ssl/.
cp /vagrant/gitlab.rb /etc/gitlab/gitlab.rb

gitlab-ctl reconfigure
lokkit -s https -s http -s ssh

# setsebool -P httpd_can_network_connect on
# setsebool -P httpd_can_network_relay on
# setsebool -P httpd_read_user_content on
# semanage -i - <<EOF
# fcontext -a -t user_home_dir_t '/home/git(/.*)?'
# fcontext -a -t ssh_home_t '/home/git/.ssh(/.*)?'
# fcontext -a -t httpd_sys_content_t '/home/git/gitlab/public(/.*)?'
# fcontext -a -t httpd_sys_content_t '/home/git/repositories(/.*)?'
# EOF
# restorecon -R /home/git
