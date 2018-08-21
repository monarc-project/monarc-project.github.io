Title: Security Considerations
Date: 2018-08-21
Hidden: false

> This document is currently under development.

[TOC]

## Architecture

Deploying MONARC with a back office requires the use of at least 4 different
servers:

* a server acting as a reverse proxy (**RPX**);
* a configuration server (**CFG**) where ansible is running;
* a back office server (**BO**);
* at least one MONARC server (**FO**).

The [MONARC architecture](/documentation/technical-guide/#global-architecture)
is presented here.

Only the **RPX** should have a public IP address and be available via HTTPS
(port 443).
It is advised to install a tool like
[Fail2ban](https://github.com/fail2ban/fail2ban) on this server.


The administration of the servers should be done via SSH and only possible
inside a VPN in order to prevent any attack (port scanning, etc.) from the
outside.


## Multitenancy

MONARC is a multitenant application. Every tenant (MONARC instances on a **FO**
server) are separated:

* databases (MONARC models, users management, etc.);
* data (assets like deliveries templates, configuration files, cache, etc.);
* Apache instances with Virtual Hosts.

An administrator of a back office is not able to access to a MONARC instance.
The administrator can only create or delete clients (instances). Read
[this section](/documentation/administrator-guide/#management-of-the-clients)
for more information.

Generally MONARC instances are virtually isolated on one **FO** server. It is
also possible to isolate instances on different servers in the same subnetwork.
Or on physically distant servers if you are using a VPN.

The reverse proxy is responsible of dispatching the MONARC users to the correct
instances.


## Configuration server

The configuration server (**CFG**) must be able to contact the other servers
via SSH with public encryption key. The corresponding private key must be
stored only on this server, for example for a system user
*ansible*. This user will launch periodically the
[MONARC playbook](https://github.com/monarc-project/ansible-ubuntu) with cron.


## System update

Always keep your systems up-to-date. At least the security updates from the
GNU/Linux distribution.
