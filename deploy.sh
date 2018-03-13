#! usr/bin/env bash
git add -f .secrets && eb deploy --staged --profile=eb && git reset HEAD .secrets

ENV $containerid  sudo docker ps -q

sudo docker exec -it $containerid  python srv/project/app/manage.py migrate