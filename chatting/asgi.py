"""
ASGI config for chatting project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
from channels.auth import AuthMiddlewareStack
#from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import app1.routing
#from channels.asgi import get_channel_layer
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatting.settings')

#channel_layer=get_channel_layer()

application = ProtocolTypeRouter({
  #"http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
        URLRouter(
            app1.routing.websocket_urlpatterns
        )
    ),
})
