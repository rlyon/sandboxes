#!/bin/sh
cd
if ! [[ -f epel-release-6-8.noarch.rpm ]] ; then
	wget http://download.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm
	yum -y localinstall epel-release-6-8.noarch.rpm
fi
yum -y install openssl libxml2 tcsh postfix

# wget http://dl.dropbox.com/u/47200624/respin/ge2011.11.tar.gz
cp /vagrant/ge2011.11.tar.gz /opt
cd /opt
tar zxvf ge2011.11.tar.gz
ln -sf /opt/ge2011.11 /opt/gridengine
rm -f ge2011.11.tar.gz

cat > /etc/profile.d/gridengine.sh << 'EOF'
## Gridengine paths
export SGE_ROOT=/opt/gridengine
export PATH=$SGE_ROOT/bin/linux-x64:$PATH
EOF

cat > /etc/profile.d/gridengine.csh << 'EOF'
## Gridengine paths
setenv SGE_ROOT "/opt/gridengine"
setenv PATH "$SGE_ROOT/bin/linux-x64:$PATH"
EOF

source /etc/profile

cp /vagrant/hosts /etc/hosts

cat > /etc/ssh/ssh_host_rsa_key << 'EOF'
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAv+VDpocINo7EnBb6PWeSCVvzxi3kNxo8uLpM04ZZUEKXYv8O
kbRc+MLiBKuOHscXSdiwP016gMVCyVQmyrggUEQ1KvDSZFHDLcSSheuEiCTyxGdc
0nFSG2E6AS+fth3zjL1mIj+G0U7FNHv4EVScNCFSpBQUsJwPpX9GRHtvpEZmtPgy
snz5WCCv/7lCnKQubQRVffE2V24Kg2x4anUF23xaOJU75ZAi3uIZBrOOdQJKUqTL
pUIcqE6BU3U0kqx+9hkPQYj/FhWyqn2GB9N+h8u6uvbEcsVtNPxWJEdE2/4rDjQB
MHy6kXC6n2MG/q4gMVyLVy7IuP4vBccEOracewIBIwKCAQAFe5Q39Tq/uu+ssDMJ
EZZ1S8Ui615Kt5tVvC4UrBEuLcnPoOMovAKoBZFt2QQPggf6y61DoyDB2cAUYX1z
gZqF81H56Z+cd11ZFD6zXoAhJaCJRMgjRRD5d851D/0/t7aAXS7Nx0z+qnqpumYs
YYDOShhN1LAiTZoMCvNhCtdN1hNtHeS257M3omtufUqJIBTMbI2bZovqMNMSEmSQ
f3DlN/q+YYct4RD9NZoMVRclGkApvmEslo+rEwT4dsUmPvQgz+7hi/ReZDYi2ifP
Ssn+YRPdP72zrXy711UuSw74EskDqxiimf4UjFdeDjeAIUpeK20gYzbFx/A0NocO
0UR7AoGBAPtRfEnAhVh9kiEy5XEN3EE895SeFa3ECpIEoVinfHlnzM/2fK7Ghya+
RvyT+gMyMVr7p9XuQPJuhx6oSj0kFmhkuFpenExuBC2WSJDQlUG3jorsSd9qA3ne
7pqhyuD2i08d2pi8cwMP2X9gbWGF+3cPEjRJffGnxNd5IIiPwwlpAoGBAMN4ZaPw
SiA/Wd6xsqDPZRU9NWSg1meOtp0GR2ABjB0dCEI6wxHZQ6mCRwzDF2EwOimh9aye
a4XWLbSy7gMz+rYU8wwMyknAXh5QYYPgBJ8I93iO9fV4CeWnnRYuOVf64WBv9Qo4
+/qyZ0ljBA70JX5CWmugIFoG44BpMgSkVzZDAoGAFYqkQNX8zRIT1vW75R5x9vaY
4NpZoS4PiNvTUL3mGQjlq2zmHZv89LE5SNl71GNjUPD/weE4xFKd3g5sw2l+Q3ZY
8c2YXlKSpNJd/ci8VhcMN8scRlmLRPXZ7/89RnuISJworgGGM3ZjGYvsHk1QEYTy
7on02jLznXDIRjg1SfMCgYEAgHOwgayIe5dYUINmwXJYXmoNJN64x7WN8iiyj4v8
/TBV4mEhGluS3RsYvz5f0icBplR83yZGqGgsqfHs3YiOz2zaOx5ZC+TQIoyX2lFi
H12p8CNubhuuu3zGUGeExMlviIQWDggwjs0CC6d3sg4nRFd9P2k51MKywhk+IE68
98UCgYEAg1KhVJNAVpagJgDI6IPLkXriODYjf3JtkK4rGVvJfwqOii/mxru7Bs7R
xGER8BSnUPKgCEaXpP+Uq5N5yZG0ihN7oAj3sVwkvu3x3FLvBhvEK4KimcDeEpCa
zY/LPurdYcBWhIeNT8aRwBxC1iJ07CfKhVT7lxqT6LsXWiT4tOs=
-----END RSA PRIVATE KEY-----
EOF

