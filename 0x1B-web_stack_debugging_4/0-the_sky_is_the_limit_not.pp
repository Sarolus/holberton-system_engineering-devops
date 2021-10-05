# Increase Ulimit

file {'/etc/default/nginx':
  path    => '/etc/default/nginx',
  content => 'ULIMIT="-n 4096"',
}

exec {'nginx':
  command => 'sudo service nginx restart',
  path    => ['/bin', '/usr/bin'],
}
