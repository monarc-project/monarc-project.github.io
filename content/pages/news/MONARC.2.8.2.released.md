Title: MONARC 2.8.2 released
Date: 2019-05-28
Modified: 2019-05-28
Category: monarc
Tags: monarc, new-release
Summary: Release 2.8.2 of MONARC

Version 2.8.2 of MONARC has been released with several improvements.

### New

- the MONARC core objects (assets, threats, vulnerabilities and risks) are now
  identified with UUIDs. We published the objects on the
  [MONARC objects sharing platform](https://objects.monarc.lu). Risks from
  the CASES models are also [available](https://objects.monarc.lu/schema/16);
- Assets, threats, vulnerabilities, risks and referentials can be imported
  in the knowledge base of your analysis from MOSP without leaving the MONARC
  user interface.

![Import a risk from MOSP](/assets/images/posts/import_risk_from_MOSP.png#center "Import a risk from MOSP")
Example with the risk object
[7f9f704b-4f02-11e9-b3ea-0800277f0571](https://objects.monarc.lu/object/7f9f704b-4f02-11e9-b3ea-0800277f0571).

### Enhancement

- Adding referential afterwards does not update the knowledge base
  [#156](https://github.com/monarc-project/MonarcAppFO/issues/156).

### Fix

- Import analysis in 2.8.1, exported from 2.7.2, gives errors [#152](https://github.com/monarc-project/MonarcAppFO/issues/152);
- Edit label of added Referentials does not work [#153](https://github.com/monarc-project/MonarcAppFO/issues/153);
- Problem generating deliverable [#157](https://github.com/monarc-project/MonarcAppFO/issues/157);
- Categories are duplicated in import [#158](https://github.com/monarc-project/MonarcAppFO/issues/158);
- Getting prob & impacts on operational risks [#161](https://github.com/monarc-project/MonarcAppFO/issues/161).


## Updating

To update, check out our
[update](http://monarc.lu/documentation/technical-guide/#monarc-update) instructions.

You can also download the new virtual machine
[here](https://github.com/monarc-project/MonarcAppFO/releases/tag/v2.8.2).
