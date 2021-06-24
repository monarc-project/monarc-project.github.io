Title: MONARC 2.10.4 released
Date: 2021-06-24
Modified: 2021-06-24
Category: monarc
Tags: monarc, new-release
Summary: Release 2.10.4 of MONARC

Version 2.10.4 includes bug-fixes.

### New

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
[here](https://my.monarc.lu/static/vm/MONARC_v2_10_4.ova).
Technical details about the VM:


    :::BBCode
    Login and Password for MONARC App (format: username:password):
      MONARC application: admin@admin.localhost:admin
    
    Login and Password for VirtualBox demo image (format: username:password):
      SSH login (Ubuntu credentials): monarc:password
    
    Database:
      Mysql root login: root:e17e0f1693af87db1b56f034cd9da0177bfc9f94e434be7c67db4132d4d093b6
      Mysql MONARC login: sqlmonarcuser:417ec2fa52648ad2c11aecbc008b7f779acbb1772ef49d77e13aac4e9c3c5178
    
    Image integrity check:
      sha512sum: ae3f2533411e3d493e99884cd77b759a2d2569fe9cc5b7d3f9af3e8259dbeb067a36334f39f69759457981ed8a75b35eb6529f456730d4c9081a0abf08c4399e
      sha1sum: 7feb5208e842baca20391e7eb1c5c793e1a67910
     
    MONARC is available on port 80.

    MONARC Stats Service is available on port 5005.
