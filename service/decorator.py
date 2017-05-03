# -*- coding: utf-8 -*-
import os
import base64
import functools
import json
from flask import make_response, jsonify, request, abort
from spider import lib_login
from errors import ForbiddenError


def tojson(f):
    """
    :function: tojson
    :args:
        - f: 被修饰的函数
    :rv: f()
    将视图函数的返回值转化成json的形式
    """
    @functools.wraps(f)
    def decorator(*args, **kwargs):
        rv = f(*args, **kwargs)
        status_or_headers = None
        headers = None
        if isinstance(rv, tuple):
            rv, status_or_headers, headers = rv + (None, ) * (3 - len(rv))
        if isinstance(status_or_headers, (dict, list)):
            headers, status_or_headers = status_or_headers, None

        rv = json.dumps(rv, indent=1, ensure_ascii=False)
        rv = make_response(rv)
        if status_or_headers is not None:
            rv.status_code = status_or_headers
        if headers is not None:
            rv.headers.extend(headers)
        return rv
    return decorator


def require_lib_login(f):
    """
    :function: require_lib_login
    :args:
        -f: 被修饰的函数
    :rv: f()
    需要图书馆登录
    """
    @functools.wraps(f)
    def decorator(*args, **kwargs):
        try:
            # s: 爬虫session对象; sid: 学号
            s, sid = lib_login()
        except ForbiddenError as e:
            return jsonify({}), e.status_code
        else:
            rv = f(s, sid, *args, **kwargs)
            return rv
    return decorator
