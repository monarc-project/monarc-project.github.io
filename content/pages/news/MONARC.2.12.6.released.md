Title: MONARC 2.12.6 released
Date: 2023-04-25
Modified: 2023-04-25
Category: monarc
Tags: monarc, new-release
Summary: Release 2.12.6 of MONARC

Version 2.12.6 includes some new features and fixes.

### New

- [FrontOffice] Analysis background import.
- Support of PHP8.
- [FrontOffice] Specific error message on a wrong password input of analysis import.
- [BackOffice] Update clients' data and linked models via Ansible and new flags "2FAEnforced" and "isBackgroundImportActive".

### Fix

- [FrontOffice] Recommendations modification from the Knowledge Base when due date is set.
- [FrontOffice] Recommendations modification fix of loading the linked recommendation set.


## Updating

One of the new features of the Release v2.12.6 is upgrade of php to v8.x.
It would be recommended to perform php version upgrade to php 8.0 or 8.1.  
In case if on the Monarc server used Ubuntu distributive, then it would be a good move to upgrade it to 22.04 or later,    
because it comes with available php8.1 by default.


The specific php packages that can be used (example with php8.0 / Ubuntu):    
`sudo apt-get install -y php8.0 php8.0-cli php8.0-common php8.0-mysql php8.0-zip php8.0-gd php8.0-mbstring php8.0-curl php8.0-xml php8.0-bcmath php8.0-intl php8.0-imagic`


`php8` module also has to be enabled for Apache and previous used version disabled (in case if was enabled):

- `a2dismod php7.4` (could be different one enabled, to check: `sudo a2query -m`)

- `a2enmod php8.0`



_Notes on new features configuration._

- [FrontOffice] Analysis background import.

    To enable and use the Background import feature there are 2 necessary actions needs to be preformed.

    1. Add/enable the configuration option in the Monarc config [local.php](https://github.com/monarc-project/MonarcAppFO/blob/master/config/autoload/local.php.dist#L120-L123), `isBackgroundProcessActive` has to be `true`.

    2. Add a crontab job to execute the import in background mode. For multiple FrontOffice clients installation the crontab could be (to run every 30 seconds):  
        `* * * * * www-data              cd /var/lib/monarc/fo && /var/lib/monarc/fo/scripts/run-background-import-for-all-clients.sh > /dev/null 2>&1`

        `* * * * * www-data ( sleep 30 ; cd /var/lib/monarc/fo && /var/lib/monarc/fo/scripts/run-background-import-for-all-clients.sh > /dev/null 2>&1 )`

        For a single client the following command can be executed from crontab:
            `bin/console monarc:import-analyses`


- [BackOffice] Update clients' data and linked models via Ansible and new flags "2FAEnforced" and "isBackgroundImportActive".

    To be able to use the Back Office feature of clients update, a new release of the BO application should be used along with ansible changes:     

    - [BackOffice release](https://github.com/monarc-project/MonarcAppBO/releases/tag/v2.12.6).
    - A new Ansible [cronjob]((https://github.com/monarc-project/ansible-ubuntu/blob/master/playbook/cronjob_update.sh)) has to be added to the system crontab.
    - [A new script](https://github.com/monarc-project/ansible-ubuntu/blob/master/playbook/monarcbo/files/update_monarc_clients.sh) has to be added to the BackOffice server `/usr/local/bin/update_monarc_clients.sh`. 

The standard steps to perform the Monarc update: 
[guide](https://monarc.lu/documentation/technical-guide/#monarc-update).

More details and notes are available on
[GitHub](https://github.com/monarc-project/MonarcAppFO/releases/tag/v2.12.6).


## Download

Download the OVA image of this release
[here](https://vm.monarc.lu/MONARC_v2.12.6@ddca7f3/).

Or use the [release bundle](https://github.com/monarc-project/MonarcAppFO/releases/download/v2.12.6/MonarcAppFO-v2.12.6.tar.gz).

