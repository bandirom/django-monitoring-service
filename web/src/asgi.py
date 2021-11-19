import os

from django.core.asgi import get_asgi_application
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')
django_asgi_app = get_asgi_application()

"""Imports only after get_asgi_application() and env.
Excluded error like:
django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.
"""

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import OriginValidator
# from sockets.routing import websocket_urlpatterns as chart_urlpatterns

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    'websocket': AuthMiddlewareStack(
        URLRouter(
            [],
        )
    ),
})
