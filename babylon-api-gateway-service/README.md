# API Gateway #

Using as reference:

- [Money transfer gateway](https://github.com/cer/event-sourcing-examples/tree/master/java-spring/api-gateway-service)
- [API Gateway](https://microservices.io/patterns/apigateway.html)

## Why not just call the microservices?

For various reasons we may want a single domain to provide all of our endpoints, at least most of them.

It will, in its turn, call the API microservices, and will most likely give a unified response with all that may be needed for that specific request. It's kind of trending, no matter if microservice or monolithic, it's necessary.