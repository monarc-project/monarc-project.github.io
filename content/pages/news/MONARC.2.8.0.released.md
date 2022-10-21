Title: MONARC 2.8.0 released
Date: 2019-03-01
Modified: 2019-03-01
Category: monarc
Tags: monarc, new-release
Summary: Release 2.8.0 of MONARC


Version 2.8.0 of MONARC has been released with important changes and new
features.

The notable changes are described below.

[TOC]

### New

#### Management of multiple security referentials

We are thrilled to announce that MONARC now supports multiple
security referentials per analysis. Without limit of number.

![Referentials](/assets/images/posts/MONARCv2.8-Referentials.png#center "Referentials")


After the update to MONARC 2.8 your existing analysis with legacy measures from
MONARC will by default use the controls from ISO/IEC 27002. Nothing will change
automatically. Of course you will be able to import new referentials via the
knowledge base. It's the goal.

#### Mapping between security referentials

Since it is now possible to use several security referentials, having the
possibility to match security controls seems natural and should be
straightforward. And as you can see below, it is.

![Mapping between security referentials](/assets/images/posts/MONARCv2.8-ReferentialsMatching.png#center "Mapping between security referentials")

A mapping can be created manually via the knowledge base of MONARC, as you can
see above. Or simply by uploading a mapping shared by the
community (with a CSV or a JSON file).

It is even possible to export your own mapping in a CSV file.

When exporting a whole risk analysis you have the opportunity to export the
statement of applicability which includes the referentials and the mapping you
have created.


#### Improvements to the statement of applicability

- It is now possible to filter on a security referential in the statement of
applicability;
- The code of the page has been refactored and loads faster.

![Statement of applicability](/assets/images/posts/MONARCv2.8-SOA.png#center "Statement of applicability")

#### Batch import of objects

You can import new objects in the knowledge base of your
analysis with a CSV, XLXS or JSON file. This concerns the following objects:

- asset types;
- threats;
- vulnerabilities;
- referentials;
- tags;
- operational risks.

![Import center](/assets/images/posts/MONARCv2.8-ImportCenter.png#center "Import center")


#### New chart for the dashboard

A new compliance chart has been added.

![Compliance chart](/assets/images/posts/MONARCv2.8-ComplianceChart.png#center "Compliance chart")


#### MONARC Objects Sharing Platform

Last but not least, we want to take this opportunity to
introduce [MOSP](https://objects.monarc.lu) (MONARC Objects Sharing Platform).

Basically MOSP is a platform to create, edit and share valid JSON objects.  
MOSP supports any kind of JSON objects, you just have to specify a JSON schema.
The instance objects.monarc.lu, operated by [NC3-LU](https://nc3-lu.github.io),
is dedicated to gather security related objects in the first place aimed to be used
with MONARC. And our instance is [open](https://objects.monarc.lu/login).

Have a look at the available objects provided by the MONARC
project:

- [Security referentials](https://objects.monarc.lu/schema/12)
- [Security referentials mapping](https://objects.monarc.lu/schema/13)

You can import these objects in MONARC.

#### Identifying objects

And now something a little under the hood but **really** important.
The release 2.8 of MONARC introduces the usage of UUIDs
for the *referential* and *measure* objects
(we will generalize the use of UUIDs for other relevant objects).  

> **UUIDs are crucial** in order to empower the sharing of objects.
>
> - A unique identifier enable to designate an object (asset, threat,
>   referential, etc.), for example independently from its language;
> - Using a common format enable to compare objects of the same kind (same
>   *schema*).

Our new platform addresses the two points above **and** promotes the
sharing of information.  
MOSP also provides an API in order to query it programmatically. This means that
MONARC will soon be able to retrieve data from MOSP.

You will find more information about MOSP in the
[documentation](/documentation/MOSP-documentation).


### Enhancement

- the code of the page which displays the dashboard has been refactored and
  loads faster.


### Fix

- Fixed an issue when deleting threat theme [#143](https://github.com/monarc-project/MonarcAppFO/issues/143);
- Improved the go back on risk sheet [#95](https://github.com/monarc-project/MonarcAppFO/issues/95);
- some minor bugs concerning the dashboard have been resolved.


## Updating

To update, check out our
[update](http://monarc.lu/documentation/technical-guide/#monarc-update)
instructions.
This is an important release with database migrations.
Backup your database first.

You can also download the new virtual machine
[here](https://github.com/monarc-project/MonarcAppFO/releases/tag/v2.8.0).


We want to thank all contributors and reporters.
Especially [ANSSI-LU](https://cybersecurite.public.lu/fr/securite-information/mission.html) for their
help with the German translations.

## Training

Do not forget our next [training](/trainings) in March (which will be given in
French).

<script type="text/javascript" src="https://PTGAFFQ-modules.xing-events.com/resources/js/amiandoExport.js"></script><iframe src="https://PTGAFFQ-modules.xing-events.com/PTGAFFQ.html?viewType=iframe&distributionChannel=CHANNEL_IFRAME&language=en&useDefaults=false&resizeIFrame=true" frameborder="0" width="650px" id="_amiandoIFrame3572043"><p>This page requires frame support. Please use a frame compatible browser to see the ticket sales module.</p><p> Try out the <a href="https://en.xing-events.com/">online event registration system</a> from XING Events.</p></iframe>More participants thanks to <a href="https://en.xing-events.com?viralRefId=PTGAFFQ&utm_campaign=ev-PTGAFFQ&utm_medium=viral&utm_source=EventWebsite&utm_content=TextLinkBottom&utm_term=text-link" target="_blank" alt="XING Events" title="XING Events">online event management solutions</a> from XING Events.
