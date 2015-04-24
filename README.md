# Playa Mesos

Tiltai-example helps you quickly tryout [Tiltai][24] functionality on a single host. 

It is based on [Playa Mesos][8], which helps you quickly create [Apache Mesos][1] test environments.
This project relies on [VirtualBox][5], [Vagrant][6], and an Ubuntu box image
which has Mesos and [Marathon][2] pre-installed. 

## Requirements

* [VirtualBox][5] 4.2+
* [Vagrant][6] 1.3+
* [git](http://git-scm.com/downloads) (command line tool)
* [Packer][9] 0.5+ (optional)
* VMware [Fusion](https://www.vmware.com/products/fusion/) or [Workstation](https://www.vmware.com/products/workstation/) (optional)
* [Vagrant Plugin for VMware Fusion or Workstation](https://www.vagrantup.com/vmware) (optional)

## Quick Start

1. [Install VirtualBox](https://www.virtualbox.org/wiki/Downloads)

1. [Install Vagrant](http://www.vagrantup.com/downloads.html)

1. Clone this repository

  ```bash
  git clone https://github.com/Zogg/Tiltai-example.git
  cd Tiltai-example
  ```

1. Make sure tests pass

  ```bash
  bin/test
  ```

1. Start the VM

  ```bash
  vagrant up
  ```

1. Connect to the Mesos Web UI on [10.141.141.10:5050](http://10.141.141.10:5050) and the Marathon Web UI on [10.141.141.10:8080](http://10.141.141.10:8080) and the Consul Web UI on [10.141.141.10:8500](http://10.141.141.10:8500)

1. SSH to the VM

  ```bash
  vagrant ssh
  ps -eaf | grep mesos
  exit
  ```

1. Launch the infrastructure

  ```bash
  cd /vagrant/bin
  ./make_infra
  ```
  
  Inspect Marathon Web UI, it should now deploy the services. Using Mesos Web UI you may inspect service logs. And using Consul Web UI you may observe the registered services and their ip/ports.

1. Playing with the services

  ```bash
  # The services are found at /vagrant/services
  # Modify the source code of the service
  cd /vagrant/services/feeder
  vim ./src/run.py
  # Rebuild docker image
  ./build.sh
  # Restart marathon infrastructure
  cd /vagrant/bin && ./restart_infra
  ```

## Documentation

* [Configuration][15]
* [Common Tasks][16]
* [Troubleshooting][17]
* [Known Issues][18]
* [To Do][19]


[1]: http://incubator.apache.org/mesos/ "Apache Mesos"
[2]: http://github.com/mesosphere/marathon "Marathon"
[3]: http://jenkins-ci.org/ "Jenkins"
[4]: http://zookeeper.apache.org/ "Apache Zookeeper"
[5]: http://www.virtualbox.org/ "VirtualBox"
[6]: http://www.vagrantup.com/ "Vagrant"
[7]: http://www.ansibleworks.com "Ansible"
[8]: https://github.com/mesosphere/playa-mesos "Playa Mesos"
[9]: http://www.packer.io "Packer"
[13]: http://mesosphere.io/downloads "Mesosphere Downloads"
[14]: http://www.ubuntu.com "Ubuntu"
[15]: doc/config.md "Configuration"
[16]: doc/common_tasks.md "Common Tasks"
[17]: doc/troubleshooting.md "Troubleshooting"
[18]: doc/known_issues.md "Known Issues"
[19]: doc/to_do.md "To Do"
[20]: http://www.packer.io/docs "Packer Documentation"
[21]: config.json "config.json"
[22]: packer/packer.json "packer.json"
[23]: lib/scripts "scripts"
[24]: http://github.com/Zogg/Tiltai "Tiltai"
