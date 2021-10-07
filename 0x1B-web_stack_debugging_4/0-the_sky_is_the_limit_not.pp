# Increase Ulimit

exec { 'update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => installed,
  name    => 'nginx',
  require => Exec['update'],
}

file {'/etc/default/nginx':
  ensure  => present,
  path    => '/etc/default/nginx',
  content => 'ULIMIT="-n 4096"',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
