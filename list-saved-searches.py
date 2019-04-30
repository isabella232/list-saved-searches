import requests, json, argparse
from tabulate import tabulate

parser = argparse.ArgumentParser()
parser.add_argument("url")
parser.add_argument("token")
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
      usernameToSavedSearchCount.append([n['username'], len(s['search.savedQueries'])])

orgNodes = responseJSON['data']['organizations']['nodes']
orgNamesToSavedSearchCount = []
for o in orgNodes:
  settings = o['configurationCascade']['merged']['contents']
  if (settings):
    s = json.loads(settings)
    if (s['search.savedQueries']):
      orgNamesToSavedSearchCount.append([o['name'], len(s['search.savedQueries'])])

print(tabulate(usernameToSavedSearchCount, headers=["Username", "# saved searches"]))
print('\n')
print(tabulate(orgNamesToSavedSearchCount, headers=["Org name", "# saved searches"]))