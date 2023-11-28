# btvnano-prod

Submit crab jobs for btvNano production using crabb.py.

**This branch is set for CMSSW_13_0_13 for NanoV12 production**

## Instruction for user 
Step 1: setup up cmssw & setup crab

```bash
cmsrel CMSSW_13_0_13
cd CMSSW_13_0_13/src
source /cvmfs/grid.cern.ch/centos7-umd4-ui-4_200423/etc/profile.d/setup-c7-ui-example.sh
source /cvmfs/cms.cern.ch/common/crab-setup.sh prod # note: this is new w.r.t. 106X instructions
source /cvmfs/cms.cern.ch/cmsset_default.sh
cmsenv
git cms-merge-topic Ming-Yan:130X-fixPuppi_NanoV12
scram b -j 10
```

Step 2: setup `btvnano-prod` 

```bash
git clone https://github.com/cms-btv-pog/btvnano-prod.git -b NanoAODv12_22Sep2023.
```

Step 2.1 modify the configuration in `crab_ymls`



```yaml

  workArea: data_2022_MINIAODv4_BTagMu
  storageSite: T2_XXX # ===>  change to your storage site
  outLFNDirBase: /store/user/XXX/PFNano_Run3/data_2022_MINIAODv4 # XXX to be user name
  voGroup:  # or if you are dcms
```

Step 3: submit crab jobs configured in `crab_ymls/`.

```bash
# make the submit python file and submit
python3 crabby.py -c crab_ymls/XXX --make --submit 
# Only generate configuration
python3 crabby.py -c crab_ymls/XXX --make --submit 
# This disable publish config and produce single file per dataset
python3 crabby.py -c crab_ymls/XXX --make --submit --test True
```

Step 4: track the production status using nice tool from Jan van der Linden

https://github.com/JanvanderLinden/mrCrabs/tree/main

Step 5: Creation of csv tables with the job progress status.

There is a standalone script ```crab_status.py``` which takes the crab directory from your work area as an input and pars the job status info in a csv table. The csv files are saved in the btveos-www area and can be monitored in browser. It takes a second input of your submitted yml script to make a comparison between datasets and the crab directory outputs. 

Usage:
```python crab_status.py <crab_dir_path> <crab_yml to compare>```

Additionally it produces progress plots for each jobs. You can monitor them here:
```https://btvweb.web.cern.ch/BTVNanoProduction/ProgressPlots/```
To view your tables:
```https://btvweb.web.cern.ch/BTVNanoProduction/csvoutputs/prod_tables.php```
In the drop down menu, select the process that you've produced.

## Notes for developer (TBD)

```
 # data 2022 NanoV12
 cmsDriver.py data_2022_22Sep2023 --conditions 130X_dataRun3_v2 --datatier NANOAOD --era Run3,run3_miniAOD_12X --eventcontent NANOAOD --filein /store/data/Run2022C/BTagMu/MINIAOD/22Sep2023-v1/40000/fc8f31f6-4bf7-4b51-8f6d-ef0833c1e383.root --fileout file:data_defaultAK4.root --nThreads 4 --number -1 --scenario pp --step NANO --data --customise PhysicsTools/NanoAOD/custom_btv_cff.PrepBTVCustomNanoAOD_DATA --customise_commands="process.add_(cms.Service('InitRootHandlers', EnableIMT = cms.untracked.bool(False)));process.MessageLogger.cerr.FwkReport.reportEvery=1000;process.NANOAODoutput.fakeNameForCrab = cms.untracked.bool(True)" --no_exec

 # MC 2022 NanoV12- preEE
cmsDriver.py MC_preEE2022_22Sep2023 --eventcontent NANOAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier NANOAODSIM --fileout file:MC_defaultAK4_preEE.root --conditions 130X_mcRun3_2022_realistic_v5 --step NANO --scenario pp --filein /store/mc/Run3Summer22MiniAODv4/QCD_PT-15to20_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/056b90db-c5cf-4f5f-a4cb-1c69bf4e65b5.root --era Run3  --mc -n -1 --customise PhysicsTools/NanoAOD/custom_btv_cff.PrepBTVCustomNanoAOD_MC  --nThreads 4  --customise_commands="process.add_(cms.Service('InitRootHandlers', EnableIMT = cms.untracked.bool(False)));process.MessageLogger.cerr.FwkReport.reportEvery=1000;process.NANOAODSIMoutput.fakeNameForCrab = cms.untracked.bool(True)"  --no_exec

 # MC 2022 NanoV12 -postEE
cmsDriver.py MC_2022_22Sep2023 --eventcontent NANOAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier NANOAODSIM --fileout file:MC_defaultAK4.root --conditions 130X_mcRun3_2022_realistic_postEE_v6 --step NANO --scenario pp --filein /store/mc/Run3Summer22EEMiniAODv4/QCD_PT-15to20_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2520000/177762d0-23ed-436f-aa0d-a20c33e33dc3.root --era Run3  --mc -n -1 --customise PhysicsTools/NanoAOD/custom_btv_cff.PrepBTVCustomNanoAOD_MC  --nThreads 4  --customise_commands="process.add_(cms.Service('InitRootHandlers', EnableIMT = cms.untracked.bool(False)));process.MessageLogger.cerr.FwkReport.reportEvery=1000;process.NANOAODSIMoutput.fakeNameForCrab = cms.untracked.bool(True)"  --no_exec
```