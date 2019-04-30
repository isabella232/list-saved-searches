A short script to list the number of saved searches associated with users and organizations on a Sourcegraph instance.

To run:

1. Clone this repository and `cd` into it.
1. Run `pipenv install`
1. Run `pipenv run python get-saved-search-owners.py https://$YOUR_SOURCEGRAPH_INSTANCE_URL $YOUR_SITE_ADMIN_ACCESS_TOKEN`. You can create an access token at https://$YOUR_SOURCEGRAPH_INSTANCE_URL/users/$USERNAME/settings/tokens. The user associated with the token should be a site admin of the Sourcegraph instance you are querying.

Running the script will output the number of saved searches associated with each user and org like so:

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