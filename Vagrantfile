Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.provision "file", source: "./", destination: "~/"
  config.vm.provision "shell", path: "vagrant_provision.sh"
  config.vm.network "public_network"
  config.vm.network "forwarded_port", guest: 5000, host: 8080
  
end
