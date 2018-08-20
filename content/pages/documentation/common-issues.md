Title: Common issues
Date: 2018-08-20
Hidden: false

[TOC]

## Problem after an update

After an update you may need to delete the cache of MONARC.
For example if you noticed that the version number of MONARC,
in the left menu, is wrong or MONARC still says that it is
not up-to-date.

Possible solution:

* delete the cache of MONARC ``data/cache``


## Not receiving password reset emails

This is very unlikely a problem of MONARC.

* check the configuration of Postix (/etc/postfix/main.cf) on the MONARC
  server. Especially the address of the SMTP relay server (the line
  starting with _relayhost_);
* check the configuration of your SMTP relay server. Most of the time a
  rule will block the sending of the email.

## GitHub token problem during MONARC update

Because of GitHub's rate limits on their API it can happen that Composer
prompts for authentication asking your token so it can go ahead with its work.

The best solution is to generate your own token and store it on the server:

1. [Create](https://github.com/settings/tokens) an OAuth token on GitHub;
2. Add it to the configuration running ``composer config -g github-oauth.github.com <oauthtoken>``.
   Do this on the MONARC server and on the MONARC back office server.
