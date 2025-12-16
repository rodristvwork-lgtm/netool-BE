## Linux Enviroment

python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

### Optional
python -m pip install --upgrade pip

### Run

python  main.py

### Run with gunicorn
gunicorn --bind 0.0.0.0:5000 main:app

### Port

http://localhost:5000



## Docker

### step 1 - build Image using Dockerfile

docker build -t netool-be-image:1.0 .
    
### step 2 - create container with mounted directory (using this net-performance-collectors directory)

docker run -it --name netool-be-image-container -p 5000:5000 -v "$(Get-Location):/app" netool-be-image:1.0 bash

exit

### step 3 - Contatiner Access and Enviroment 

docker start -ai netool-be-image-container

python -m venv .venv

### Optional

source .venv/bin/activate

python -m pip install --upgrade pip

pip install -r requirements.txt

### step 4 - Run

python main.py

### step 4(Optional) - Run with gunicorn
gunicorn --bind 0.0.0.0:5000 main:app

#### Port
http://localhost:5000