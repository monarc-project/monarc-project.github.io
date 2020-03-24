Title: MONARC 2.9.11 released
Date: 2020-02-24
Modified: 2020-02-24
Category: monarc
Tags: monarc, new-release
Summary: Release 2.9.11 of MONARC

Version 2.9.11 of MONARC has been released with several fixes and a new feature.


### New

- added users creation command
  ([PR 27](https://github.com/monarc-project/zm-client/pull/27));
- backend has been migrated from Zend Framework to Laminas
  ([#249](https://github.com/monarc-project/MonarcAppFO/issues/249)).


### Fix

- The description area of the shelf life is too fair at the character level
  ([#252](https://github.com/monarc-project/MonarcAppFO/issues/252));
- In the description of destinations area; info is not kept after registration
  ([#253](https://github.com/monarc-project/MonarcAppFO/issues/253));
- [GDPR module] Issue when creating a new recipient with default values
  ([#254](https://github.com/monarc-project/MonarcAppFO/issues/254));
- Get the list controls in BO
  ([#256](https://github.com/monarc-project/MonarcAppFO/issues/256));
- fix: improved performance when drag and dropping assets
  ([ff473d9](https://github.com/monarc-project/zm-core/commit/ff473d96b51ddbdbcd8e6c59927e59f246b7b67b)).



## Updating

To update, please follow the instructions guide.
[update](http://monarc.lu/documentation/technical-guide/#monarc-update) instructions.

If you are coming from MONARC 2.9.0 please read
[this](/news/2019/11/25/monarc-291-released/#updating).

---

> The new version comes with the php framework upgrade. We changed usage of "Zend Framework 3" to "Laminas", which is a new official repository of the framework.
> As Zend Framework will not longer be maintained, we had to make the transition as soon as possible. We also recommend to perform the update for you.
>
> To be able to install the Laminas framework, it is mandatory to have "composer" (php dependency manager) version on your server >= 1.9.0.  
> We added the version validation in the update-all.sh script, which will show you a warning message with instructions in case if your "composer" version is outdated.
>
> Please, contact us in case if you have any issues during the update process.

---

You can also download the new virtual machine
[here](https://github.com/monarc-project/MonarcAppFO/releases/tag/v2.9.11).
