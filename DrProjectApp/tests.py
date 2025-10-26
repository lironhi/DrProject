from django import urls
from django.db.models.fields import AutoField
from django.test import TestCase,SimpleTestCase
from django.urls import resolve, reverse
from DrProjectApp.views import *
from DrProjectApp.models import *
import unittest

# Create your tests here.


class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url = reverse('home')
        url1 = reverse('login')
        url2= reverse('newanalyze')
        url3 = reverse('searchpatient')
        print(resolve(url))
        print(resolve(url1))
        print(resolve(url2))
        print(resolve(url3))


class workerstest(TestCase):

    def test_user(self):
       item=doctor_identification()
       item.id=1
       item.login='regham1'
       item.idnumber='123456789'
       item.password='123456'
       item.type='DR'
       item.save()
       record= doctor_identification.objects.get()
       print("OK")
       self.assertEqual(record,item)