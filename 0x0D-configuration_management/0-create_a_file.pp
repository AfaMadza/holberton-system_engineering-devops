#Creates a file in a specific directory
file { '/tmp':
  ensure => directory,
}

file { '/tmp/holberton':
  ensure  => present,
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet'
}
