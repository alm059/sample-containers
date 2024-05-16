This sample project consists of the following services deployed in individual containers through docker-compose:


· A load tester through cronjobs
· NGINX ingress
· Grafana
· Gunicorn (Flask)
· Redis Cache
· Mongo DB


It's purpose is to demonstrate the deployment of an API serviced with an NGINX ingress that communicates with mongo DB and a redis cache. This NGINX ingress shows access logs in grafana. Separately, a cronjob runs every 5 minutes a load test against the NGINX ingress. All these services are deployed in separate containers in a docker environment set up through docker-compose.

The project will be oriented to keeping book details.

Implement an API (Gunicorn + Flask) that talks to a mongo DB and has a redis cache, which is serviced with a nginx ingress that shows access logs in grafana, and has a cronjob that runs every 5 minutes a 5 minute load test against the nginx ingress.

SocketIO?