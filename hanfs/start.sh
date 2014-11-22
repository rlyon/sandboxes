#!/bin/sh

if [ "$(uname -n)" == "g01.local" ] ; then
	gluster peer probe g02.local
else
	gluster volume create gv0 replica 2 g02.local:/data/brick1/gv0 g01.local:/data/brick1/gv0 force
	gluster volume set gv0 auth.allow 10.10.10.10
	gluster volume info
fi
