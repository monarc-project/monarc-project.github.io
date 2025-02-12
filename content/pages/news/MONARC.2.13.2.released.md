Title: MONARC 2.13.2 released
Date: 2025-02-12
Modified: 2025-02-12
Category: monarc
Tags: monarc, new-release
Summary: Release 2.13.2 of MONARC

Version 2.13.2 includes some new features and a fix.

### New

- An optional Captcha integration, that can appear after certain number, configured, of unsuccessful login attempts.
  To enable Captcha a specific configuration has to be added (@see config/autoload/local.php.dist, 'captcha' option).
- Configurable export of analyses with evaluations. By default, the option can be yes, so export with evaluations is not forgotten to be enabled.
  To enable it a specific configuration has to be added (@see config/autoload/local.php.dist, 'export' option).
- Added the risks IDs to all the tables to facilitate the traceability. Based on [the discussion](https://github.com/monarc-project/MonarcAppFO/discussions/419).

### Fix

- [#552](https://github.com/monarc-project/MonarcAppFO/issues/552), Fix of Assets Library objects import.


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
[GitHub Release v2.13.2](https://github.com/monarc-project/MonarcAppFO/releases/tag/v2.13.2){:target="_blank"}

## Download

Download the OVA image of this release
[here](https://vm.monarc.lu/MONARC_v2.13.2@1f3a616/){:target="_blank"}.

Or use the [release bundle](https://github.com/monarc-project/MonarcAppFO/releases/download/v2.13.2/MonarcAppFO-v2.13.2.tar.gz).

