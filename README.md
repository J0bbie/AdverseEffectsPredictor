AdverseEffectsPredictor
==========

##Description

<<<<<<< HEAD
This is a database and prediction/analysis algorithm which can be used to store (adverse) side-effect/chemical structure relationships and use this information in the prediction of side-effects in other compounds based on the comparison of binary chemical fingerprints, gene expression omics and related statistics.

##Data used in the prediction/analysis

The following data-sources are used:

-	[FAERS](http://www.fda.gov/Drugs/GuidanceComplianceRegulatoryInformation/Surveillance/AdverseDrugEffects/ucm082193.htm)
	-	Compound-Adverse Effect relationships
-	[SIDER2](http://sideeffects.embl.de/), [PROTECT ADR database](http://www.imi-protect.eu/adverseDrugReactions.shtml)
	-	Compound-Adverse Effect relationships
-	[TG-Gates](ftp://ftp.biosciencedbc.jp/archive/open-tggates/LATEST/README_e.html)
	-	Compound-Gene-expression relationships
-	[Protect ADR](http://www.imi-protect.eu/adverseDrugReactions.shtml)
	-	Compound-Adverse Effect relationships
-	[ChEMBL](https://www.ebi.ac.uk/chembl/)
	-	Compound-Structure relationships
-	DIAMONDS (TNO In-house DB)
	-	Compound-Structure & Compound-Gene-expression relationships
	
##Initial data files

These are the files that were used for the creation of the initial DB, read by the scripts in /writeData2DB/
-	FAERS *(XML formatted)*
	-	ADR13Q1_FORMATTED.xml
-	SIDER2	
	-	*(17-10-2012)*
		-	adverse_effects_raw.tsv
		-	indications_raw.tsv
		-	label_mapping.tsv
		-	meddra_adverse_effects.tsv
		-	meddra_freq_parsed.tsv
-	TG-GATEs
	-	Add 
	-	Add
=======
This is a database and prediction algorithm which can be used to store (adverse) side-effect/chemical structure relationships and use this information in the prediction of side-effects in other compounds based on the comparison of pre-defined binary fingerprints and related statistics.

##Where does the data originate from?

Data from the [SIDER 2](http://sideeffects.embl.de/) database is used as a test-set for the compound-adverse effect relationship. Additional compound-adverse effect relationships are also gathered from the [FAERS / FDA Adverse Event Reporting System](http://www.fda.gov/Drugs/GuidanceComplianceRegulatoryInformation/Surveillance/AdverseDrugEffects/default.htm).

The two data-sources are used to create a test-set of compound-adverse effect relationships. Omics data from additional (in-house) toxicological sources can also be used to further strengthen/weaken a prediction.
>>>>>>> 11030f5bbf37ff76efd190942a346db1afaf235e

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

-	Dependencies:
	-	For writing the initial data-files to the DB
		-	Python 3.4, PyMySQL, optparse, MySQL >= 5.6
	-	AdversePredictor
		-	R, MySQL >= 5.6
	
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

![ERD Database](sql/erdDatabase.png)
