from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.db.models import Count
from django.core.mail import send_mail
from blogi.models import Post
from taggit.models import Tag