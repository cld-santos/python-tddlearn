package { 'python':
	ensure => present,
	name => "python3.5",
}

package { 'python3-pip':
  ensure => '8.1.1-2ubuntu0.2',
   require => Package["python"],
}

package { 'unittest':
        provider => pip3,
        ensure   => present,
        name     => "unittest2",
        require => Package["python3-pip"],
}

package {'django':
        provider => pip3,
        ensure => present,
        name => "django",
        require => Package["python3-pip"],
}

package {'gunicorn':
        provider => pip3,
        ensure => '19.3.0',
        name => "gunicorn",
        require => Package["python3-pip"],
}

package {'pillow':
        provider => pip3,
        ensure => '2.9.0',
        name => "Pillow",
        require => Package["python3-pip"],
}

