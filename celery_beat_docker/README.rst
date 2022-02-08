===============================
Celery + docker-compose example
===============================

This is a simple example, with only one task, and two test to launch the task and see Celery working.
You can use it as a template (flower is not protected).


Install
-------
``$ cd celery_beat_docker``

``$ cp environment.secret.template environment.secret``         and configure

``$ cp environment.secret.template environment.secret.dev``     and configure

``$ make compose-dev     or    make compose-pro`` 

Use
---

Launch:

    ``$ docker-compose up --build``

or to detached mode:

    ``$ docker-compose up --build -d``

With this, you need to launch other command to see logs:

    ``$ docker-compose logs -f``

Flower URL: http://localhost:5555      (If you use virtualbox or other machine, set the correct ip)


Tests
-----

Launch test1:
   

    ``$ make test1``


Launch test2:

    ``$ make test2``

    You can see now logs and flower changes.


Clean data
----------

Finally remove containers and volumes:

    ``$ docker-compose down -v``

    Or

    ``$ docker-compose rm -v``

And rm directory.
