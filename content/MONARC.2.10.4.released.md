Title: MONARC 2.10.4 released
Date: 2021-06-24
Modified: 2021-06-24
Category: monarc
Tags: monarc, new-release
Summary: Release 2.10.4 of MONARC

Version 2.10.4 includes bug-fixes.

### Fix

- Foreign Key Error by when deactivating information security risks.
  ([#358](https://github.com/monarc-project/MonarcAppFO/issues/358))
- Dashboard cartography error for risk lists.
  ([#359](https://github.com/monarc-project/MonarcAppFO/issues/359))
- [FrontOffice] Snapshots creation error.
  ([#362](https://github.com/monarc-project/MonarcAppFO/issues/362))


## Updating

To update, please follow the 
[guide](http://monarc.lu/documentation/technical-guide/#monarc-update).

If you are coming from MONARC 2.9.0 please read
[this](/news/2019/11/25/monarc-291-released/#updating).

If you would like to use the new statistics feature then [StatsService](https://github.com/monarc-project/stats-service) has to be setup as well.
The documentation, architecture and installation instructions of Stats Service can be found [here](https://www.monarc.lu/documentation/stats-service).

More details and notes are available on [GitHub](https://github.com/monarc-project/MonarcAppFO/releases/tag/v2.10.4).


## MONARC is in your language

You can now help us to make MONARC available in your language via [our platform](https://translate.monarc.lu/projects/monarc/) powered by [Weblate](https://weblate.org).


## <a href="#vm-image">The VirtualBox demo image</a>

Download the OVA image of this release
[here](https://vm.monarc.lu/MONARC_v2.10.4@f76b07a/).

Technical details about the VM:


    :::BBCode
    Login and Password for MONARC App (format: username:password):
      MONARC application: admin@admin.localhost:admin
    
    Login and Password for VirtualBox demo image (format: username:password):
      SSH login (Ubuntu credentials): monarc:password
    
    Database:
      Mysql root login: root:bc17550830486f893127ba8efd4acacc880754cbedddd01a00819b395c53a3fa
      Mysql MONARC login: sqlmonarcuser:2043e9a647bd2a76ac7466c7afc3b86958a6780f933eb05a545294932bb8a1fb
    
    Image integrity check:
      sha512sum: 80ecf52111c795c879fcb299cfed155fc83c052317f09e6396ef438f9ce85490ec918b66418e38846fe59bbfca415a7ba053d410ac431a0eb87c48634a2a9b5b
      sha1sum: ef35b819f37e3931e06e9d33124159779222988b
     
    MONARC is available on port 80.

    MONARC Stats Service is available on port 5005.
