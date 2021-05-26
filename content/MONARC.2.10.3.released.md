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
      Mysql root login: root:a77f8b5d8071563459dd26f775ea5627925ff1333c0a0d9a0be1ba8fd78be928
      Mysql MONARC login: sqlmonarcuser:754c5f7ffa714cca51291ec1181e9cec883d1b1caa6d8b991e40c74d59c0410a
    
    Image integrity check:
      sha512sum: 306ba5a3a113d84633380bfab740fe73132e257e50d2a549427f59bf3ccba57ac4e76701f3c196334517b1610acca46ea81d2091e25ed2f6933b72027cf3c4ce
      sha1sum: 6109c1b8e697704c7a46a9467531713cd6aaec51
     
    MONARC is available on port 80.

    MONARC Stats Service is available on port 5005.
