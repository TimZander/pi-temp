#stop daemon
git fetch
if [ `git rev-parse HEAD` != `git rev-parse @{u}` ]; then
    #stop daemon
    pkill -f pitemp.py
    echo "pulling `date`" >> fetch.log
    git reset --hard origin/master
    bash setup.sh
fi