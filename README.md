Objective
==========
I am trying to create a token based REST API backend service to store links and a description about it. These links can point to anything that helped you learn or something that you want to keep to yourself. You can categorize or tag them so it helps in easy retrieval. The back end is developed using Django and Django Rest Framework. In parallel, I am developing a user interface/client application using React/Redux.

Uses
====
* Python3.6.3.
* Django2.0.5.
* Django Rest Framework.
* django-rest-auth
* django-allauth
* JWT.

Dependencies to run
===================
* docker
* docker-compose

Usage
=====
```
cd bookmarky
docker-compose up --build

# register and get a token.
curl -d '{"username": "jay", "email": "jay@example.com", "password1": "a-strong-password", "password2": "a-strong-password"}' -H 'Content-Type: application/json' http://localhost:8000/api/v1.0/auth/registration/

# create your bookmarks by POSTing to bookmarks API.
curl -H 'Authorization: JWT <your-token-goes-here>' -H 'Content-Type: application/json' -d '{"title": "Google", "link": "https://google.com", "tags": ["search engine", "web"]}' http://localhost:8000/api/v1.0/my/bookmarks/

# ping boomarks API to retrieve your bookmarked links.
curl -H 'Authorization: JWT <your-token-goes-here>' http://localhost:8000/api/v1.0/my/bookmarks/

# login and get a new token.
curl -d '{email": "jay@example.com", "password": "a-strong-password"}' -H 'Content-Type: application/json' http://localhost:8000/api/v1.0/auth/login/
```
