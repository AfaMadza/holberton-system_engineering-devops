# 0x19. Postmortem

## Description

A postmortem is a tool widely used in the tech. industry to evaluate the process that lead to a failure in mission essential systems. After any outage, the team(s) in charge of the system will write a summary that has 2 main goals:

* To provide the rest of the company’s employees easy access to information detailing the cause of the outage. Often outages can have a huge impact on a company, so managers and executives have to understand what happened and how it will impact their work.
* To ensure that the root cause(s) of the outage has been discovered and that measures are taken to make sure it will be fixed.
-----------------------------------------------------------------

# Vagrant Postmortem
## Date:
2018-09-11

## Authors:
Afa Madza


## Issue Summary
On August 17, 2018 from 1201-1300 PST, a Vagrant VM running Ubuntu 14.04 LTS on Virtualbox essentially became inoperable as a result of the private key on the local machine not matching the public key stored on the remote machine. This issue affected 100% of users. When a specific user tried to ssh to the machine, an error stating ``permission denied (publickey)``. The root cause was that the correct ssh keys were not present in the ``authorized_keys`` folder.

## Timeline
* 1200: User attempts to ssh into machine but is prompted to update vagrant box upon ``Vagrant up.``
* 1201: User updates vagrant box and attempts to ssh again. Despite ssh being confiured properly, user is prompted for password.
* 1202: User types in default password ``vagrant``, but is prompted again for password.
* 1203: User types in default password again, but is propmted once more for password.
* 1204: User just hits ``enter``, and is prompted for password again.
* 1205: User types ``root`` as password and receives the following error: ``permission denied (publickey)``
* 1206: User runs ``Vagrant halt`` and contacts DevOps team.
* 1218: DevOps team talks to User to ascertain situation. DevOps opens ``Vagrantfile`` and checks for errors an find none.
* 1220: DevOps runs VirtualBox GUI and starts Vagrant VM.
* 1221: Vagrant VM tries to connect for 3 minutes all the while displaying the following messaage ``default: Error: Connection timeout. Retrying...``.
* 1224: Vagrant VM prompts DevOps for password.
* 1225: DevOps types ``root`` as password, and is able to log on.
* 1230: DevOps uses ``su`` to switch from root to user's account.
* 1235: DevOps navigates to /.ssh directory and examines the authorized_keys folder. There were several keys in the file, so DevOps created a backup folder to place the keys that were in the file.
* 1240: DevOps navigates to ``id_rsa`` file and examines it, and also creates a backup of the ``id_rsa.pub`` file.
* 1245: DevOps uses the following command to generate a new public key: ``ssh-keygen -y -f ~/.ssh/id_rsa > ~/.ssh/id_rsa.pub``.
* 1250: DevOps adds the new public key to the ``authorized_keys`` file.
* 1255: DevOps runs ``Vagrant halt`` and closes VirtualBox  GUI.
* 1300: DevOps succesfully runs ``Vagrant up`` and ``Vagrant ssh`` on user's VM.


## Root Cause
This issue was caused by an unauthorized update of Vagrant. As a result, the ssh key pairs were no longer current. The situation was resolved by using the ssh keygen command to generate a public key from a private key that the user had. Finally, the public key was added to the authorized_keys file to allow the user to ssh into the system.

## Preventative Measures
* Prevent automatic update of Vagrant by adding ``config.vm.box_check_update = false`` to Vagrantfile.
* Examine Vagrantfile every 2 weeks to ensure desired configurations are present.
* Check Vagrant documentation and website every other week to proactively prevent issues if discovered.
