# Increase hard and soft file limit for user

exec {'increase-hard-file':
  command => 'sed -i "/holberton hard/s/5/1024/" /etc/security/limits.conf'
  path    => '/usr/local/bin/:/bin',
}

exec {'increase-soft-file':
  command => 'sed -i "/holberton soft/s/4/1024/" /etc/security/limits.conf'
  path    => '/usr/local/bin/:/bin',
}
