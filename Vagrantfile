
#-*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  # config.vm.box_check_update = false

  config.vm.network "forwarded_port", guest: 8000, host:8080
  config.vm.network "forwarded_port", guest: 5432, host: 15432

  # config.vm.network "private_network", ip: "192.168.33.10"

  # config.vm.network "public_network"

  config.vm.synced_folder "src/", "/home/ubuntu/src/"
  config.vm.synced_folder "hands_on/", "/home/ubuntu/hands_on/"

  # config.vm.provider "virtualbox" do |vb|
  #   # Display the VirtualBox GUI when booting the machine
  #   vb.gui = true
  #
  #   # Customize the amount of memory on the VM:
  #   vb.memory = "1024"
  # end
  #

  config.vm.provision "shell", path: "environments/all/manifests/install-puppet.sh"

  config.vm.provision :puppet do |puppet|
    puppet.environment = 'all'
    puppet.environment_path = "environments"
  end
end
