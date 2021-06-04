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
      Mysql root login: root:1e1e89e230337021f2ee45380e73c99ce1fdf84f7e3f4c0a612df15d16ec7b7e
      Mysql MONARC login: sqlmonarcuser:99c6ecc8d3933f0957cf8749fafe9f7f266cfb9eadc7e0a09c5f550c419aafcf
    
    Image integrity check:
      sha512sum: 9c26930b03076b3b77e7f0ee16cc68dd4f3e069f1277d25159ba00d6ba8b7ecd7574ba73299db907bedf72c29b4880aa45e17d6fa7d78543e133fe698f2d7bfc
      sha1sum: bc1f8b318b1676f22e22fc148c25c10fda8a97f8
     
    MONARC is available on port 80.

    MONARC Stats Service is available on port 5005.
