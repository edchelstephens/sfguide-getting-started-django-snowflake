# Welcome to the Django-Snowflake Quickstart!

## Overview

This repository is intended to be used as you follow along in the official Django-Snowflake Quickstart. As part of the quickstart, you'll:

- Create a database in Snowflake and load data into it
- Connect the Django application in this repo to Snowflake, using the `django-snowflake` backend
- Create models in the Django app to represent the data
- Browse the data as an end user of the app
- Browse the data using Django's admin interface

To get started, navigate to the [Getting Started with Django and Snowflake Quickstart](https://quickstarts.snowflake.com/guide/getting-started-django-snowflake/). Have fun!


## Running Locally
### With Docker Container
1. Build the image
    `sudo docker build -t snowflake-django .`
2. Run the container
    `sudo docker run -p 8000:8000 snowflake-django`

### With Docker Compose
1. Build and run the containters up
    `sudo docker-compose -f local.yml up --build`
