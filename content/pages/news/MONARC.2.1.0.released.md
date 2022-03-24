Title: MONARC 2.1.0 released
Date: 2017-12-04
Modified: 2017-12-04
Category: monarc
Tags: monarc, new-release
Summary: Release 2.1.0 of MONARC

Version 2.1.0 of MONARC has been released including multiple bug fixes and
enhancements.

## Enhancement

- cleaning of the initial database structure.
- split database model and data.
- simplify the panel to create new MONARC clients.
- improved the table of MONARC clients of the administration panel.
- removed all useless column of the 'clients' table.
- removed cities and countries tables in the database.
- added a condition to hide/show probability field on Threats assessment.
- it is now possible to export a whole analysis (or an asset) in JSON or as an
  encrypted JSON file. Analysis exported with the legacy system can still be
  imported in MONARC.
- it is now mandatory to specify a level of permissions when creating a new
  user.

## Fix

- minor fixes in the forms of the user profile page.
- minor translations fixes.
- fixed a bug that prevented users to update password without the
  password recovery feature.

## Updating

To update, check out our
[update](http://monarc.lu/technical-guide/#monarc-update) instructions.

You can also download the new virtual machine
[here](https://github.com/monarc-project/MonarcAppFO/releases/tag/v2.1.0).
