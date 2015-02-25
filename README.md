Algorithm Snippets
================

This repository contains various algorithm exercises, some were asked during my interviews:

- Google
- Grist Labs
- The New York Times

##Configuration

###GIT

Fork this project in your GitHub account, then clone your repository:

```
cd /var/
sudo mv www/ _www/
sudo git clone https://[YOUR-USERNAME]@github.com/[YOUR-USERNAME]/machine-learning.git www
```

Then, change the *file permissions* for the entire project by issuing the command:

```
cd /var/
sudo chown -R jeffrey:sudo www
```

**Note:** change 'jeffrey' to the user account YOU use.

Then, add the *Remote Upstream*, this way we can pull any merged pull-requests:

```
cd /var/www/
git remote add upstream https://github.com/[YOUR-USERNAME]/machine-learning.git
```
