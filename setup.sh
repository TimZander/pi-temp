. ./secrets

python3 -m pip install --upgrade pip
~/.local/bin/pip install -r requirements.txt

#start daemon
python3 src/pitemp.py -i 60