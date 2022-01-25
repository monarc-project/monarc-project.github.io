Title: MONARC 2.2.0 released
Date: 2018-02-01
Modified: 2018-02-01
Category: monarc
Tags: monarc, new-release
Summary: Release 2.2.0 of MONARC

Version 2.2.0 of MONARC has been released including multiple bug fixes and
enhancements.

### New

- generate deliverable on 4th step of method (#51)
- export all of risk analysis data (#28)

### Enhancement

- option of export tables in a csv file (#52)
- show version MONARC on left panel (#50)
- ensures new users (of the back office) are created with a level of
  permissions (#48)
- the back office displays the appropriate view based on the user permissions
  (#48)
- set the selected attribute for the search filter of models in the back office

### Fix

- user operational risk - tag (#55)
- operational risk - tag (#54)
- detach a tag from an asset (#53)
- operational risk importation (#64)
- various minor fixes in the back office (management of models)

## Updating

To update, check out our
[update](http://monarc.lu/technical-guide/#monarc-update) instructions.

This release includes a consequent changes in the database of the back office
and in the synchronization process of the deliveries templates (between the
back office and the different clients instances). If you are using a back
office, be careful to also update your ansible playbook
([instructions](http://monarc.lu/technical-guide/#update-monarc-when-connected-to-a-back-office)).

You can also download the new virtual machine
[here](https://github.com/monarc-project/MonarcAppFO/releases/tag/v2.2.0).
