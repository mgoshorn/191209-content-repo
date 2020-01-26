#

## Install Conda:
*`wget https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh`
*`sh Anaconda3~`

## Install git
* `sudo apt install git`

## Pull Git Repo
* `git clone repo-url`
* Login if necessary

## Configure Environment
### Anaconda
* Export an environment configuration and import in the cloud environment
* OR Manually install dependencies using `conda install x`
### Pip
* Create a file that enumerates dependencies (dependency per line)
* `pip install -r file-name.txt`

## Starting Server

* `gunicorn -b 0.0.0.0:PORT app:app`
* Format: `gunicorn -b <ip:port> <app-file>:<app-object>`

* Note: You may want to use screen or nohup to run it in a detached fashion.

## GCP configuration:
* Create a compute instance - Recommend F1-Micro generally, though you may want to use something a bit larger during the presentation, as one of your classmates may try to crash it.

* Firewall configuration is accessible from the compute instance's drop down menu (... menu) > View Network Details
1. (Left Aside Menu) > Firewall Rules
2. Create Firewall Rule
* Provide name. (Arbitrary)
* Assign target (ie. All instances in the network)
* Set IP Range. 0.0.0.0/0 - CIDR block
* Allow TCP [Your Port]

