function mock_init {
	/usr/bin/mock -r $1 --init
}

function run_as {
	user=$1
	shift
	sudo -u $user -i bash "$@"
}

function mock_rebuild {
	repo=$1
	version=$2
	arch=$3
	specfile=$4
	sourcefile=$5
	pushd ~
	echo '%_topdir %(pwd)' > ~/.rpmmacros
	mkdir -p package/{BUILD,RPMS,SOURCES,SRPMS,SPECS}

	pushd package
	cp $specfile SPECS/.
	cp $sourcefile SOURCES/.

	basefile=`basename $specfile`
	rpmbuild --nodeps -bs SPECS/$basefile -D 'dist 0'

	/usr/bin/mock -r $repo-$version-$arch --rebuild SRPMS/*.src.rpm
	mv /var/lib/mock/$repo-$version-$arch/result/*.src.rpm /yumrepo/wsurel/el$version/SRPMS
	cp /var/lib/mock/$repo-$version-$arch/result/*.rpm /yumrepo/wsurel/el$version/$arch
	createrepo /yumrepo/wsurel/el$version/$arch
	popd
	rm -rf package
	popd
}

function add_packages {
	repo=$1
	version=$2
	arch=$3
	mv /var/lib/mock/$repo-$version-$arch/results/*.src.rpm /yumrepo/wsurel/el$version/SRPMS
	cp /var/lib/mock/$repo-$version-$arch/results/*.rpm /yumrepo/wsurel/el$version/$arch
	createrepo /yumrepo/wsurel/el$version/$arch
}

function create_repo {
	repo=$1
	version=$2
	arch=$3
}
