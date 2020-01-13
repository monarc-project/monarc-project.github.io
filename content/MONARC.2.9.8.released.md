Title: MONARC 2.9.8 released
Date: 2020-01-13
Modified: 2020-01-13
Category: monarc
Tags: monarc, new-release
Summary: Release 2.9.8 of MONARC

Version 2.9.8 of MONARC has been released with several fixes.

---

>This release as well as previous releases since 2.9.0 contain(s) important fixes:
>
> - preventing losing recommendations during assets removal from your analysis;
> - library categories management fixes;
> - global objects operations fixes (impact propagation, existing controls field modification);
> - snapshots creation without comment;
> - other fixes and improvements.
> 
> We would recommend you to upgrade to the version to avoid those issues.
> 
> If your current version is lower then 2.9.1, please don't forget to follow the upgrade instructions:
> [2.9.1 release notes](https://www.monarc.lu/news/2019/11/25/monarc-291-released/).

---


### Fix

- Library categories management issues
  ([#221](https://github.com/monarc-project/MonarcAppFO/issues/221));
- Library -> global asset -> delete asset
  ([#229](https://github.com/monarc-project/MonarcAppFO/issues/229));
- Library -> asset -> Asset used in the risks analysis
  ([#218](https://github.com/monarc-project/MonarcAppFO/issues/218)).

## Updating

To update, check out our
[update](http://monarc.lu/documentation/technical-guide/#monarc-update) instructions.
If you are coming from MONARC 2.9.0 please read
[this](/news/2019/11/25/monarc-291-released/#updating).

You can also download the new virtual machine
[here](https://github.com/monarc-project/MonarcAppFO/releases/tag/v2.9.8).
