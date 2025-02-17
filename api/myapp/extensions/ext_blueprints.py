from configs import dify_config
from dify_app import DifyApp


def init_app(app: DifyApp):
    
    from flask_cors import CORS  # type: ignore