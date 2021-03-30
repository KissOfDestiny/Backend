from django.test import TestCase

# Create your tests here.
from news.models import *

Post.objects.create(title='title1_title', text='text1_text')
Post.objects.create(title='Bad_word', text='text text bad_word text')
Post.objects.create(title='title3_title', text='text3_text')