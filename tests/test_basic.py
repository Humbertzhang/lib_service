# -*- coding: utf-8 -*-
import os
import json
import unittest
from base64 import b64encode
from service import create_app
from service.models import Attention


class APITestCase(unittest.TestCase):
    sid = os.environ.get('SID')
    passwd = os.environ.get('PASSWD')
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.app_context.pop()

    def get_api_headers(self, sid, password):
        return {
            'Authorization': 'Basic ' + b64encode(
                (sid + ':' + password).encode('utf-8')).decode('utf-8'),
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

    def test_404(self):
        response = self.client.get(
                '/wrong/url',
                headers=self.get_api_headers('sid', 'passwd')
                )
        self.assertTrue(response.status_code == 404)

    def test_login(self):
        response = self.client.get(
                '/api/lib/login/',
                headers=self.get_api_headers(self.sid, self.passwd)
                )
        self.assertTrue(response.status_code == 200)

    def test_search_books(self):
        response = self.client.get(
                '/api/lib/search/?keyword=平凡的世界/'
                )
        self.assertTrue(response.status_code == 200)

    def test_book_detail(self):
        response = self.client.get(
                '/api/lib/?id=0001148463'
                )
        self.assertTrue(response.status_code == 200)

    def test_book_me(self):
        response = self.client.get(
                '/api/lib/me/',
                headers=self.get_api_headers(self.sid, self.passwd)
                )
        self.assertTrue(response.status_code == 200)

    def test_renew_book(self):
        response = self.client.post(
                '/api/lib/renew/',
                headers = self.get_api_headers(self.sid, self.sid),
                data = json.dumps({
                    'bar_code' : 'T112141974',
                    'check' : 'FAE793CE'
                    })
                )
        self.assertTrue(response.status_code in [200, 400, 403, 406])

    def test_create_atten(self):
        response = self.client.post(
                '/api/lib/create_atten/',
                headers = self.get_api_headers(self.sid, self.passwd),
                data = json.dumps({
                    "bid": "fff",
                    "book": "平凡的世界",
                    "id": "0001148463",
                    "author": "路遥著"
                    })
                )
        self.assertTrue(response.status_code in [201, 409])

    def test_get_atten(self):
        response = self.client.get(
                '/api/lib/get_atten/',
                headers = self.get_api_headers(self.sid, self.passwd)
                )
        self.assertTrue(response.status_code in [200, 404])

    def test_del_atten(self):
        response = self.client.delete(
                '/api/lib/del_atten/',
                headers = self.get_api_headers(self.sid, self.passwd),
                data = json.dumps({
                    "id": "0001148463",
                    })
                )
        self.assertTrue(response.status_code in [200, 404])
