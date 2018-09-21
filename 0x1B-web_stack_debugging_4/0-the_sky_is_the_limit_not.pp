# fix too many open files error

exec {'raise ulimit':
  command => 'sed -i "s|15|4096|g" /etc/default/nginx',
  path    => '/bin/:/sbin/:/usr/bin/:/usr/sbin/'
}

exec {'restart nginx':
  require => Exec['raise ulimit'],
  command => 'sudo service nginx restart',
  path    => '/bin/:/sbin/:/usr/bin/:/usr/sbin/'
  }
