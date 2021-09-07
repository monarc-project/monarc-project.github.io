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
[here](https://vm.monarc.lu/MONARC_v2.11.0-p1@5a1cb27/).
