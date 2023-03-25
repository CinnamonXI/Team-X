# GOL S4 - Team X

## Problem Statement
Access to healthcare information and support is limited, particularly for people with different health conditions. Existing healthcare services are often costly and not easily accessible, and there is a lack of community support and information-sharing among people with similar health conditions. This creates a significant burden for patients and their families, leading to a lack of knowledge and understanding about health conditions and treatments, and increased isolation.

## Proposed Solution
To address the problem of access to primary healthcare, we propose building a health forum website that provides a platform for people to connect, share information, and support each other. The health forum will be designed to cater to people with different health conditions and will offer a range of features such as discussion boards, user profiles, search functionality, notifications, moderation tools, resource library, private messaging, multi-language support, and accessibility features. The website will be user-friendly, visually appealing, and accessible to users of all levels of technical skill and abilities. By creating a community of people with shared experiences, the health forum will help to reduce the burden of health conditions, improve access to healthcare information and support, and increase social connections and well-being. 

## Table of Content
1. [How to install and run the project](#1-how-to-install-and-run-the-project)
2. [Team Members](#3-team)
3. [Pages that Requires Content](#4-pages-that-requires-content)

## 1. How to install and run the project

To set up the project, you will need to have python and git installed on your computer. You can download python from https://www.python.org/downloads/ and git from https://git-scm.com/downloads.
1. Clone the repository by typing in the following command in your terminal:
```bash
git clone https://github.com/CinnamonXI/Team-X.git
```
2. Change directory into the project folder by typing in the following command in your terminal:
```bash
cd Team-X/
```
3. Assuming you have python,pip and virtualenv installed ,you will have to create a virtual environment. To do this, open your terminal and type in the following command:
```bash
virtualenv venv
``` 
or
```bash
python -m venv venv
```
or
```bash
python3 -m venv venv
```
4. Once you have created the virtual environment, you will have to activate it. To do this, type in the following command:
For Linux and Mac:
```bash
source venv/bin/activate
```
For Windows:
```bash
venv\Scripts\activate
```
5. Once you have activated the virtual environment, you will have to install the requirements. To do this, type in the following command:
```bash
pip install -r requirements.txt
```
6. Once you have installed requirements, you may run the server. To do this, type in the following command:
```bash
python manage.py runserver
```
- If you want to run the server on a different port, you can do so by typing in the following command:
```bash
python manage.py runserver <port number>
``` 
e.g
```bash
python manage.py runserver 7000
```
- If you want to run the server on a different ip address, you can do so by typing in the following command:
```bash
python manage.py runserver <ip address>:<port number>
```
e.g
```bash
python manage.py runserver 192.168.100.1:8000
```
To confirm, you'll see a similar output to the following:
```bash
System check identified no issues (0 silenced).
March 25, 2023 - 07:40:18
Django version 4.1.7, using settings 'portfolio.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

7. You can now view site at http://127.0.0.1:8000/mlsa/ or login to the admin panel by going to http://127.0.0.1:8000/admin/ and logging in with the superuser credentials.

username: admin
password: 1234

## Sample Images

### Home Page

### Admin Panel

### Resouce Library

#### Articles

#### Documents

#### Videos



Reach out to us if you have any questions or suggestions +254795067776. Thanks for reading.

## 3. Team
The application was designed and build by `Team X`:

| Name | Role |
| --- | --- |
| Lateefah Belal | Team Lead |
| Jeff Odhiambo | Backend Lead |
| Miriam Adhiambo | Frontend Lead |
| Miriam Mildren | Frontend |
| - | Content Creation |

## 4. Pages that Requires Content
1. Homepage
2. About Page
3. Contact Page
4. Privacy Policy Page
5. Terms of Service Page
6. FAQ Page
7. Resource Library Page
    <!-- Todo list -->
    - [] we need to add more articles, documents and videos
8. Team X - Blog Page
    - [] we need to add more articles