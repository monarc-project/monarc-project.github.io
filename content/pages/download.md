Title: Download

[TOC]

## Install MONARC

The source code of MONARC is available on
[GitHub](https://github.com/monarc-project).

### Virtual machine

A virtual machine for VirtualBox is
[available on the release page](https://github.com/monarc-project/MonarcAppFO/releases/latest)
(.ova file).   
This is the easiest method if you want to quickly use MONARC on your computer.

You can also generate generate your virtual machine with the latest version of
MONARC. More information
[here](https://github.com/monarc-project/monarc-packer).


#### Importing the image

You will need a tool for virtualization which accepts .ova files.
In this guide, [VirtualBox](https://www.virtualbox.) will be used.

Import the image in your application by either just double-click on the .ova
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

### Ansible

Deploy the whole architecture with [Ansible](https://github.com/monarc-project/ansible-ubuntu).




## Use MONARC

Just open your browser and go to this address: http://10.0.0.101/

Login / Password : admin@admin.test / admin


### Risk Analysis Demo (Only in French)

1. [Create a risk analysis in French](/documentation/user-guide/#creating-a-risk-analysis)
2. Download the risk analysis file <a href="/assets/files/monarc-training/fr/myprint.json" download>(myprint.json)</a>
3. [Import JSON file](/documentation/user-guide/#contextual-menu-of-asset)
