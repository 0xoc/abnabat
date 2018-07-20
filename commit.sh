#!/bin/bash
source .vnev/bin/activate
cp abnabat/settings.py abnabat/settings-sample.py
python manage.py collectstatic
git add -A
git commit -m "$1"
git push
