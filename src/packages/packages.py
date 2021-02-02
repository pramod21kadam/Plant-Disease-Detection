from flask import Flask, redirect, render_template, request, jsonify, session, make_response, url_for
from flask.views import MethodView
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from jsonschema import Draft7Validator
from sqlalchemy import exc
from sqlalchemy.sql import func, and_, or_
from datetime import datetime, timedelta
from functools import wraps
import json
import jwt
import os