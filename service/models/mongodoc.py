# -*- coding: utf-8 -*-
from mongokit import Document


class Attention(Document):
    """
    :class: Attention
    用户图书关注存储
    """
    __collection__ = 'attentions'
    __database__ = 'attendb'
    structure = {
        'bid': basestring,
        'book': basestring,
        'id': basestring,
        'author': basestring,
        'sid': basestring
    }

    def __repr__(self):
        return '<Mongo Attention>'
