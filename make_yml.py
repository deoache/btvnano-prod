import yaml
with open('samples.yml', 'r') as f:
    samples = yaml.safe_load(f)

templates = '''campaign:
  name: %NAME%
  crab_template: template_crab.py

  # User specific
  workArea: %NAME%
  storageSite: T2_XXX
  outLFNDirBase: /store/user/XXX/PFNano_Run3/%CAMPAIGN%
  voGroup: null # or leave empty

  # Campaign specific
  tag_extension: %TAG% # Will get appended after the current tag
  tag_mod: # Will modify name in-place for MC eg. "PFNanoAODv1" will replace MiniAODv2 -> PFNanoAODv1
  # If others shall be able to access dataset via DAS (important when collaborating for commissioning!)
  publication: True
  config: %CONFIG%
  # Specify if running on data
  data: %DATA%
  lumiMask: %LUMIMASK% 
  # datasets will take either a list of DAS names or a text file containing them
  # do NOT submit too many tasks at the same time, despite it looking more convenient to you
  # wait for tasks to finish before submitting entire campaigns,
  # it's better to request one dataset at a time (taking fairshare into account)
  datasets: |
    %DATASETS%
'''

def get_config(campaign):
    config_prefix = {
        'mc_summer22_MINIAODv4': 'MC_2022_22Sep2023',
        'mc_summer22EE_MINIAODv4': 'MC_2022_22Sep2023',
        'data_2022_MINIAODv4': 'data_2022_22Sep2023',
    }
    return config_prefix[campaign] + '_NANO.py'

tag_extension = 'BTV_Run3_2022_Comm_MINIAODv4'

for campaign in ['mc_summer22_MINIAODv4','mc_summer22EE_MINIAODv4','data_2022_MINIAODv4']:
    for sam in samples[campaign]:
        name = f'{campaign}_{sam}' 
        templates_write = templates\
            .replace('%NAME%', name)\
            .replace('%CAMPAIGN%', campaign)\
            .replace('%TAG%', tag_extension)\
            .replace('%CONFIG%', get_config(campaign))\
            .replace('%DATA%', 'True' if campaign.startswith('data_') else 'False')\
            .replace('%LUMIMASK%', 'jsons/Cert_Collisions2022_355100_362760_Golden.json' if campaign.startswith('data_') else '')\
            .replace('%DATASETS%', '\n    '.join(samples[campaign][sam]))
        with open(f'crab_ymls/{name}.yml', 'w') as f:
            f.write(templates_write)