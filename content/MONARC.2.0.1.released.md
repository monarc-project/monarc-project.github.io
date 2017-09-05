Title: MONARC 2.0.1 released
Date: 2017-08-28
Modified: 2017-08-28
Category: monarc
Tags: monarc, new-release
Summary: Release 2.0.1 of MONARC

Version 2.0.1 of MONARC has been released including a security fix, multiple
bug fixes and enhancements.

You can download the new virtual machine
[here](https://github.com/monarc-project/MonarcAppFO/releases/tag/v2.0.1).

Enhancement
===========

- Auto-complete function in the creation of a specific risk (#29)
- Remove the category for operational risk (#26)
- update of the database
- the database of MONARC is now backed up before an upgrade

Fix
===

- Import bug : Format of duedate in recomandation (#30)
- Problem when a label of an impact contains a character such as '&' or '%' (#24)
- Lost operational risks of assets in library after a snapshot (#25)
- Problem setting a comment in new scale row (#24)
- hash of users' passwords were exposed through the API as reported by
  Thomas LARCHER, Cyber Security Team of PwC Luxembourg.
