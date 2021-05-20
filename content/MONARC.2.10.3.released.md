Title: MONARC 2.10.3 released
Date: 2021-05-12
Modified: 2021-05-12
Category: monarc
Tags: monarc, new-release
Summary: Release 2.10.3 of MONARC

Version 2.10.3 Includes bug-fixes, new features and an enhancement.

### New

- Implement the UI language management
  ([#318](https://github.com/monarc-project/MonarcAppFO/issues/318))
- Implementation of the library objects import and assets export from/to MOSP
  ([#320](https://github.com/monarc-project/MonarcAppFO/issues/320))
- Possibility to export items from the Knowledge Base
  ([#321](https://github.com/monarc-project/MonarcAppFO/issues/321))
- Send MONARC version to Stats Service
  ([#341](https://github.com/monarc-project/MonarcAppFO/issues/341))

### Fix

- [Front Office] export of measure related to "amvs" stoped working since v2.10.1
  ([#340](https://github.com/monarc-project/MonarcAppFO/issues/340))

### Enhancement

- Improve the import speed of analyses and instances (*partially done*).
  ([#248](https://github.com/monarc-project/MonarcAppFO/issues/248))


## Updating

To update, please follow the 
[guide](http://monarc.lu/documentation/technical-guide/#monarc-update).

If you are coming from MONARC 2.9.0 please read
[this](/news/2019/11/25/monarc-291-released/#updating).

If you would like to use the new statistics feature then [StatsService](https://github.com/monarc-project/stats-service) has to be setup as well.
The documentation, architecture and installation instructions of Stats Service can be found [here](https://www.monarc.lu/documentation/stats-service).

You can also download the new virtual machine
[here](https://github.com/monarc-project/MonarcAppFO/releases/tag/v2.10.3).


## MONARC is in your language

You can now help us to make MONARC available in your language via [our platform](https://translate.monarc.lu/projects/monarc/) powered by [Weblate](https://weblate.org).


## <a href="#vm-image">The VirtualBox demo image</a>

Download the OVA image of this release
[here](https://my.monarc.lu/static/vm/MONARC_v2_10_3.ova).
Technical details about the VM:


    :::BBCode
    Login and Password for MONARC App (format: username:password):
      MONARC application: admin@admin.localhost:admin
    
    Login and Password for VirtualBox demo image (format: username:password):
      SSH login (Ubuntu credentials): monarc:password
    
    Database:
      Mysql root login: root:7e4195ac73cd3be6b08f84bfcd8df22e6fc844c719d9a632f28bd6d29d95c700
      Mysql MONARC login: sqlmonarcuser:ac9a093eaea88120909374679aa625355077e1888274b36180cd66bf8019d842
    
    Image integrity check:
      sha512sum: 4de7e6631cd8a753313eb59581f20618626c93f46785e95744bd5727dab8de70558b8aff52941d25893a6977d051fedceebd7bea970e4936640f938341b84c93
      sha1sum: e3b0631dee78a9d0d7f2e50fff80064104047edf
     
    MONARC is available on port 80.

    MONARC Stats Service is available on port 5005.
