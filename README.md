A short script to list users and organizations that have saved searches, and the number of saved searches associated with each user or org.

**Note**: This script works for Sourcegraph instances before version 3.0.0.

To run:

1. Clone this repository and `cd` into it.
1. Run `pipenv install`
1. Create a Sourcegraph access token at https://$YOUR_SOURCEGRAPH_INSTANCE_URL/users/$USERNAME/settings/tokens. The user associated with the token should be a site admin of the Sourcegraph instance you are querying.
1. Run `pipenv run python get-saved-search-owners.py https://$YOUR_SOURCEGRAPH_INSTANCE_URL $YOUR_SITE_ADMIN_ACCESS_TOKEN`.

Running the script will output the users and organizations that have saved searches associated with them, and the number of saved searches associated with each:

```
Username      # saved searches
----------  ------------------
beyang                       2
ryan                         1
sqs                          2
felix                        1
keegan                       1
ijt                          1


Org name                      # saved searches
--------------------------  ------------------
Sourcegraph                                  1
```
