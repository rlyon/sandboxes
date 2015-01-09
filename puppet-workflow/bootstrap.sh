#!/bin/bash

cat > /etc/hosts << 'EOF'
127.0.0.1   gitlab.local gitlab localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
10.10.1.41  gitlab.local.vm gitlab
10.10.1.42  puppet.local.vm puppet
10.10.1.43  client.local.vm client
10.10.1.44  jenkins.local.vm jenkins
EOF

INSTALL_PATH="/vagrant/${hostname}"
sh ISNTALL_PATH=""
