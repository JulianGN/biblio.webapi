"""
ASGI config for biblio.webapi project.

It exposes the ASGI callable as a module-level variable named ``application``.
"""

import os
import sys
from pathlib import Path
from django.core.asgi import get_asgi_application

# Aponta para as settings corretas
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

# 🔧 IMPORTANTE no Render (e em qualquer ASGI server): inclui ./src no PYTHONPATH
BASE_DIR = Path(__file__).resolve().parent.parent
SRC_DIR = BASE_DIR / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.append(str(SRC_DIR))

application = get_asgi_application()
