function mock_init {
	/usr/bin/mock -r $1 --init
}

function mock_rebuild {
	repo=$1
	version=$2
	arch=$3
	specfile=$4
	sourcefile=$5

	mkdir -p package/{BUILD,RPMS,SOURCES,SRPMS,SPECS}
	cd package

	cp $specfile SPECS/.
	cp $sourcefile SOURCE/.

	rpmbuild --nodeps -bs /SPECS/`basename $specfile` -D 'dist 0'

	/usr/bin/mock -r $repo-$version-$arch --rebuild SRPMS/*.src.rpm
	mv /var/lib/mock/$repo-$version-$arch/results/*.src.rpm /yumrepo/wsurel/el$version/SRPMS
	cp /var/lib/mock/$repo-$version-$arch/results/*.rpm /yumrepo/wsurel/el$version/$arch

	createrepo /yumrepo/wsurel/el$version/$arch
}