import os
from urllib.request import urlopen
import json 

import ruamel.yaml
import pandas as pd

# First get all contribs across repos
all_files = ["https://raw.githubusercontent.com/pyOpenSci/python-package-guide/main/.all-contributorsrc",
             "https://raw.githubusercontent.com/pyOpenSci/software-peer-review/main/.all-contributorsrc",
             "https://raw.githubusercontent.com/pyOpenSci/pyopensci.github.io/main/.all-contributorsrc"]

def flatten_list(l):
    return [item for sublist in l for item in sublist]   

# Open all contributors, deserialize json to dict / pandas?
all_contribs = []
for file in all_files:
    with urlopen(file) as url:
        data = json.load(url)
        all_contribs.append(data["contributors"])

contribs_flat = flatten_list(all_contribs)

all_keys = ["mastodon", "twitter", "bio", "orcidid", 
            "contributor_type", "packages-submitted", "packages-reviewed"]
# Modify contribs (turn into function)
for acontrib in contribs_flat:
    # Change login: sumit-158 to github username github_username: "lwasser"
    # change profile profile --> website: "website-here.com"
    acontrib['github_username'] = acontrib.pop('login')
    acontrib['website'] = acontrib.pop('profile')
    # Parse avatar id from string avatar_url: https://avatars.githubusercontent.com/u/118582?v=4 --> github_image_id: 30430
    gh_avatar_num = acontrib['avatar_url'].rsplit('/', 1)[-1].rsplit('?', 1)[0]
    # 
    acontrib['github_image_id'] = acontrib.pop('avatar_url') 
    acontrib['github_image_id'] = int(gh_avatar_num)
    # Add keys needed in website yaml
    for akey in all_keys:
        # TODO: turn "" or None into a blank in the yaml file
        acontrib.update({akey:""})

# It's much easier to remove dups with pandas
contribs_df = pd.DataFrame.from_dict(contribs_flat).sort_values(by=['github_username']).drop_duplicates(subset=['github_username'])
contribs_df.drop(['contributions'], axis=1, inplace=True)
contribs_dict = contribs_df.reset_index().to_dict(orient='records')


# Next - open the existing yaml file, and look for each "github username"
# So it comes in as a dict vs ordered dict
yaml = ruamel.yaml.YAML(typ='safe')
with open(os.path.join("_data", "contributors.yml"), "r") as contrib_file:
    web_contribs = yaml.load(contrib_file)

web_contribs_df = pd.DataFrame.from_dict(web_contribs)

# Now compare github user names between contribs_df and web_contribs_df
web_contribs_df[["name", "github_username"]]   


# Diff against the web yaml list - case insensitive
bool = contribs_df["github_username"].apply(str.lower).isin(web_contribs_df['github_username'].apply(str.lower))
new_contributors_dict = contribs_df[~bool].reset_index(drop=True, inplace=True).to_dict(orient='records')
# Add each username that doesn't already exist in the file to the bottom of the file


with open(f"_data/contributors-test.yml",'r') as all_contrib:
    yaml = ruamel.yaml.YAML(typ='safe')
    all_contrib = yaml.load(all_contrib) 
    all_contrib.extend(new_contributors_dict)

# Output to contributor file to yaml
with open(f"all-pyos-contributors.yml", "w") as file:
    # yaml.dump need a dict and a file handler as parameter
    yaml = ruamel.yaml.YAML(typ='safe')
    #yaml.indent(sequence=4, offset=2)
    yaml.dump(all_contrib, file)
"""
This is flipping the order of stuff - not sure why?
bio: Executive Director, pyOpenSci
  board: true
  contributor_type: [leadership, current editor, package-maintainer]
  github_image_id: 7649194
  github_username: lwasser
  mastodon: https://fosstodon.org/@leahawasser
  name: Leah Wasser
  orcidid: 0000-0002-8177-6550
  organization: pyOpenSci
  packages-editor: [errdapy, pandera, nbless]
  packages-reviewed: ['']
  packages-submitted: [earthpy]
  sort: 1
  title: Executive Director
  twitter: leahawasser
  website: https://www.leahwasser.com
"""


# Eventually i think i'll want to write sections in the file in addition to just dumping yaml

## TODO: FUTURE - could use github api to grab twitter and location from profile too??

# ```
# - name: Yuvi Panda
#   advisory: true
#   bio: 'Open Source Infrastructure Engineer'
#   organization: "Project Jupyter"
#   github_username: yuvipanda
#   github_image_id: 30430
#   twitter: 
#   mastodon: https://hachyderm.io/@yuvipanda
#   orcidid: 
#   website: https://words.yuvi.in
#   contributor_type: []
#   packages-submitted: [""]
#   packages-reviewed: [""]
#   `

# turn into pandas DF


# write to yaml file for website?