#!/bin/bash
PPEXISTS="/opt/puppetlabs/bin"
if [ ! -d "$PPEXISTS" ]
then
  sudo apt-get install -y language-pack-pt
  sudo dpkg -i /vagrant/environments/all/apps/puppetlabs-release-pc1-xenial.deb
  sudo apt-get update
  sudo apt-get install -y puppet-agent=1.7.1-1xenial
  
else
  echo "puppet instalado djow!"
fi
export PATH=/opt/puppetlabs/bin:$PATH

