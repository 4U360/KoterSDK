# KoterSDK
 Koter integration package made to ensure security between the exchange of information between the platform and our customers.
 

## Setup

```shell
git clone git@github.com:4U360/KoterSDK.git
cd <ApplicationDir>
python manage.py migrate

# This start a SDK Local Server
# This is necessary as we will use your Rest API for communication
python manage.py runserver 0.0.0.0:8000
```

## How To Update
```shell
# This command will update your SDK to the latest version, it will run git pull.
# The difference is that it will take into account the repository versioning file.
python manage.py updatesdk
```