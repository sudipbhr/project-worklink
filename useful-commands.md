# Setting up project
    ## Cloning project from github
    1. git clone https://github.com/sudipbhr/project-worklink.git
    
    ## create virutal environement
    1. py -m venv venv

    ## activate virtual environment
    1. venv/Scripts/activate
    
    ## installing django
    1. pip install django

    ## installing other packages and modules required
    1. pip install -r requirements.txt

    ## running django project
    1. py manage.py runserver

    ## creating new migrations
    1. py manage.py makemigrations
        ### Note
            makemigrations command is runned when certain changes are make on the models.py file
    2. py manage.py migrate
        ### Note
            migrate command is runned after makemigrations command is runned
