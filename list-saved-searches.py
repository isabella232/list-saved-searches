import requests, json, argparse
from tabulate import tabulate

parser = argparse.ArgumentParser()
parser.add_argument("url")
parser.add_argument("token")
parser.add_argument("--multiple", action='store_true')
args = parser.parse_args()

r = requests.post(args.url + '/.api/graphql', json={'query':
"""query{
  users {
    nodes {
      username
      configurationCascade {
        merged {
          contents
        }
      }
    }
  }
  organizations{
    nodes {
      name
      members{
        nodes {
          username
        }
      }
      configurationCascade {
        merged {
          contents
        }
      }
    }
  }
}"""}, headers={"Authorization": "token " + args.token})

responseJSON = r.json()

userNodes = responseJSON['data']['users']['nodes']
usernameToSavedSearchCount = []
for n in userNodes:
  settings = n['configurationCascade']['merged']['contents']
  if (settings):
    s = json.loads(settings)
    if (s['search.savedQueries']):
      numQueries = len(s['search.savedQueries'])
      if ((args.multiple == True and numQueries > 1) or args.multiple == False):
        usernameToSavedSearchCount.append([n['username'], numQueries])

orgNodes = responseJSON['data']['organizations']['nodes']
orgNamesToSavedSearchCount = []
for o in orgNodes:
  settings = o['configurationCascade']['merged']['contents']
  if (settings):
    s = json.loads(settings)
    if (s['search.savedQueries']):
      numQueries = len(s['search.savedQueries'])
      if ((args.multiple == True and numQueries > 1) or args.multiple == False):
        orgNamesToSavedSearchCount.append([o['name'], numQueries])

print(tabulate(usernameToSavedSearchCount, headers=["Username", "# saved searches"]))
print('\n')
print(tabulate(orgNamesToSavedSearchCount, headers=["Org name", "# saved searches"]))