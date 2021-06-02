import re,sys,git

#Arguement passed in
hub_repo_path = './hub'
spoke_repo_path = './spoke' 
commit_arg = str(sys.argv[1]) #'main'
branch = 'main'

#Determine latest commit on hub branch
repo = git.Repo(hub_repo_path)
repo.git.checkout(branch)
hub_sha = repo.head.object.hexsha

#Determine which Commit SHA to use
if commit_arg == 'main':
    commit = hub_sha
else:
    commit = commit_arg

#Location of Manifest File
manifest_path = spoke_repo_path + '/manifest.lkml'
manifest_lock_path = spoke_repo_path + '/manifest_lock.lkml'

#Construct text to replace with
replace = 'ref: "'+ commit +'"'

#Open Manifest File
with open(manifest_path) as f:
    s = f.read()

#Search with regex to find the ref 
search = re.search(r"ref: \"(\w*)\"",s)

#Return the result of regex
find = search.group()

#Replace the string
s = s.replace(find, replace)

#Write back manifest file with new code
with open(manifest_path, "w") as f:
    f.write(s)

#Open Manifest Lock File
with open(manifest_lock_path) as f:
    s = f.read()

#Search with regex to find the ref 
search = re.search(r"ref: \"(\w*)\"",s)

#Return the result of regex
find = search.group()

#Replace the string
s = s.replace(find, replace)

#Write back manifest file with new code
with open(manifest_lock_path, "w") as f:
    f.write(s)
