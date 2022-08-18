# UI Gateway #

A gateway for the user interface. Not the clearest idea at the moment

## Why a UI Gateway service?

Well, an API Gateway should suffice, in theory. But, nowadays, we end up having a ton of endpoints, the more requests, the more abstracted but the more time and requests the user should process, which may not be the greatest idea, in fact, it isn't.

Creating a UI Gateway that consumes from the API Gateway when needed, even though it shouldn't be it's main flow. Can help.

This UI Gateway, instead of pointing to the API Endpoints, it should, instead, point to the ui/view services, which, inside, will request all the information that may be necessary given a requested endpoint. Thus reducing the request fatigue and obscuring microservices when necessary