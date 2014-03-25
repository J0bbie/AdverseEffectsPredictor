AdverseEffectsPredictor
==========

##Description

This is a database and prediction algorithm which can be used to store (adverse) side-effect/chemical structure relationships and use this information in the prediction of side-effects in other compounds based on the comparison of pre-defined binary fingerprints and related statistics.

##Where does the data originate from?

Data from the [SIDER 2](http://sideeffects.embl.de/) database is used as a test-set for the compound-adverse effect relationship. Additional compound-adverse effect relationships are also gathered from the [FAERS / FDA Adverse Event Reporting System](http://www.fda.gov/Drugs/GuidanceComplianceRegulatoryInformation/Surveillance/AdverseDrugEffects/default.htm).

The two data-sources are used to create a test-set of compound-adverse effect relationships. Omics data from additional (in-house) toxicological sources can also be used to further strengthen/weaken a prediction.

##Predictors used
The binary fingerprints which are deduced from the compounds and used in the prediction of side-effects are the following:
- Chemical groups
- logP  (Partition coefficient)
- Molecular mass
- Protein targets
- Metabolite forming
- Quantum mechanics

Gene expression data (Omics) is also used as an additional resource in the prediction.

##Installation/setup

**Describe this**

##Examples

Examples are added in the /examples/ folder.

##Impressions

###Impression interface

**Insert impression here**

###Impression data-output

**Insert impression data-output here**

##Flowcharts 

**Insert flowcharts here**

##ERD

**Insert ERD here**
