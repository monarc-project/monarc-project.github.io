Title: Product

[TOC]

<style>
th:not(:first-child) {
  text-align: center;
}

td:not(:first-child)  {
  text-align: center;
  color: #ffd500;
  text-shadow: 1px 0 grey, -1px 0 grey, 0 -1px grey, 0 1px grey;
}
</style>

## Features summary

There are 2 different [MONARC](https://github.com/monarc-project/MonarcAppFO)
installations possible:

 - MONARC Instance Management (also known as MONARC BackOffice or BO)
 - MONARC (Also known as MONARC FrontOffice or FO)

The table below summarises the functionality of both versions:

<table class="table">
    <thead>
        <tr>
            <th>Features</th>
            <th>MONARC FrontOffice</th>
            <th>MONARC BackOffice</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Creation, edition, management of risk analysis</td>
            <td>&#10004;</td>
            <td></td>
        </tr>
        <tr>
            <td>Reports generation</td>
            <td>&#10004;</td>
            <td></td>
        </tr>
        <tr>
            <td>Import and export of risk analysis</td>
            <td>&#10004;</td>
            <td></td>
        </tr>
        <tr>
            <td>Fine management of permissions per projects</td>
            <td>&#10004;</td>
            <td></td>
        </tr>
        <tr>
            <td>Management of users per projects</td>
            <td>&#10004;</td>
            <td></td>
        </tr>
        <tr>
            <td>Database of risk models</td>
            <td>&#10004;</td>
            <td>&#10004;</td>
        </tr>
        <tr>
            <td>Management of risk models</td>
            <td>&#10004;</td>
            <td>&#10004;<span style="color:#555555;text-shadow:none"> **</span></td>
        </tr>
        <tr>
            <td>Creation and removal of MONARC instances</td>
            <td></td>
            <td>&#10004;</td>
        </tr>
    </tbody>
</table>

<span style="font-size:small">** <i>Accross multiple MONARC FrontOffice</i></span>

<br/>The MONARC Instance Management is appropriate for big organizations or state
organizations. More derails about the architecture
[here](/technical-guide#monarc-and-the-back-office).

Since MONARC is an open-source project, you can also have a look at our
[roadmap](https://github.com/monarc-project/MonarcAppFO/wiki/Roadmap).


## MONARC Instance Management
As an operator or service provider having multiple clients that desire
to use MONARC for their risk assessment, this would be the optimal
solution. It provides a centralised management of all the instances.
This means that you as service provider have a dashboard-like view of
how many clients you have. You can add and remove MONARC Instances
(Front Offices) and import Risk Models that are automatically accessible
to all your instances.
> As a bank, you might have different departments in different countries
and thus the risk assessment varies - yet the model stays the same. Thus
this would be a much easier way to share objects between departments
with a centralised import - no need to import the model in each instance!

It is to be noted, that you do not have access to the different
instances and that the user management for each instance is done on the
instance itself. This is a conscious choice to allow an administrator to
create instances but not give access at the same time. This gives the
admin for each MONARC instance the power to really manage the access of
their instance.

It is to be noted that the MONARC instance management is only
interesting, if the implementation should result in some sort of cloud and you are the
service provider. If you only wish to conduct risk assessment and your
are a single small to medium sized company, we suggest you have an
installation of a single MONARC instance without the Instance
Management. This will take less maintenance.

## MONARC
The risk assessment is done in a MONARC instance, not the Instance
Management. Each instance has, after all, its own user management -
inaccessible by the MONARC Instance Management - to control access by
user and risk analysis.

### User management
User management is done by the administrators of each instance (there
can be mutliple administrators per instance). So if a user creates a
risk analysis to perform a risk assessment, she or he have read/write
permissions for that analysis only. No user sees or can access the risk
analysis from any other users by default. It is the work of the instance
administrator to grant access. The choices are as follows:

1. No access
2. Read only
3. Read/Write

These are kept very simple and is by design. If it is desired to create
different departments with each of them only being allowed to write to
their respective objects but read only on the others, we suggest to
create different risk analysis' with the desired permissions. It is easy
to combine the risk analysis later through "export/import" into a new
analysis for a combined report.

### Import and export
It is possible to import and export all the risk model information and
thus share between instance. Or simply import the risk model from one
instance in the MONARC Instance Management if multiple instances could
benefit from that model, effectively removing the need to import and
update that model on each instance.
