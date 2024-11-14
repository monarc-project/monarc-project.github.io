Title: MONARC 2.13.1 released
Date: 2024-10-15
Modified: 2024-10-15
Category: monarc
Tags: monarc, new-release
Summary: Release 2.13.1 of MONARC

Version 2.13.1 includes some new features and a fix.

### New

- Refactored the codebase of core and client repositories to improve different aspects of the application, [described here](https://github.com/monarc-project/MonarcAppBO/releases/tag/v2.13.1) 
- Added possibility to export risk analysis with Knowledge Base (KB) and/or Assets Library (AL). That allows to optionally export all the KB a AL data without having the analysis modelling started. This is needed for sharing models between FrontOffices or update AL or KB with new versions of the structures.
- Changed the export format of JSON export file to reduce its size and be similar to the api endpoints responses and the projects structures views. An old data converter is implemented for the backward compatibility.
- Significantly improved the import time and made it always consistent. In case of import issues the data are not inserted, there are saved in the DB only at the end of the process (transactional approach).
- Removed extra user’s information from password reset response and removed the endpoint access by the other users.
- Restricted analysis creation based on the models that are not available for the client.

### Fix

- [Fixed the password change](https://github.com/monarc-project/MonarcAppFO/discussions/523).


## Updating

If the update is performed from Monarc v2.12.5 or earlier, the update of php to v8.x is necessary.
It would be recommended to perform php version upgrade to php 8.1.  
In case if on the Monarc server used Ubuntu distributive, then it would be a good move to upgrade it to 22.04 or later,    
because it comes with available php8.1 by default.


The specific php packages that can be used (example with php8.0 / Ubuntu):    
`sudo apt-get install -y php8.1 php8.1-cli php8.1-common php8.1-mysql php8.1-zip php8.1-gd php8.1-mbstring php8.1-curl php8.1-xml php8.1-bcmath php8.1-intl php8.1-imagic`


`php8` module also has to be enabled for Apache and previous used version disabled (in case if was enabled):

- `a2dismod php7.4` (could be different one enabled, to check: `sudo a2query -m`)

- `a2enmod php8.1`


The standard steps to perform the Monarc update:
[guide](https://monarc.lu/documentation/technical-guide/#monarc-update).

More details and notes are available on
[GitHub Release v2.13.1](https://github.com/monarc-project/MonarcAppFO/releases/tag/v2.13.1){:target="_blank"}

## Download

Download the OVA image of this release
[here](https://vm.monarc.lu/MONARC_v2.13.1@ed598a0/){:target="_blank"}.

Or use the [release bundle](https://github.com/monarc-project/MonarcAppFO/releases/download/v2.13.1/MonarcAppFO-v2.13.1.tar.gz).

