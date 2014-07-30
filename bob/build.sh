#!/bin/sh

cd
mkdir -p rpmbuild/{BUILD,RPMS,SOURCES,SRPMS,SPECS}
cp /vagrant/lmod.spec rpmbuild/SPECS/.
cp /vagrant/Lmod-* rpmbuild/SOURCES/.

cd rpmbuild/SPECS/
rpmbuild -ba lmod.spec