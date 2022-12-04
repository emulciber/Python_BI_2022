# How to launch ultraviolence.py         
         
## Information about software environment       
          
OS: Ubuntu 20.04.5 LTS    
Python: Python 3.11.0rc2   


## Installation python, venv and dependencies instructions for launching ultraviolence.py     
       
### Python v3.11 installation     
     
Install a package to add new repositories:
~~~
sudo apt install software-properties-common -y
~~~

Add a repository for python installation:
~~~
sudo add-apt-repository ppa:deadsnakes/ppa
~~~

Install python 3.11 and python3.11-venv (package for creating virtual environments with python) to your system:   
*(while python3.11 is unstable, this version of python will be available on "python3.11", but it won't changed python version on "python" or "python3")*
~~~
sudo apt-get install python3.11 python3.11-venv
~~~

If you haven't already done so, go to folder with ultraviolence.py (download it from this repository):
~~~
cd <PATH_TO_FOLDER_WITH_ULTRAVIOLENCE>
~~~

Create a virtual environment for isolate installing dependencies:
*(instead of "py11uv" here and below it can be your own name of virtual environment)*
~~~
python3.11 -m venv py11uv
~~~

Activate the virtual environment:
~~~
source py11uv/bin/activate
~~~

Install required packages from requirements.txt:
~~~
pip install -r requirements.txt
~~~
or do it manually:
~~~
pip install beautifulsoup4 biopython lxml pandas==1.4
~~~

Create empty files to import it in ultraviolence.py as modules:      
*(This step is suitable to run ultraviolence.py in venv due to the way it is written and to minimize the number of dependencies, but it is not recommended to do this logic with other projects. As an alternative you can try to install some of this packages legally with "pip install", but it won't work with all packages.)*
~~~
touch google.py
touch aiohttp.py
touch requests.py
touch cv2.py
~~~

Launch ultraviolence.py:
~~~
python ultraviolence.py
~~~

**It's done! You're amazing!**

## To whom it may concern:

Some errors (like "match-case" syntax and "except*" syntax for exception errors handling) solved by installing newer version of python (python 3.10 for "match-case" and python 3.11 for "except*"). 
"Match-case" syntax was added in 3.10 python but also available from PyPMatch library.      

Conda do not support unstable and recent versions so installing python 3.11 with conda didn't work out.
~~~
conda create -n py11_uv python==3.11   
> PackagesNotFoundError: The following packages are not available from current channels:
>
> - python==3.11
~~~

Installing python locally also didn't work with following pipeline (error with using pip install):
~~~
wget https://www.python.org/ftp/python/3.11.0/Python-3.11.0rc2.tgz  
tar -zxvf Python-3.11.0rc2.tgz 
cd Python-3.11.0rc2
mkdir .localpython
./configure --prefix=/home/emulciber/IB/python/Python_BI_2022/homework_3_modules/ultraviolence/Python-3.11.0rc2/.localpython   
make    
make install   
Python-3.11.0rc2/.localpython/bin/python3 -m venv py11_venv     
source py11_venv/bin/activate  
pip install bs4      
> Could not fetch URL https://pypi.org/simple/pip/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host='pypi.org', port=443): Max retries exceeded with url: /simple/pip/ (Caused by SSLError("Can't connect to HTTPS URL because the SSL module is not available.")) - skipping
~~~

Modifying "pip.conf" and installing packages with --trusted-host argument like `pip install --trusted-host pypi.python.org beautifulsoup4` also didn't work.

Syntax error with using set as index in dictionary solved by installing pandas with version <1.5 (pandas==1.4 in instruction).