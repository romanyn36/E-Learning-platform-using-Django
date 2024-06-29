from django.db import models
import os
# Create your models here.

class SystemAdmin(models.Model):

    # id must be unique 10 digit number
    name = models.CharField(max_length=30,default="System Admin")
    number = models.IntegerField(max_length=10)
    email = models.EmailField(max_length=50)
    address = models.TextField(max_length=50)
    username = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=16)
    def __str__(self):
        return self.name

class Course(models.Model):
    category_choices = [('marketing','marketing'),('programming','Programming'),('web','Web Development'),('app','App Development'),('game','Game Development'),('database','Database Management'),('network','Network Security'),('cloud','Cloud Computing'),('iot','Internet of Things'),('blockchain','Blockchain Technology'),('cyber','Cyber Security'),('vr','Virtual Reality'),('ar','Augmented Reality'),('mr','Mixed Reality'),('robotics','Robotics'),('bigdata','Big Data'),('datascience','Data Science'),('ai','Artificial Intelligence'),('ml','Machine Learning'),('dl','Deep Learning'),('cv','Computer Vision'),('nlp','Natural Language Processing')]
    
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=100)
    category = models.CharField(max_length=20,choices=category_choices)
    description = models.TextField(max_length=500,blank=True)
    is_active = models.BooleanField(default=True)
    image_url = models.ImageField(upload_to='courses/',default='courses/default.jpg',blank=True)
    
    def save(self, *args, **kwargs):
        # Check if a new image was uploaded
        if self.pk:
            try:
                old_course = Course.objects.get(pk=self.pk)
                if old_course.image_url != self.image_url:
                    if old_course.image_url.name != 'courses/default.jpg':
                        # Delete the old image file
                        os.remove(old_course.image_url.path)
            except Course.DoesNotExist:
                pass
        super().save(*args, **kwargs)
    def __str__(self):
        return self.course_name


    
class Student(models.Model):
    # id must be unique 10 digit number
    name = models.CharField(max_length=30,default="Student")
    number = models.IntegerField(max_length=10,blank=True,null=True)
    email = models.EmailField(max_length=50,blank=True)
    address = models.TextField(max_length=50,blank=True)
    username = models.CharField(max_length=20,unique=True,default="student")
    password = models.CharField(max_length=16,blank=True)
    enrolled_courses = models.ManyToManyField(Course,related_name='Student',blank=True)
    def __str__(self):
        return self.name



class CourseRequest(models.Model):
    request_id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,related_name='course_requests')
    student = models.ForeignKey(Student, on_delete=models.CASCADE,related_name='course_requests')
    # make date field takes the current date automatically
    request_date = models.DateField(auto_now=True)
    reason = models.TextField(max_length=500,blank=True)
    status = models.CharField(max_length=20, default="pending")

    # ensure that student can request for a course only once
    class Meta:
        unique_together = ('course', 'student')
    def __str__(self):
        return f"{self.student.name} request for {self.course.course_name}"
    
