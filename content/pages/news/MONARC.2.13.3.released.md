Title: MONARC 2.13.3 released
Date: 2025-04-17
Modified: 2025-07-04
Category: monarc
Tags: monarc, new-release
Summary: Release 2.13.3 of MONARC

Version 2.13.3, 2.13.3-p1, 2.13.3-p2 and 2.13.3-p3 include some new features and fixes

### New

- [#522](https://github.com/monarc-project/MonarcAppFO/issues/522) Possibility to rest 2FA of users by the admin account along with the password reset.
- The Global analyses stats is only available now to the users with CEO (global statistics) role.
- Possibility to import on the BackOffice side risks with mode (generic | specific) property.

### Fix

- Fixed analysis creation based on a specific model when the model has assets that consist of risks with generic threats or vulnerabilities.
- Added the validation of the instances hierarchy to prevent a possible parent / child circular reference.
- Fixed batch import validation error for measures, operational risks and operational risks tags.
- [#562](https://github.com/monarc-project/MonarcAppFO/issues/562) Fixed the final report generation error when the asset's context is set.
- Fixed the scale impact type status validation during the import process. If an instance consequence is not hidden, but a corresponding scale impact type is hidden the consequence value is not used for the risk calculation.
- Import Asset Library objects from MOSP when selected category is root.
- Snapshots creation when Record of Processing Activities are fully defined.


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
[GitHub Release v2.13.3](https://github.com/monarc-project/MonarcAppFO/releases/tag/v2.13.3){:target="_blank"}
on the patch1 release page
[GitHub Release v2.13.3-p1](https://github.com/monarc-project/MonarcAppFO/releases/tag/v2.13.3-p1){:target="_blank"}
on the patch2 release page
[GitHub Release v2.13.3-p2](https://github.com/monarc-project/MonarcAppFO/releases/tag/v2.13.3-p2){:target="_blank"}
and on the patch3 release page
[GitHub Release v2.13.3-p3](https://github.com/monarc-project/MonarcAppFO/releases/tag/v2.13.3-p3){:target="_blank"}

## Download

Download the OVA image of this release
[here](https://vm.monarc.lu/MONARC_v2.13.3-p3@6d10eba/){:target="_blank"}.
[here](https://vm.monarc.lu/MONARC_v2.13.3-p2@66ea2df/){:target="_blank"}.
[here](https://vm.monarc.lu/MONARC_v2.13.3-p1@a3d7cbc/){:target="_blank"}.
[here](https://vm.monarc.lu/MONARC_v2.13.3@54bb656/){:target="_blank"}.

Or use the [release bundle](https://github.com/monarc-project/MonarcAppFO/releases/download/v2.13.3/MonarcAppFO-v2.13.3.tar.gz).


## Monarc BackOffice application.

The is also a new BackOffice release available. The details can be found [here](https://github.com/monarc-project/MonarcAppBO/releases/tag/v2.13.3){:target="_blank"}.
