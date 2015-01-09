$apache_pkgs = [
  'httpd', 'httpd-devel', 'mod_ssl',
  'ruby-devel', 'rubygems', 'gcc-c++', 'libcurl-devel',
  'zlib-devel', 'make', 'automake',  'openssl-devel'
]

package { $apache_pkgs:
  ensure => 'installed'
}

package { 'git':
  ensure => 'installed'
}

package { 'passenger':
  provider => 'gem',
  ensure => 'installed'
}

exec { 'install apache passenger modules':
  command => 'passenger-install-apache2-module -a',
  path => '/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin',
  unless => 'test -f /usr/local/share/gems/gems/passenger-4.0.57/buildout/apache2/mod_passenger.so'
}

file { '/etc/httpd/conf.d/puppetmaster.conf':
  owner => 'root',
  group => 'root',
  mode => 0644,
  content => template('/vagrant/puppetmaster.conf.erb'),
  notify => Service['httpd']
}

file { '/usr/share/puppet/rack':
  ensure => directory,
  owner => 'puppet',
  group => 'puppet'
}

file { '/usr/share/puppet/rack/puppetmasterd':
  ensure => directory,
  owner => 'puppet',
  group => 'puppet'
}

file { '/usr/share/puppet/rack/puppetmasterd/public':
  ensure => directory,
  owner => 'puppet',
  group => 'puppet'
}

file { '/usr/share/puppet/rack/puppetmasterd/tmp':
  ensure => directory,
  owner => 'puppet',
  group => 'puppet'
}

file { '/usr/share/puppet/rack/puppetmasterd/config.ru':
  owner => 'puppet',
  group => 'puppet',
  mode => 0644,
  source => '/vagrant/config.ru',
  notify => Service['httpd']
}

service { 'puppetmaster':
  ensure => stopped,
  enable => false
}

service { 'httpd':
  ensure => running,
  enable => true,
}
