import re,sys,git

#Arguement passed in
hub_repo =  str(sys.argv[1]) #'/Users/adamminton/Documents/GitHub/hub/'
commit_arg = str(sys.argv[2]) #'Master'
#branch = str(sys.argv[3]) #'main'
branch = 'main'

#Determine latest commit on hub branch
repo = git.Repo(hub_repo)
repo.git.checkout(branch)
hub_sha = repo.head.object.hexsha

#Determine which Commit SHA to use
if commit_arg == 'Master':
    commit = hub_sha
else:
    commit = commit_arg

#Location of Manifest File
filepath = './manifest.lkml'

#Construct text to replace with
replace = 'ref: "'+ commit +'"'

#Open Manifest File
with open(filepath) as f:
    s = f.read()

#Search with regex to find the ref 
search = re.search(r"ref: \"(\w*)\"",s)

#Return the result of regex
find = search.group()

#Replace the string
s = s.replace(find, replace)

#Write back manifest file with new code
with open(filepath, "w") as f:
    f.write(s)
