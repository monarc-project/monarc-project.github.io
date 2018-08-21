Title: Security Considerations
Date: 2018-08-21
Hidden: false

[TOC]

## Infrastructure

Deploying MONARC with a back office requires the use of at least 4 different
servers:

* a server acting as a reverse proxy (**RPX**);
* a configuration server (**CFG**) where ansible is running;
* a back office server (**BO**);
* at least one MONARC server (**FO**).

Only the **RPX** should have a public IP address and be available via HTTPS
(port 443).

Administration of the servers should be done via SSH and only possible inside
a VPN in order to prevent any attack (port scanning, etc.) from the outside.

## Client instances separation
