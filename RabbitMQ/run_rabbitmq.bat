docker stop myrabbit
docker rm myrabbit
docker run -d --hostname myrabbit --name myrabbit -p 5672:5672 -p 15672:15672 rabbitmq:3-management