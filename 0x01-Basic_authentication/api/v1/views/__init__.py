#!/usr/bin/env python3
""" Blueprint
"""
from flask import Blueprint
from api.v1.views.index
from api.v1.views.users

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

User.load_from_file()
