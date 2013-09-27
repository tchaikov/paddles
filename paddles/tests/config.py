from pecan.hooks import TransactionHook, RequestViewerHook
from paddles import models


# Server Specific Configurations
server = {
    'port': '8080',
    'host': '0.0.0.0'
}

address = 'http://localhost:%s' % server['port']

# Pecan Application Configurations
app = {
    'root': 'paddles.controllers.root.RootController',
    'modules': ['paddles'],
    'static_root': '%(confdir)s/../../public',
    'template_path': '%(confdir)s/../templates',
    'debug': True,
    'errors': {
        '404': '/error/404',
        '__force_dict__': True
    }
}


sqlalchemy = {
    'url': 'sqlite://',
    'echo'          : True,
    'echo_pool'     : True,
    'pool_recycle'  : 3600,
    'encoding'      : 'utf-8'
}
