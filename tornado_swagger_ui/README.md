# tornado-swagger-ui

Simple Tornado Handler for adding [Swagger UI](https://github.com/swagger-api/swagger-ui) to your tornado application.

Included Swagger UI version: 3.22.1.

## Installation

`pip install git+https://gitlab.com/api-projects-boilerplates/tornado-swagger-ui.git`

## Usage

Example application:

```python
import tornado.ioloop
import tornado.web
from tornado_swagger_ui import get_tornado_handler

SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
# Our API url (can of course be a local resource)
API_URL = 'http://petstore.swagger.io/v2/swagger.json'

# Call factory function to create our blueprint
swagger_handlers = get_tornado_handler(
    base_url=SWAGGER_URL,
    api_url=API_URL,
    config={
        "app_name": "Test application"
    },
    # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
    #    'clientId': "your-client-id",
    #    'clientSecret': "your-client-secret-if-required",
    #    'realm': "your-realms",
    #    'appName': "your-app-name",
    #    'scopeSeparator': " ",
    #    'additionalQueryStringParams': {'test': "hello"}
    # }
)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.finish("Tornado Swagger UI")

handlers = [
    (r"/", IndexHandler)
]

handlers.extend(swagger_handlers)

def make_app():
    return tornado.web.Application(handlers)


if __name__ == "__main__":
    app = make_app()
    app.listen(5000)
    tornado.ioloop.IOLoop.current().start()

# Now point your browser to localhost:5000/api/docs/

```

## Configuration

The handler supports overloading all Swagger UI configuration options that can be JSON serialized.
See https://github.com/swagger-api/swagger-ui#parameters for options.

Plugins and function parameters are not supported at this time.

OAuth2 parameters can be found at https://github.com/swagger-api/swagger-ui#oauth2-configuration .

## 

Based on the package:

* https://github.com/sveint/flask-swagger-ui