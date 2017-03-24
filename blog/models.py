
# Create your models here.
from django.db import models
from django.utils import timezone

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(
		default=timezone.now)
	published_date =models.DateTimeField(
		blank=True, null=True)
	likes = 0
	def publish(self):
		self.published_date = timezone.now()
		self.save()
	def likes_add(self,):
		self.likes +=1
		
	def __str__(self):
		return self.title
class Comment(models.Model):
	post = models.ForeignKey('blog.Post', related_name='comments')
	author = models.CharField(max_length=200)
	text = models.TextField()
	created_comment = models.BooleanField(default=False)
#	created_date = models.DateTimeField( default=timezone.now)
	def approve(self):
		self.approved_comment = True
		self.save()
	def __str__(self):
		return self.text

class Eintrag(models.Model):
	
	titel = models.CharField(max_length=50)
	betriebsstelle = models.CharField(max_length=200)
	lsz = models.CharField(max_length=200)
	ordnr = models.CharField(max_length=200)
	nkz = models.CharField(max_length=200)
	datum = models.DateTimeField(default=timezone.now)
	def veröffentlichen(self):
		self.datum = timezone.now()
		self.save()
	def __str__(self):
		return self.titel
	
