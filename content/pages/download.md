Title: Download

[TOC]

## Installation of MONARC

Different options are available to install MONARC.

### Source code

The source code of MONARC is available on
[GitHub](https://github.com/monarc-project).
For installation instructions from the source code see
[here](https://github.com/monarc-project/MonarcAppFO/tree/master/INSTALL).

### Virtual machine

If you would like to test MONARC and don't want to do an installation,
a virtual machine for VirtualBox is
[available on the release page](https://github.com/monarc-project/MonarcAppFO/releases/latest)
(.ova file).   

Import the image by either just double-click on the .ova
file (if VirtualBox is associated with .ova files) or launch VirtualBox and
click on *File* -> *Import appliance*.

You can also generate generate your virtual machine with the latest version of
MONARC. More information
[here](https://github.com/monarc-project/monarc-packer).

### Vagrant

Deploy MONARC with [Vagrant](https://github.com/monarc-project/MonarcAppFO/tree/master/vagrant).
Vagrant is convenient to use in order to setup your development environment.

### Ansible

Deploy the whole architecture with [Ansible](https://github.com/monarc-project/ansible-ubuntu).
Use this method only if you want to use a back office.


## Usage of MONARC

With your Web browser:

* go to the address [http://10.0.0.101](http://10.0.0.101) (depending on your
  configuration and the installation method)
* Login: admin@admin.test
* Password: admin


### Import a risk analysis demo

1. [Create a risk analysis](/documentation/user-guide/#creating-a-risk-analysis)
2. Download the risk analysis file <a href="/assets/files/monarc-training/fr/MyPrint.json" download>(MyPrint FR)</a> or
   <a href="/assets/files/monarc-training/en/MyPrint-With-Values.json" download>(MyPrint EN)</a>
3. [Import JSON file](/documentation/user-guide/#contextual-menu-of-asset)



## Having troubles?

Have a look at the section of [common issues](/documentation/common-issues).
If you do not find your answer, [ask the community](/community/contribution-guidelines).
