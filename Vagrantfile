# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing
VAGRANTFILE_API_VERSION = '2'

PM_ROOT = File.dirname(__FILE__)
PM_CONFIG = File.expand_path(File.join(File.dirname(__FILE__), 'config.json'))
require_relative File.join(PM_ROOT, 'lib', 'ruby', 'playa_settings')
pmconf = PlayaSettings.new(PM_CONFIG)

box_url = "#{pmconf.base_url}/#{pmconf.box_name}-#{pmconf.platform}.box"

# #############################################################################
# Vagrant VM Definitions
# #############################################################################

ENV['VAGRANT_DEFAULT_PROVIDER'] = pmconf.platform

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  config.vm.network :private_network, ip: pmconf.ip_address

  # If true, then any SSH connections made will enable agent forwarding.
  # Default value: false
  config.ssh.forward_agent = true
  
  config.vm.network "forwarded_port", guest: 8080, host: 8080
  config.vm.network "forwarded_port", guest: 5050, host: 5050
  config.vm.network "forwarded_port", guest: 8500, host: 8500
  
  # Every Vagrant virtual environment requires a box to build off of.
  config.vm.box = pmconf.box_name

  # There are two levels of caching here.
  # 1. If pmconf.box_local is set, then the file referenced by pmconf.box_url
  #    was found in the Packer build path (packer/builds/*.box) and Vagrant's
  #    vm.box_url is set to that path. To force retrieving the box
  #    from the URL again, simply remove the Packer builds directory.
  # 2. Vagrant only retrieves box images from vm.box_url if it does not have
  #    a local copy in ~/.vagrant.d/boxes/$BOX_NAME. These can be removed
  #    with the command: "vagrant box remove $BOX_NAME"
  config.vm.box_url = pmconf.box_local ? pmconf.box_local : box_url

  # Note: You'll want a decent amount of memory for your mesos master/slave
  # VM. The strict minimum, at least while the VM is provisioned, is the
  # amount necessary to compile mesos and the jenkins plugin. 2048m+ is
  # recommended.  The CPU count can be lowered, but you may run into issues
  # running the Jenkins Mesos Framework if you do so.
  config.vm.provider :virtualbox do |vb|
    vb.name = pmconf.box_name
    vb.customize ['modifyvm', :id, '--memory', pmconf.vm_ram]
    vb.customize ['modifyvm', :id, '--cpus',   pmconf.vm_cpus]
  end
  config.vm.provider :vmware_fusion do |v|
    v.vmx['memsize'] = pmconf.vm_ram
    v.vmx['numvcpus'] = pmconf.vm_cpus
  end
  config.vm.provider :vmware_workstation do |v|
    v.vmx['memsize'] = pmconf.vm_ram
    v.vmx['numvcpus'] = pmconf.vm_cpus
  end

  # Make the project root available to the guest VM.
  # config.vm.synced_folder '.', '/vagrant'

  # Only provision if explicitly request with 'provision' or 'up --provision'
  if ARGV.any? { |arg| arg =~ /^(--)?provision$/ }
    config.vm.provision :shell do |shell|
      shell.path = 'lib/scripts/common/mesosflexinstall'
      arg_array = ['--slave-hostname', pmconf.ip_address]
      # Using an array for shell args requires Vagrant 1.4.0+
      # TODO: Set as array directly when Vagrant 1.3 support is dropped
      shell.args = arg_array.join(' ')
    end
  end

  config.vm.provision "shell", path: "lib/scripts/common/dockerize"

  config.vm.provision "shell" do |s|
    s.inline = "cd /vagrant/services/nanomsg && /bin/bash /vagrant/services/nanomsg/build.sh" 
  end
  config.vm.provision "shell" do |s|
    s.inline = "cd /vagrant/services/feeder && /bin/bash /vagrant/services/feeder/build.sh" 
  end
  config.vm.provision "shell" do |s|
    s.inline = "cd /vagrant/services/encryptor && /bin/bash /vagrant/services/encryptor/build.sh" 
  end
  config.vm.provision "shell" do |s|
    s.inline = "cd /vagrant/services/emailsink && /bin/bash /vagrant/services/emailsink/build.sh" 
  end

  config.vm.provision "docker" do |d|
    d.pull_images "progrium/consul"
    d.pull_images "gliderlabs/registrator"
  end

  config.vm.provision "shell" do |s|
    s.inline = "sudo apt-get install mesos marathon && sudo stop mesos-slave && sudo stop marathon || echo ''" 
  end
  
  config.vm.provision "shell" do |s|
    s.inline = "sudo rm -rf /tmp/mesos/meta/slaves && sudo start mesos-slave && sudo start marathon" 
  end
end
