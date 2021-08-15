# Add configuration lines in the client SSH config file.
file_line {'Add identity file':
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => '\tIdentityFile ~/.ssh/holberton'
}

file_line {'Set password auth off':
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => '\tPasswordAuthentication no',
}
