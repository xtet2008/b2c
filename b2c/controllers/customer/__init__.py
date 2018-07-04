# -*- coding:utf8 -*-

from flask import Blueprint
# from b2c.core.log import get_logger

c_bp = Blueprint('c', __name__)

# logger = get_logger()

#
# def validate_arg(validator):
#     def deco(f):
#         @wraps(f)
#         def _(*args, **kwargs):
#             input = validator(request)
#             if not input.validate():
#                 abort(403)
#             resp = f(*args, **kwargs)
#             return resp
#
#         return _
#
#     return deco


from . import index