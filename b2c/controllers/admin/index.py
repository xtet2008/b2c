# -*- coding:utf8 -*-

from flask import render_template
from flask import request, current_app

from b2c.controllers.admin import a_bp
# from . import validate_arg
# from lyra.service import UserService, AlbumService, ScoreService
# from lyra.controllers.web.validators import ShareMp3Input
#


@a_bp.route('/', methods=['GET', 'POST'])
def index():
    print('get:', request.args)
    print('post:', request.form)
    print('json:', request.json)
    print('headers:',request.headers)
    return 'admin manage msg'
