echo 'installing dependencies....'
pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput

echo 'build completed'