Title: Download

[TOC]

## Installation of MONARC

### Source code

The source code of MONARC is available on
[GitHub](https://github.com/monarc-project).

For installation instructions from the source code see
[here](https://github.com/monarc-project/MonarcAppFO/tree/master/INSTALL).


### Virtual machine

If you would like to test MONARC and don’t want to do an installation,
a virtual machine for VirtualBox is
[available on the release page](https://github.com/monarc-project/MonarcAppFO/releases/latest)
(.ova file).   

You can also generate generate your virtual machine with the latest version of
MONARC. More information
[here](https://github.com/monarc-project/monarc-packer).

#### Importing the image

You will need a tool for virtualization which accepts .ova files.
In this guide, [VirtualBox](https://www.virtualbox.org) will be used.

Import the image by either just double-click on the .ova
file (if VirtualBox is associated with .ova files) or launch VirtualBox and
click on File -> Import appliance.

#### Configuration of VirtualBox

Now, set-up a new "host only network" (file -> preferences -> network)

![monarc_cli](/assets/images/trainings/create_host.png "Create host")

After this, fill out using the following parameters :

![monarc_cli](/assets/images/trainings/param1.JPG "Adapter")
![monarc_cli](/assets/images/trainings/param2.JPG "DHCP")

You also have to modify the network interface of the virtual machine.

Just be sure that "host only adapter" is selected and the name is the one just
created.

_**NOTE:**_ The box "cable connected" has to be ticked.

![monarc_cli](/assets/images/trainings/network.JPG "Image - network")

#### Run the server

Now that the image is installed and configured, you can run the server by
selecting "demo_monarc" and clicking start.

![monarc_cli](/assets/images/trainings/launch.png "launch")

The server is running when the window of the virtual appliance looks like this :

![monarc_cli](/assets/images/trainings/vm_launched.JPG "vm launched")


### Vagrant

Deploy MONARC with [Vagrant](https://github.com/monarc-project/MonarcAppFO/tree/master/vagrant).

Vagrant is convenient to use in order to setup your development environment.

### Ansible

Deploy the whole architecture with [Ansible](https://github.com/monarc-project/ansible-ubuntu).




## Usage of MONARC

Open your Web browser and go to this address (depending on your
configuration):  
[http://10.0.0.101](http://10.0.0.101)

* Login: admin@admin.test
* Password: admin


### Import a risk analysis demo

1. [Create a risk analysis in French](/documentation/user-guide/#creating-a-risk-analysis)
2. Download the risk analysis file <a href="/assets/files/monarc-training/fr/myprint.json" download>(myprint.json)</a>
3. [Import JSON file](/documentation/user-guide/#contextual-menu-of-asset)
