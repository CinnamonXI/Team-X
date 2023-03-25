# GOL S4 - Team X

## Problem Statement
Access to healthcare information and support is limited, particularly for people with different health conditions. Existing healthcare services are often costly and not easily accessible, and there is a lack of community support and information-sharing among people with similar health conditions. This creates a significant burden for patients and their families, leading to a lack of knowledge and understanding about health conditions and treatments, and increased isolation.

## Proposed Solution
To address the problem of access to primary healthcare, we propose building a health forum website that provides a platform for people to connect, share information, and support each other. The health forum will be designed to cater to people with different health conditions and will offer a range of features such as discussion boards, user profiles, search functionality, notifications, moderation tools, resource library, private messaging, multi-language support, and accessibility features. The website will be user-friendly, visually appealing, and accessible to users of all levels of technical skill and abilities. By creating a community of people with shared experiences, the health forum will help to reduce the burden of health conditions, improve access to healthcare information and support, and increase social connections and well-being. 

## Table of Content
1. [How to install and run the project](#1-how-to-install-and-run-the-project)
2. [How to use the project](#2-how-to-use-the-project)
3. [Team Members](#3-team)

## 1. How to install and run the project

First clone our project if you wish to run it remotely, and to achieve that change directory to location where you would like it installed e.g. to install it to Desktop and you are in the root directory run `cd Users\<user_name>\Desktop`. Once in the desired folder run `git clone https://github.com/smartjef/vsmatt.git` 

**Note:** You need to have git installed in your machine to use git commands. If you dont kindly visit [https://git-scm.com/downloads](https://git-scm.com/downloads) to download and install

Once you have the project cloned, you can cd into it by running command `cd vsmatt` then create a virtualenvironment by running either `python -m venv <environment_name>` or `virtualenv <environment_name>` and activate the environment.

To activate environment run `<environment_name>\Scripts\activate` on windows or `source <environment_name>/bin/activate` on Linux systems. Once your environment is active run `pip install -r requirements.txt` to install requirements for this application.

## 2. How to use the project
You have installed the requirements, what next? Our next step is to makemigration and migration to create the required tables in our database. To achive that run `python manage.py makemigrations` followed by `python manage.py migrate`.

We will need a superuser account for some operations such as approving businesses and for that run `python manage.py createsuperuser` and fill in the required information to create one.

Upto this point you are good to run the application. By default the application will run on port 8000 when command `python manage.py runserver` is executed. And sumple of how the output should be is as below.

```bash
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
November 13, 2022 - 13:19:41
Django version 4.0.8, using settings 'vsmatt.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
You can change the port is there is an application already using that port by passing port number as an argument e.g. `python manage.py runserver 80` to start the server at port 80 or you can provide your desired ip address and port number e.g. `python manage.py runserver 192.168.10.1:80`.

Assuming you are using the default visit [127.0.0.1:8000](http://127.0.0.1:8000) to view the application. You can add businesses and product and you can as well login to admin pannel to approve them [127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)


## 3. Team
The application was designed and build by:

    +-------------------+------------------------------+
    |       Name        |       Github account         |
    +-------------------+------------------------------+
    | 1. Jeff Odhiambo  | https://github.com/smartjef  |
    +-------------------+------------------------------+
    | 2. Laurent Ouma   | https://github.com/Omoshlawi |
    +-------------------+------------------------------+