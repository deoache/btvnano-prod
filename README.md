# pfnano-prod

Submit crab jobs for PFNano production using crabb.py.

Step 1: setup the PFNano (current branch: `13_0_7_from124MiniAOD`)
 according to https://github.com/cms-jet/PFNano/tree/13_0_7_from124MiniAOD#recipe

Step 2: setup `pfnano-prod`

```bash
mkdir $CMSSW_BASE/production
cd $CMSSW_BASE/production
git clone https://github.com/colizz/pfnano-prod.git .
```

Step 3: submit crab jobs configured in `crab_ymls/`.

See introducitons in https://github.com/cms-jet/PFNano/tree/13_0_7_from124MiniAOD#submission-to-crab.
Also, remember to edit the LFN path and storage cite in the config.

```bash
python3 ../test/crabby.py -c crab_ymls/XXX --make
```
Then append `--submit` for submission.

