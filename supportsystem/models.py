from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Company(models.Model):
	company = models.CharField(max_length=50)


	def __str__(self):
		return '{}'.format(self.company)

class Role(models.Model):
	role = models.CharField(max_length=20)

	def __str__(self):
		return '{}'.format(self.role)

class ExtendedUserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	role = models.ForeignKey(Role, on_delete=models.CASCADE)
	company = models.ForeignKey(Company, on_delete=models.CASCADE)

	def __str__(self):
		return '{} at {} as {}'.format(self.user.username, self.company, self.role)

class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	posttitle = models.CharField(max_length=50)
	postbody = models.TextField()
	#postmedia = models.ImageField(upload_to = 'uploadedimages/', default = 'uploadedimages/None/no.img.jpg')
	poststatus = models.BooleanField(default=True)
	date_added = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return '<PostID:{}, Posttitle:{}, Status:{}>'.format(self.id, self.posttitle, self.poststatus)

class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments", related_query_name="comment")
	commentbody = models.TextField()
	#commentmedia = models.ImageField(upload_to = 'uploadedimages/', default = 'uploadedimages/None/no.img.jpg')
	date_added = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return '<CommentID:{}, Post:{}>'.format(self.id, self.post)

class Image(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True )
	comment = models.ForeignKey(Comment, on_delete=models.CASCADE, blank=True, null=True)
	image = models.ImageField(upload_to = 'uploadedimages/', default = 'uploadedimages/None/no.img.jpg')

	def __str__(self):
		return '<{}{}{}>'.format(self.image, self.post, self.comment)