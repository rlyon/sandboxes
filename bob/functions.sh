function mock_init {
	/usr/bin/mock -r $1 --init
}

function download_unless_present {
	if ! [[ -f $1 ]] ; then
		wget $2
	fi
}

function run_as {
	user=$1
	shift
	sudo -u $user -i bash "$@"
}

function gcc_deps_rebuild {
	# version_file=$1
	# source $version_file
	# Build GMP
	mock_rebuild_all /vagrant/specs/gmp.spec /usr/local/src/gmp-4.3.2.tar.gz
	mock_rebuild_all /vagrant/specs/mpfr.spec /usr/local/src/mpfr-2.4.2.tar.gz
	mock_rebuild_all /vagrant/specs/mpc.spec /usr/local/src/mpc-0.8.1.tar.gz
	mock_rebuild_all /vagrant/specs/isl.spec /usr/local/src/isl-0.12.2.tar.gz
	mock_rebuild_all /vagrant/specs/cloog.spec /usr/local/src/cloog-0.18.1.tar.gz
	mock_rebuild_all /vagrant/specs/zlib.spec /usr/local/src/zlib-1.2.8.tar.gz
	mock_rebuild_all /vagrant/specs/gcc.spec /usr/local/src/gcc-4.8.3.tar.gz
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
	rpmbuild --nodeps -bs SPECS/$basefile -D 'dist %{nil}'

	/usr/bin/mock -r $repo-$version-$arch --rebuild SRPMS/*.src.rpm
	rm -rf /var/lib/mock/$repo-$version-$arch/result/*-debuginfo*.rpm
	mv /var/lib/mock/$repo-$version-$arch/result/*.src.rpm /yumrepo/wsurel/el$version/SRPMS
	cp /var/lib/mock/$repo-$version-$arch/result/*.rpm /yumrepo/wsurel/el$version/$arch
	createrepo /yumrepo/wsurel/el$version/$arch
	popd
	rm -rf package
	popd
}

function mock_build_all {
	for version in 5 6 ; do
		for arch in i386 x86_64 ; do
			echo "Building for wsurel-$version-$arch"
			mock_build $1 $2 wsurel $version $arch
		done
	done
}

function mock_scrub_all {
	for version in 5 6 ; do
		for arch in i386 x86_64 ; do
			echo "Scrubbing wsurel-$version-$arch"
			/usr/bin/mock -r $repo-$version-$arch --scrub=all
		done
	done
}

function mock_build {
	dir=$1
	name=$2
	repo=$3
	version=$4
	arch=$5

	pushd ${dir}/sources/${name}
	if [[ -f prepare.sh ]] ; then
		sh prepare.sh
	fi
	popd

	pushd ~
	echo '%_topdir %(pwd)' > ~/.rpmmacros
	mkdir -p package/{BUILD,RPMS,SOURCES,SRPMS,SPECS}
	pushd package

	cp ${dir}/specs/${name}.spec SPECS/.
	cp -rf ${dir}/sources/${name}/* SOURCES/.
	rpmbuild --nodeps -bs SPECS/${name}.spec -D 'dist %{nil}'

	/usr/bin/mock -r $repo-$version-$arch --rebuild SRPMS/*.src.rpm
	rm -rf /var/lib/mock/$repo-$version-$arch/result/*-debuginfo*.rpm
	mv /var/lib/mock/$repo-$version-$arch/result/*.src.rpm /yumrepo/wsurel/el$version/SRPMS
	cp /var/lib/mock/$repo-$version-$arch/result/*.rpm /yumrepo/wsurel/el$version/$arch
	createrepo /yumrepo/wsurel/el$version/$arch

	popd
	rm -rf package
	popd
}

function mock_build_module_all {
	for version in 5 6 ; do
		for arch in i386 x86_64 ; do
			echo "Building module for wsurel-$version-$arch"
			mock_build_module $1 $2 wsurel $version $arch
		done
	done
}

function mock_build_module {
	dir=$1
	name=$2
	repo=$3
	version=$4
	arch=$5

	pushd ~
	echo '%_topdir %(pwd)' > ~/.rpmmacros
	mkdir -p package/{BUILD,RPMS,SOURCES,SRPMS,SPECS}
	pushd package

	cp ${dir}/specs/module-${name}.spec SPECS/.
	rpmbuild --nodeps -bs SPECS/module-${name}.spec -D 'dist %{nil}'

	/usr/bin/mock -r $repo-$version-$arch --rebuild SRPMS/*.src.rpm
	rm -rf /var/lib/mock/$repo-$version-$arch/result/*-debuginfo*.rpm
	mv /var/lib/mock/$repo-$version-$arch/result/*.src.rpm /yumrepo/wsurel/el$version/SRPMS
	cp /var/lib/mock/$repo-$version-$arch/result/*.rpm /yumrepo/wsurel/el$version/$arch
	createrepo /yumrepo/wsurel/el$version/$arch

	popd
	rm -rf package
	popd
}

function pack_srpm {
	DIR=$1
	NAME=$2
	cp ${DIR}/specs/${NAME}.spec SPECS/.
	cp -rf ${DIR}/sources/${NAME}/* SOURCES/.

	basefile=`basename $specfile`
	rpmbuild --nodeps -bs SPECS/$basefile -D 'dist %{nil}'
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

function clean_repos {
	for version in 5 6 ; do
		for arch in i386 x86_64 ; do
			echo "Cleaning wsurel-$version-$arch"
			rm -rf /yumrepo/wsurel/el$version/$arch/*
			createrepo /yumrepo/wsurel/el$version/$arch
		done
	done
}

function update_repos {
	for version in 5 6 ; do
		for arch in i386 x86_64 ; do
			echo "Cleaning wsurel-$version-$arch"
			createrepo /yumrepo/wsurel/el$version/$arch
		done
	done
}