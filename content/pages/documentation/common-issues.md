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

* delete the cache of MONARC in the folder ``data/cache``.


## Not receiving password reset emails

This is very unlikely a problem of MONARC.

Check the logs in the files */var/log/syslog* and */var/log/mail.log*.

Possible solutions:

* check the configuration of Postfix (/etc/postfix/main.cf) on the MONARC
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

## A blank screen is displayed

A blank screen is generally caused by a faulty database connection.

Possible solutions:

* check manually the connection to the database;
* check the Apache error logs for database related problems. This can also be
  caused by a PHP library (for example Doctrine). In this case launch again the
  update script (*scripts/update-all.sh*) then delete the cache of MONARC.

## Is it possible for a back office administrator to change the administrator user of a MONARC instance?

The answer is no. This is a design choice that has been made for security reason.
An administrator of the back office is only able to create and delete MONARC
instances (clients) on a MONARC server. The administrator has no access to the
MONARC instances.

A minimum of one administrator per MONARC instance is recommended.
The management of users on a specific MONARC instance is the responsibility
of administrator of the instance.
The administrator of the back office should not be responsible of this.

## Adding a new administrator without access to the MONARC Web interface

Considering, for example, that an employee with administrator rights on MONARC
recently left the company.

You must have a SSH access to the server where MONARC is installed.

**Situation 1**

If you are using MONARC without back office, simply run this command at the
root of MONARC:

    $ php ./vendor/robmorgan/phinx/bin/phinx seed:run -c ./module/MonarcFO/migrations/phinx.php

This will create a new administrator account with the login *admin@admin.test*
and the password *admin*.

**Situation 2**

If you are using a back office, as explained in the previous section, it is not
possible to change the adminstrator of a MONARC instance or to add a new one.
Clients databases are separated.  
A simple solution would be to update the email address of the former
administrator directly in the client database (on the FO server), with your own
email address.
Then you will be able to use the passord recovery feature of MONARC.

