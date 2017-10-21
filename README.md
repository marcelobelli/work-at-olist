# Work at Olist

My solution for the Work at Olist [test](https://github.com/olist/work-at-olist).

The demo is running [here](https://mbelli-wants-to-work-at-olist.herokuapp.com).

## API Documentation

### Listing all channels
##### Endpoint
~~~~
/api/channels/
~~~~
This endpoint will bring all channels in the database.
##### Response
~~~~json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "channel": "Amazon",
            "url": "http://127.0.0.1:8000/api/channels/amazon/"
        },
        {
            "channel": "Submarino",
            "url": "http://127.0.0.1:8000/api/channels/submarino/"
        }
    ]
}
~~~~

### Channel details

##### Endpoint
~~~~
/api/channels/<channel_slug>/
~~~~
This endpoint will bring all categories and subcategories of the channel.
##### Response
~~~~json
{
    "channel": "Ricardo Eletro",
    "categories": [
        {
            "category": "Books",
            "url": "http://127.0.0.1:8000/api/channels/ricardo-eletro/categories/books/"
        },
        {
            "category": "National Literature",
            "url": "http://127.0.0.1:8000/api/channels/ricardo-eletro/categories/books-national-literature/"
        },
        {
            "category": "Science Fiction",
            "url": "http://127.0.0.1:8000/api/channels/ricardo-eletro/categories/books-national-literature-science-fiction/"
        }
    ]
}
~~~~

### Category details

##### Endpoint
~~~~
/api/channels/<channel_slug>/categories/<category_slug>/
~~~~
This endpoint will bring all children and parents of the category.
##### Response
~~~~json
{
    "category": "XBOX 360",
    "children": [
        {
            "category": "Accessories",
            "url": "http://127.0.0.1:8000/api/channels/submarino/categories/games-xbox-360-accessories/",
            "children": []
        },
        {
            "category": "Console",
            "url": "http://127.0.0.1:8000/api/channels/submarino/categories/games-xbox-360-console/",
            "children": []
        },
        {
            "category": "Games",
            "url": "http://127.0.0.1:8000/api/channels/submarino/categories/games-xbox-360-games/",
            "children": []
        }
    ],
    "parent": {
        "category": "Games",
        "url": "http://127.0.0.1:8000/api/channels/submarino/categories/games/",
        "parent": null
    }
}
~~~~

___

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

___

## Running the project

~~~~
$ cp local.env .env
$ python work-at-olist/manage.py migrate
$ python work-at-olist/manage.py runserver
~~~~