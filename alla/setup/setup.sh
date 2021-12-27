python manage.py makemigrations
python manage.py migrate
cp alla/setup/set.py set.py
python set.py $1
rm alla/readme.md
rm -rf alla/setup/