Title: MONARC 2.9.1 released
Date: 2019-11-25
Modified: 2019-11-25
Category: monarc
Tags: monarc, new-release
Summary: Release 2.9.1 of MONARC

Version 2.9.1 of MONARC has been released with several fixes and important
changes in the backend.

### Enhancement

- the backend of MONARC is now using Zend Framework 3
  ([#15](https://github.com/monarc-project/MonarcAppFO/issues/15));
- MONARC code has been restructured to comply with PSR-2 standard;
- updated the usage of the dependencies (Core and FrontOffice) from
  packagist.org;  
- default initialization of the set of recommendations
  ([#183](https://github.com/monarc-project/MonarcAppFO/issues/183)).

### Fix

- Error when importing OP risks with recommendation
  ([#191](https://github.com/monarc-project/MonarcAppFO/issues/191));
- fix editing of recommendations via the risk sheet
  ([#195](https://github.com/monarc-project/MonarcAppFO/issues/195));
- various fixes related to the management of recommendations and impact edition;
- fixes in the GDPR module.


## Updating

Due to the consequent changes in the backend and the switch to the version 3 of
Zend Framework, the update method is different from the usual process.
We wrote a script in order to help you to update your MONARC installation.
No database migrations will be executed.

The minimum requirement is now PHP 7.1. We strongly advise to
update to at least PHP 7.2. PHP 7.1 ends security support at the
[end of this year](https://www.php.net/supported-versions.php).

MONARC 2.9.1 has been mainly tested on:

- Debian 10 with PHP 7.3;
- Ubuntu 18.04 LTS with PHP 7.2.

Once you have checked that your system met the minimum requirements you can
update your MONARC instance with the following command:

```bash
$ cd /var/lib/monarc/fo
$ rm -Rf data/DoctrineORMModule data/cache
$ mkdir -p data/LazyServices/Proxy # set owners to www-data
$ curl -sSL https://www.monarc.lu/assets/scripts/upgrade-to-2.9.1.sh | bash
```

> **NOTE:**  Never execute a remote script without checking it.

This is the only time you will have to use this script. Future MONARC updates
will works as usual.

```bash
$ sha512sum upgrade-to-2.9.1.sh
76a908ff39ae0d3ada2ccbf254979e733ef993ac650a41c27c03dc2f6f2c164ac22ba1862a155fb9bd05d7f7bdcc064287d7e2eb2a2cf3c2f2cd4e35389be6ae  upgrade-to-2.9.1.sh
```

This script can be used in order to update MONARC and the
[back office of MONARC](https://github.com/monarc-project/MonarcAppBO).

<!-- To update, check out our
[update](http://monarc.lu/documentation/technical-guide/#monarc-update) instructions. -->

As usual you can download the virtual machine
[here](https://github.com/monarc-project/MonarcAppFO/releases/tag/v2.9.1).
