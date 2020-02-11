#stop daemon
if git fetch | grep master > /dev/null; then
    #stop daemon
    pkill -f pitemp.py
    echo "pulling `date`" >> fetch.log
    git pull
    bash setup.sh
fi