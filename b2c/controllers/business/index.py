# -*- coding:utf8 -*-

from flask import render_template
from flask import request, current_app

from b2c.controllers.business import b_bp
# from . import validate_arg
# from lyra.service import UserService, AlbumService, ScoreService
# from lyra.controllers.web.validators import ShareMp3Input


@b_bp.route('/', methods=['GET'])
def index():
    print(request.args)
    return 'business msg'