cat > /etc/ssh/ssh_host_rsa_key.pub << 'EOF'
ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAv+VDpocINo7EnBb6PWeSCVvzxi3kNxo8uLpM04ZZUEKXYv8OkbRc+MLiBKuOHscXSdiwP016gMVCyVQmyrggUEQ1KvDSZFHDLcSSheuEiCTyxGdc0nFSG2E6AS+fth3zjL1mIj+G0U7FNHv4EVScNCFSpBQUsJwPpX9GRHtvpEZmtPgysnz5WCCv/7lCnKQubQRVffE2V24Kg2x4anUF23xaOJU75ZAi3uIZBrOOdQJKUqTLpUIcqE6BU3U0kqx+9hkPQYj/FhWyqn2GB9N+h8u6uvbEcsVtNPxWJEdE2/4rDjQBMHy6kXC6n2MG/q4gMVyLVy7IuP4vBccEOracew== 
EOF

cat > /etc/ssh/sshd_config << 'EOF'
Protocol 2
SyslogFacility AUTHPRIV
RhostsRSAAuthentication yes
HostbasedAuthentication yes
HostbasedUsesNameFromPacketOnly yes
IgnoreUserKnownHosts yes
IgnoreRhosts no
PasswordAuthentication yes
ChallengeResponseAuthentication no
GSSAPIAuthentication yes
GSSAPICleanupCredentials yes
UsePAM yes
AcceptEnv LANG LC_CTYPE LC_NUMERIC LC_TIME LC_COLLATE LC_MONETARY LC_MESSAGES
AcceptEnv LC_PAPER LC_NAME LC_ADDRESS LC_TELEPHONE LC_MEASUREMENT
AcceptEnv LC_IDENTIFICATION LC_ALL LANGUAGE
AcceptEnv XMODIFIERS
X11Forwarding yes
Subsystem sftp /usr/libexec/openssh/sftp-server
UseDNS no
GSSAPIAuthentication no
EOF

cat > /etc/ssh/ssh_config << 'EOF'
Host * 
		PreferredAuthentications hostbased,publickey,keyboard-interactive,password
        HostbasedAuthentication yes
        EnableSSHKeysign yes
EOF

# For vagrant test boxes.
cat > /etc/ssh/ssh_known_hosts << 'EOF'
its-genomics-hn ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAv+VDpocINo7EnBb6PWeSCVvzxi3kNxo8uLpM04ZZUEKXYv8OkbRc+MLiBKuOHscXSdiwP016gMVCyVQmyrggUEQ1KvDSZFHDLcSSheuEiCTyxGdc0nFSG2E6AS+fth3zjL1mIj+G0U7FNHv4EVScNCFSpBQUsJwPpX9GRHtvpEZmtPgysnz5WCCv/7lCnKQubQRVffE2V24Kg2x4anUF23xaOJU75ZAi3uIZBrOOdQJKUqTLpUIcqE6BU3U0kqx+9hkPQYj/FhWyqn2GB9N+h8u6uvbEcsVtNPxWJEdE2/4rDjQBMHy6kXC6n2MG/q4gMVyLVy7IuP4vBccEOracew== 
its-genomics-n01 ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAv+VDpocINo7EnBb6PWeSCVvzxi3kNxo8uLpM04ZZUEKXYv8OkbRc+MLiBKuOHscXSdiwP016gMVCyVQmyrggUEQ1KvDSZFHDLcSSheuEiCTyxGdc0nFSG2E6AS+fth3zjL1mIj+G0U7FNHv4EVScNCFSpBQUsJwPpX9GRHtvpEZmtPgysnz5WCCv/7lCnKQubQRVffE2V24Kg2x4anUF23xaOJU75ZAi3uIZBrOOdQJKUqTLpUIcqE6BU3U0kqx+9hkPQYj/FhWyqn2GB9N+h8u6uvbEcsVtNPxWJEdE2/4rDjQBMHy6kXC6n2MG/q4gMVyLVy7IuP4vBccEOracew== 
its-genomics-n02 ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAv+VDpocINo7EnBb6PWeSCVvzxi3kNxo8uLpM04ZZUEKXYv8OkbRc+MLiBKuOHscXSdiwP016gMVCyVQmyrggUEQ1KvDSZFHDLcSSheuEiCTyxGdc0nFSG2E6AS+fth3zjL1mIj+G0U7FNHv4EVScNCFSpBQUsJwPpX9GRHtvpEZmtPgysnz5WCCv/7lCnKQubQRVffE2V24Kg2x4anUF23xaOJU75ZAi3uIZBrOOdQJKUqTLpUIcqE6BU3U0kqx+9hkPQYj/FhWyqn2GB9N+h8u6uvbEcsVtNPxWJEdE2/4rDjQBMHy6kXC6n2MG/q4gMVyLVy7IuP4vBccEOracew== 
EOF
# For others, just scp the files over from the headnode or use
# ssh-keyscan -vt rsa host.example.com >> /etc/ssh/ssh_known_hosts

grep "cluster" /etc/hosts | awk -F' ' '{print $3}' > /etc/hosts.equiv
ln -sf /etc/hosts.equiv /etc/ssh/shosts.equiv
ln -s /etc/hosts.equiv /root/.shosts

service sshd restart
######
yum -y install nfs-utils

cat > /etc/exports << 'EOF'
/opt/gridengine  10.10.10.0/24(rw,no_root_squash,sync)
/home            10.10.10.0/24(rw,no_root_squash,async)
EOF

chkconfig nfs on
chkconfig rpcbind on
service rpcbind start
service nfs start

######
cd /opt/gridengine
./inst_sge -m -auto /vagrant/sge_install.conf

