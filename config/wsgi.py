"""
WSGI config for biblio.webapi project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os
import sys
from pathlib import Path
from django.core.wsgi import get_wsgi_application

# Aponta para as settings corretas
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

# 🔧 IMPORTANTE no Render: inclui ./src no PYTHONPATH também no WSGI/Gunicorn
BASE_DIR = Path(__file__).resolve().parent.parent  # raiz do projeto (onde está manage.py)
SRC_DIR = BASE_DIR / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.append(str(SRC_DIR))

application = get_wsgi_application()
