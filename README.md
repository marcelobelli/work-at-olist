# Work at Olist

My solution for the Work at Olist test.

## Creating the local environment

For this to work you'll need:

- git
- Python 3.6
- docker (go to [docker.io](https://docker.io) for instructions)
- docker-compose (`pip install docker-compose`)

### Clone the Git Repository

Download the code repository:

    mkdir -p ~/projects/
    cd ~/projects/
    git clone git@github.com:marcelobelli/work-at-olist.git
    cd work-at-olist

### Create virtualenv and Install Dependencies

    mkvirtualenv --python=$(which python3.6) --no-site-packages work-at-olist
    workon work-at-olist # requires virtualenvwrapper
    pip install -r requirements/local.txt

### Run Service Containers

For the first time, to run all needed services as background containers, execute:

    docker-compose --file=composer-dev.yml --project-name=work-at-olist up -d
    
After that, you can run the container with the command:

    docker-compose -f composer-dev.yml -p work-at-olist start

The services will have fixed ports exported on host machine:
- PostgreSQL will be running on port `32007`

#### Other Container Commands

You can list the containers' statuses:

    docker-compose -f composer-dev.yml -p work-at-olist ps

Stop them:

    docker-compose -f composer-dev.yml -p work-at-olist stop

Remove them completely:

    docker-compose -f composer-dev.yml -p work-at-olist rm

