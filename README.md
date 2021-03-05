# webapps
This project is private webapps.



## Install FRPC/FRPS

~~~bash
wget https://github.com/fatedier/frp/releases/download/v0.35.1/frp_0.35.1_linux_amd64.tar.gz 
tar -zxvf frp_0.35.1_linux_amd64.tar.gz 
cp -r frp_0.35.1_linux_amd64 frp
~~~



## Setup virtual env of python

~~~bash
sudo apt update
sudo apt install python3-dev python3-pip python3-venv
python3 -m venv --system-site-packages ./venv
vim ~/.bashrc
alias actpython="source ~/venv/bin/activate"
source ~/.bashrc
~~~

