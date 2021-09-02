Title: MONARC 2.11.0 released
Date: 2021-09-02
Modified: 2021-09-02
Category: monarc
Tags: monarc, new-release
Summary: Release 2.11.0 of MONARC

Version 2.11.0 includes a major new feature and various bug-fixes.

### New

- having the possibility to define custom scales for operational risks
  ([#353](https://github.com/monarc-project/MonarcAppFO/issues/353));
- introduction of the risk context and the risk owner
  ([#21](https://github.com/monarc-project/MonarcAppFO/issues/21),
  [#186](https://github.com/monarc-project/MonarcAppFO/issues/186)).


![Custom scales for operational risks](/assets/images/posts/evaluation-scales-custom-op-risks.png#center "Custom scales for operational risks")

![Example of custom operational risk](/assets/images/posts/custom-op-risks-example.png#center "Example of custom operational risk")

![Context and owner of risk](/assets/images/posts/context-and-owner.png#center "Context and owner of risk")


### Fix

- update-all.sh: Could not read from remote repository
  ([#365](https://github.com/monarc-project/MonarcAppFO/issues/365));
- some files in script do not have the correct permissions
  ([#364](https://github.com/monarc-project/MonarcAppFO/issues/364)).


## Updating

To update, please follow the 
[guide](http://monarc.lu/documentation/technical-guide/#monarc-update).

If you would like to use the new statistics feature then
[StatsService](https://github.com/monarc-project/stats-service) has to be setup
as well.
The documentation, architecture and installation instructions of Stats Service
can be found [here](https://www.monarc.lu/documentation/stats-service).

More details and notes are available on
[GitHub](https://github.com/monarc-project/MonarcAppFO/releases/tag/v2.11.0).


## <a href="#vm-image">The VirtualBox demo image</a>

Download the OVA image of this release
[here](https://my.monarc.lu/static/vm/MONARC_v2.11.0_65bed51382debaf4f87c9774618cb75df3d6044f.ova).
Technical details about the VM:


    :::BBCode
    Login and Password for MONARC App (format: username:password):
      MONARC application: admin@admin.localhost:admin
    
    Login and Password for VirtualBox demo image (format: username:password):
      SSH login (Ubuntu credentials): monarc:password
    
    Database:
      Mysql root login: root:a7daab4243ed998c7e61dc6e4aa48f64dda354021778379ec11e75430534693e
      Mysql MONARC login: sqlmonarcuser:8c125ed24f4cf1fe50ec8ac4450c81c98b65475677956242bb9385e97fa4027d
    
    Image integrity check:
      sha512sum: a39110feac44558acf0d018d14978040f970cc306554ab3c02ad1af1bde5a3a94a5f7da3e5cd20d9ee2146ed02cbc7f69a7a9533766c173d989f02ec4d523290
      sha1sum: a304f8301e5c0116f8c94d6a143eb48b189f03fa
     
    MONARC is available on port 80.

    MONARC Stats Service is available on port 5005.
