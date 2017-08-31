Title: Quick Start
Tags: documentation, quick start

* <a href="#Introduction">Introduction</a>

* <a href="#Creating the first risk analysis">Creating the first risk analysis</a>

* <a href="#Description of the main view">Description of the main view</a>

* <a href="#Simplified risk analysis">Simplified risk analysis</a>

    * <a href="#Risk identification (default modeling)">Risk identification (default modeling)</a>

    * <a href="#Edit impacts and consequences">Edit impacts and consequences</a>

    * <a href="#Risk assessment">Risk assessment</a>

    * <a href="#Risk treatment">Risk treatment</a>

    * <a href="#Risk treatment plan management">Risk treatment plan management</a>

<a name="Introduction" />
### **Introduction**
#### Purpose

The purpose of this document is to help get started quickly with MONARC. It explains the main features of the tool and the necessary steps to deal with a risk with the default settings.

#### Other documents
* [**Tool guide**](/Tool-guide): Complete documentation of the tool.
* [**Method guide**](/Method-guide): Complete documentation of the method.
* [**Technical guide**](/technical-guide): Complete technical documentation.

#### Syntax used in the document

![Cursor](./images/Step.png) : All numbers in white on a red background are used on print-screen views to provide additional explanations. Explanations are always after the view with the corresponding numbering. **i.e.** 1.

`Reference` : MONARC Reference

#### Syntax used in MONARC
![Menu](./images/Menu.png) : Button that always brings up the menu.

![Create](./images/CreateButton.png) : Creating/adding something in context (assets, recommendations, etc.).

![Cursor](./images/Cursor.png) : Most fields of MONARC display additional information when the pointer stay unmoved some time.

<a name="Creating the first risk analysis" />
### **Creating the first risk analysis**
After clicking on `Create a risk analysis`, the following pop-up appear

![Create a risk analysis](./images/NewRiskAnalysis.png)

1. Select `CASES model`
1. There are at least two choices. Select `Modelling CASES`, this is the default template. It provides sufficient knowledge bases to start an analysis.
1. `Show inherent operational risks`. This option does not matter right now.
1. Select your preferred language for this new analysis. (FR/EN/DE)
1. Give your analysis a name, for example _My analysis_.
1. Optional field, which allows you to describe your analysis with more details.

<a name="Description of the main view" />
### **Description of the main view**
![Main view](./images/Main.png)

1. Risk Analyses panel: Create and select a risk analysis. Once the analysis is selected, the dashboard can be retracted to optimize the horizontal space by clicking on the symbol ![Hide Risk Analyses panel icon](./images/HideRiskAnalysesPanel.png).
1. Navigation panel, users administration and account management.
1. Access to steps of the method by clicking on numbers 1 to 4.
1. Contextual working areas of analysis.

<a name="Simplified risk analysis" />
### **Simplified risk analysis**

<a name="Risk identification (default modeling)" />
####	Risk identification (default modeling)
It is necessary to use the assets of the library and place them in the analysis.
If the risk analysis does not contain any assets, follow the instructions below, otherwise go to the next chapter.
MONARC proposes by default a structure where primary assets (Business) must be placed on the root of the analysis and supporting assets below. In order to simplify this step, two groups of assets have been created:

* `Front-Office`: This asset group provides the identification of the common risks found on the user’s side for a “Human Resources” department (for example, risks related to the office, computers, applications, physical & environmental risks…).

* `Back-Office`: These assets group provide the identification of transversal risks of the organization related to the IT and to organizations in general.

![Modelling](./images/Modelling.png)

Click on the `+` or the `-` to expand or wrap all categories of the library.

1. In the category `Primary assets`, click on `Department` and then, by holding down the left mouse button, move the asset to the analysis area just above (Drag and Drop).

1. In the category `Model Structure`  find the assets `Front Office` and `Back Office` and then, by holding down the left mouse button, move the asset on the asset Department, which is now in the analysis area.

![Model](./images/Model.png)

