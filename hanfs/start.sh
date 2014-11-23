#!/bin/sh

if [ "$(uname -n)" == "g01.local" ] ; then
	gluster peer probe g02.local
	# Because we are only a two node
	pcs property set stonith-enabled=false
	pcs property set no-quorum-policy=ignore

	# Because we are only testing
	pcs resource defaults migration-threshold=1

	# Add the virtual ip
	pcs resource create ClusterIP \
		ocf:heartbeat:IPaddr2 \
		ip=10.10.10.100 \
		cidr_netmask=24 \
		op monitor interval=10s

	# Failback to default
	pcs resource defaults resource-stickiness=100
	pcs constraint location ClusterIP prefers g01.local
	pcs status
elif [ "$(uname -n)" == "client.local" ] ; then
	echo "Connecting"
else
	# Set up gluster as a 2 brick replicate
	gluster volume create gv0 replica 2 g02.local:/data/brick1/gv0 g01.local:/data/brick1/gv0 force
	gluster volume set gv0 auth.allow 10.10.10.10
	gluster volume set gv0 nfs.rpc-auth-allow 10.10.10.10
	gluster volume set gv0 nfs.trusted-sync on
	gluster volume set gv0 nfs.disable false

	# Profile
	gluster volume profile gv0 start

	# Start
	gluster volume gv0 start
	gluster volume info
fi
