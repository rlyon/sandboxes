function mock_init {
	/usr/bin/mock -r $1 --init
}

function run_as {
	user=$1
	shift
	sudo -u $user -i bash "$@"
}

function gcc_deps_rebuild {
	version_file=$1
	source $version_file
	# Build GMP
	mock_rebuild_all /vagrant/gmp.spec /usr/local/src/gmp-4.3.2.tar.gz
	mock_rebuild_all /vagrant/mpfr.spec /usr/local/src/mpfr-2.4.2.tar.gz
	mock_rebuild_all /vagrant/mpc.spec /usr/local/src/mpc-0.8.1.tar.gz
	mock_rebuild_all /vagrant/isl.spec /usr/local/src/isl-0.12.2.tar.gz
	mock_rebuild_all /vagrant/cloog.spec /usr/local/src/cloog-0.18.1.tar.gz
	mock_rebuild_all /vagrant/zlib.spec /usr/local/src/zlib-1.2.8.tar.gz
}

function mock_rebuild_all {
	for version in 5 6 ; do
		for arch in i386 x86_64 ; do
			echo "Building for wsurel-$version-$arch"
			mock_rebuild wsurel $version $arch $1 $2
		done
	done
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