1. The risk analysis now offers a model for *Department*.
1. The *Front Office* now offers a default identification of the risks on the users’ side.
1. The *Back Office* now offers a default identification of the risks, for IT and organization.
1. The total number of risks in this model is 84 (in this case).

**Note**: Identified risks by default are the risks commonly encountered and supposed to be significant, they do not claim to be exhaustive.

<a name="Edit impacts and consequences" />
####	Edit impacts and consequences
The aim is to define impacts and consequences for primary assets that can result from an occurrence of a risk from the model.
In the case of this analysis, the primary asset is *Department*.

![Edit impacts](./images/EditImpacts.png)

1. Click on the primary asset `Department`.
1. Click on the symbol![Menu](./images/Menu.png)to display the context menu of the asset.
1. Click on `Edit impacts`.

The pop-up below appears.

![Impacts](./images/Impacts.png)

1. Consultation of impact scales is done through the menu at the top right of the screen. *By leaving the pointer unmoved over the numbers, the meaning of this number appears after one second.*

When one of the criteria **C** (confidentiality), **I** (integrity) or **A** (availability) is allocated, there is a need to ask : what are the consequences on the company, and more particularly on its ROLFP, i.e. its **R**eputation, its **O**peration, its **L**egal, its **F**inances or the impact on the **P**erson (in the sense of personal data).

In the case of the above figure, the `3` (out of 5) impact on confidentiality, is explained by the maximum value ROLFP regarding confidentiality. Example, `3` is the consequence for the person in case of disclosure of his personal file.

<a name="Risk assessment" />
#### Risk assessment

![Risk assessment](./images/RiskAssessment.png)

1. Click on a secondary asset, for example `Building`.
1. `CIA Impact`: It has been assigned to the *Department* is inherited by default and are no longer required.
1. `Threat`: *Theft or destruction of media, documents or equipment* is a physical threat that expresses fear of being robbed or destroyed materials.
1. `probability (Prob.)` : This is an estimate of the probability on a scale of 1 to 4 that the threat occurs. Take, for example, the case of a very large company where this threat is above average, so **3**.
1. `Vulnerability`: *The principle of least privilege is not applied*. The security principles searched are to know who has access rights and whether they related to the duties of the people involved.
1. `Existing controls`: Describe, in a factual manner, the security controls in place regarding this vulnerability or, more broadly, the risk in question. Take, for example, a second unfavorable case, for example a hospital where the whole building is like a public area.
1. `Qualification (Qualif.)` : In relation to the measure in place (point 6 above), the vulnerability qualification is therefore maximum **5** out of 5.
1. `Current Risk` : All the parameters for calculating the risk are present, the current risk is therefore calculated based on the CIA values, which are directly dependent on the threat.

**Note**: By leaving the pointer on most fields, a tooltip appears after 1 second.

<a name="Risk treatment" />
#### Risk treatment

The risk treatment consists in proposing one of the 4 types of treatment, knowing that most of the time the treatment is to reduce the risk by allocating a control, or to accept a weak risk. To access click on `Not treated` in *Treatment column*.

![Risk treatment](./images/RiskTreatment.png)

1. Create one or many recommendations.
1. Define the treatment type (according to ISO / IEC 27005).
1. Estimate the risk-reducing value in order to define the residual risk.
1. Save the treatment.

<a name="Risk treatment plan management" />
#### Risk treatment plan management

![Plan risk treatment](./images/PlanTreatment.png)

In that case, the risk treatment plan only consists in one risk, but once all risks are treated, all risks and information risk recommendations will be in the treatment plan.

1. The call of the pop-up is done by clicking on the 3rd step of the method and `Risk treatment plan management`.
1. Order the recommendation positions holding down the left mouse button on symbol ![Move button](./images/MoveButton.png) and move it.
1. Reset the positions in importance order (Imp.)
1. Edit recommendation

A final report of risk analysis can be generated by clicking on the 3rd step of the method and `Deliverable: final report`.

**Note**: Deliverables are only relevant when the MONARC method has been fully processed and all information has been entered.
