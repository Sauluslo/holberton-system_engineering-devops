# Using Puppet, create a file in /tmp.

file { 'holberton':
  mode    => '0744',
  path    => '/tmp/holberton',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
