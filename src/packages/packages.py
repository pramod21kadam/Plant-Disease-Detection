from flask import Flask, redirect, render_template, request, jsonify, session
from jsonschema import Draft7Validator
from flask.views import MethodView
import json