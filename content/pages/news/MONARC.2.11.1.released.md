Title: MONARC 2.11.1 released
Date: 2021-10-28
Modified: 2021-10-28
Category: monarc
Tags: monarc, new-release
Summary: Release 2.11.1 of MONARC

Version 2.11.1 includes a new feature and various bug-fixes.

### New

- Add import of referential mapping from MOSP
  ([#391](https://github.com/monarc-project/MonarcAppFO/issues/391)).

### Fix
- Subsuming CIA criteria according to the maximum criteria does not work
  ([#339](https://github.com/monarc-project/MonarcAppFO/issues/339)).
- Incorrect sum and list of risks under the secondary assets
  ([#367](https://github.com/monarc-project/MonarcAppFO/issues/367)).
- If impact adjustments are made not only at the level of the primary assets but also at the level of the secondary assets, these assets are listed more than once
  ([#387](https://github.com/monarc-project/MonarcAppFO/issues/387)).
- Recommendation status change error in the Knowledge Base
  ([#393](https://github.com/monarc-project/MonarcAppFO/issues/393)).
- Import issue of setting operational risks values
  ([#394](https://github.com/monarc-project/MonarcAppFO/issues/394)).
- Fix possible circular iteration of the instance root -> parent -> child rendering
  ([#395](https://github.com/monarc-project/MonarcAppFO/issues/395)).
- Mathematical representation of large numbers in the dashboard
  ([#398](https://github.com/monarc-project/MonarcAppFO/issues/398)).


## Updating

To update, please follow the 
[guide](http://monarc.lu/documentation/technical-guide/#monarc-update).

If you would like to use the new statistics feature then
[StatsService](https://github.com/monarc-project/stats-service) has to be setup
as well.
The documentation, architecture and installation instructions of Stats Service
can be found [here](https://www.monarc.lu/documentation/stats-service).

More details and notes are available on
[GitHub](https://github.com/monarc-project/MonarcAppFO/releases/tag/v2.11.1).


## <a href="#vm-image">The VirtualBox demo image</a>

Download the OVA image of this release
[here](https://vm.monarc.lu/MONARC_v2.11.1@009f374/).
