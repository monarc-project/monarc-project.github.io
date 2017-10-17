Title: Trainings

Learn how to master risk analysis with our
[trainings](https://www.eventbrite.com/o/cases-13225622809).

## Training materials

* [Workshop MONARC - english](/assets/files/monarc-training/en/Formation_V2-MONARC_En.pdf)
* [Workshop MONARC - french](/assets/files/monarc-training/fr/Formation_V2-MONARC_Fr.pdf)
* the latest [Virtual Machine](https://github.com/monarc-project/MonarcAppFO/releases/latest)
  for VirtualBox

Next MONARC training in Luxembourg is on


## Installing the demo Virtual Machine

### Download the image

Download the last released image,
[MONARC_demo.ova](https://github.com/monarc-project/MonarcAppFO/releases/latest)


### Importing the image

You will need a tool for virtualization which accepts .ova files.
In this guide, [VirtualBox](https://www.virtualbox.) will be used.

Import the image in your application by either just double-click on the .ova
file (if VirtualBox is associated with .ova files) or launch VirtualBox and
click on File -> Import appliance.


### Configuration of VirtualBox

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


### Run the server

Now that the image is installed and configured, you can run the server by
selecting "demo_monarc" and clicking start.

![monarc_cli](/assets/images/trainings/launch.png "launch")

The server is running when the window of the virtual appliance looks like this :

![monarc_cli](/assets/images/trainings/vm_launched.JPG "vm launched")


### Use MONARC

Just open your browser and go to this address: http://10.0.0.101/

Login / Password : admin@admin.test / admin
