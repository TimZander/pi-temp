#stop daemon
if git fetch | grep master > /dev/null; then
    #stop daemon
    pkill -f pitemp.py
    git pull
    bash setup.sh
fi