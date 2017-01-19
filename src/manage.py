#!/usr/bin/env python
import os
import sys
from web.urls import Urls

if __name__ == "__main__":
    # local por default

    url = Urls()
    url.setup_urls()

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.test")

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
