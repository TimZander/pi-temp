export PITEMP_SQLSERVER=
export PITEMP_SQLUSER=
export PITEMP_SQLPASSWORD=
export PITEMP_SQLDB=

python3 -m pip install --upgrade pip
pip install -r requirements.txt

#start daemon
python3 pitemp.py -i 60