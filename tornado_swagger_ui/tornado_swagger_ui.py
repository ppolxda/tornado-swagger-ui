import json
import os
import sys

import tornado.web


class SwaggerHandler(tornado.web.RequestHandler):

    def initialize(self, path, base_url, app_name, api_url):
        self.index = path + "/index.html"

        self.base_url = base_url
        self.api_url = api_url
        self.app_name = app_name

        self.oauth_config = None

        self.default_config = {
            "app_name": self.app_name,
            'dom_id': '#swagger-ui',
            'url': self.api_url,
            'layout': 'StandaloneLayout'
        }

    def set_default_headers(self):
        headers = ["origin", "x-csrf-token", "content-type", "accept",
                   "x-requested-with"]
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", ", ".join(headers))
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get(self):
        oauth_config_json = self.oauth_config
        if oauth_config_json:
            oauth_config_json = json.dumps(oauth_config_json)

        fields = {
            'base_url': self.base_url,
            'app_name': self.app_name,
            'config_json': json.dumps(self.default_config),
            'oauth_config_json': oauth_config_json

        }

        self.render(self.index, **fields)


def get_tornado_handler(
    base_url,
    api_url,
    app_name="Swagger UI",
    config=None,
    oauth_config=None
):

    module_path = sys.modules.get("tornado_swagger_ui")
    dist = os.path.join(
        os.path.dirname(os.path.abspath(module_path.__file__)),
        "assets"
    )

    handlers_list = [
        (r"/swagger/dist/(.*)", tornado.web.StaticFileHandler, {"path": dist}),
        (
            base_url,
            SwaggerHandler,
            {
                "path": dist,
                "base_url": base_url,
                "app_name": app_name,
                "api_url": api_url
            }
        )
    ]

    return handlers_list
