Title: MONARC 2.13.4 released
Date: 2026-02-13
Modified: 2025-02-13
Category: monarc
Tags: monarc, new-release
Summary: Release 2.13.4 of MONARC

Version 2.13.4 include some new features and fixes

### New

- [Change from 27002:2013 to :2022 (default deployment)](https://github.com/monarc-project/MonarcAppFO/issues/539)
- [Increased the password min length requirement from 9 to 12 characters](https://github.com/monarc-project/MonarcAppFO/issues/590).
- [[FrontOffice] Add Docker environment for the dev env](https://github.com/monarc-project/MonarcAppFO/issues/597).
- [Add the swagger files renderer and describe all the API endpoints](https://github.com/monarc-project/MonarcAppFO/issues/570).

### Fix

- [Implementation plan: Same measure reported multiple times](https://github.com/monarc-project/MonarcAppFO/issues/573)
- [SQL syntax error (MySQL ONLY_FULL_GROUP_BY violation)](https://github.com/monarc-project/MonarcAppFO/issues/574)
- [Dashboard Operational Risks PNG Export incorrect](https://github.com/monarc-project/MonarcAppFO/issues/578)
- Updated the proxy-manager to use the LTS version and avoid the php version limitation.
- Fixed the recommendations export to .csv, removed the default limit of 25 records.


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
[GitHub Release v2.13.4](https://github.com/monarc-project/MonarcAppFO/releases/tag/v2.13.4){:target="_blank"}

Or use the [release bundle](https://github.com/monarc-project/MonarcAppFO/releases/download/v2.13.4/MonarcAppFO-v2.13.4.tar.gz).


## Local Installation (Docker + Application).

Monarc FrontOffice can also be installed locally using Docker and a small utililty to execute docker commands, configure and update the Monarc FO tool.

To install the application:

- Install Docker on your system.

- Download the appropriate application package for your operating system from [here](https://vm.monarc.lu/apps/){:target="_blank"}.

- Follow the setup instructions included with the package.

For detailed installation steps and additional information, refer to the official documentation [here](https://monarc.lu/documentation/technical-guide/#end-user-app).


## Monarc BackOffice application.

The is also a new BackOffice release available. The details can be found [here](https://github.com/monarc-project/MonarcAppBO/releases/tag/v2.13.5){:target="_blank"}.
