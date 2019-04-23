import json
import os

import tornado.web


class SwaggerHandler(tornado.web.RequestHandler):
    SWAGGER_URL = "/api/docs"
    API_URL = "https://petstore.swagger.io/v2/swagger.json"
    APP_NAME = "Swagger UI"
    OAUTH_CONFIG = None

    DEFAULT_CONFIG = {
        "app_name": APP_NAME,
        'dom_id': '#swagger-ui',
        'url': API_URL,
        'layout': 'StandaloneLayout'
    }

    def set_default_headers(self):
        headers = ["origin", "x-csrf-token", "content-type", "accept",
                   "x-requested-with"]
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", ", ".join(headers))
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get(self):
        oauth_config_json = SwaggerHandler.OAUTH_CONFIG
        if oauth_config_json:
            oauth_config_json = json.dumps(oauth_config_json)

        fields = {
            'base_url': SwaggerHandler.SWAGGER_URL,
            'app_name': SwaggerHandler.APP_NAME,
            'config_json': json.dumps(SwaggerHandler.DEFAULT_CONFIG),
            'oauth_config_json': oauth_config_json

        }

        self.render("dist/index.html", **fields)


def get_tornado_handler(
    base_url,
    api_url,
    app_name="Swagger UI",
    config=None,
    oauth_config=None
):

    handler = SwaggerHandler
    handler.SWAGGER_URL = base_url
    handler.API_URL = api_url
    handler.APP_NAME = app_name

    if config:
        handler.DEFAULT_CONFIG.update(config)

    dist = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "dist"
    )

    handlers_list = [
        (r"/swagger/dist/(.*)", tornado.web.StaticFileHandler, {"path": dist}),
        (base_url, handler)
    ]

    return handlers_list
