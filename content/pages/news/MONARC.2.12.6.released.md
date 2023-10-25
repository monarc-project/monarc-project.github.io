Title: MONARC 2.12.7 released
Date: 2023-10-25
Modified: 2023-10-25
Category: monarc
Tags: monarc, new-release
Summary: Release 2.12.7 of MONARC

Version 2.12.7 includes some new features and a fix.

### New

- [[FrontOffice] Alternative to 2FA QR code](https://github.com/monarc-project/MonarcAppFO/issues/505)
- [[FrontOffice] Add context info to the list of analysis panel](https://github.com/monarc-project/MonarcAppFO/issues/506)

### Fix

- [[FrontOffice] Global dashboard max calculation error](https://github.com/monarc-project/MonarcAppFO/issues/507)


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



_Notes on new features configuration (if the current Monarc version is <= v2.12.5)._

- [FrontOffice] Analysis background import.

    To enable and use the Background import feature there are 2 necessary actions needs to be preformed.

    1. Add/enable the configuration option in the Monarc config [local.php](https://github.com/monarc-project/MonarcAppFO/blob/master/config/autoload/local.php.dist#L120-L123), `isBackgroundProcessActive` has to be `true`.

    2. Add a crontab job to execute the import in background mode. For multiple FrontOffice clients installation the crontab could be (to run every 30 seconds):  
        `* * * * * www-data              cd /var/lib/monarc/fo && /var/lib/monarc/fo/scripts/run-background-import-for-all-clients.sh > /dev/null 2>&1`

        `* * * * * www-data ( sleep 30 ; cd /var/lib/monarc/fo && /var/lib/monarc/fo/scripts/run-background-import-for-all-clients.sh > /dev/null 2>&1 )`

        For a single client the following command can be executed from crontab:
            `bin/console monarc:import-analyses`



The standard steps to perform the Monarc update: 
[guide](https://monarc.lu/documentation/technical-guide/#monarc-update).

More details and notes are available on
[GitHub](https://github.com/monarc-project/MonarcAppFO/releases/tag/v2.12.7).


## Download

Download the OVA image of this release
[here](https://vm.monarc.lu/MONARC_v2.12.7@fda59cb/).

Or use the [release bundle](https://github.com/monarc-project/MonarcAppFO/releases/download/v2.12.7/MonarcAppFO-v2.12.7.tar.gz).

