from django.db import models
from django.contrib.auth.models import AbstractUser


class School(models.Model):
    name = models.CharField(max_length=200)
    info = models.TextField()
    foundation_year = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    amount_of_students = models.CharField(max_length=200)
    amount_of_teachers = models.CharField(max_length=200)
    amount_of_floors = models.CharField(max_length=200)

    def get_all_students(self):
        return self.students.all()

    def get_all_teachers(self):
        return self.teachers.all()

    def get_all_forms(self):
        return self.forms.all()

    def __str__(self):
        return f'{self.name}'


class Form(models.Model):
    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        related_name="forms",
    )
    grade = models.CharField(max_length=2)
    letter = models.CharField(max_length=2)
    class_teacher = models.OneToOneField(
        'Teacher',
        blank=False,
        null=False,
        on_delete=models.PROTECT,
        related_name="forms",
    )

    def get_all_students(self):
        return self.students.all()

    def __str__(self):
        return f'{self.grade} {self.letter}  -  {self.school}'


class Teacher(AbstractUser):
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200, blank=False, null=False)
    date_of_birth = models.DateField(null=True, blank=True)
    form = models.OneToOneField(
        Form,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        related_name="teachers",
    )
    school = models.ForeignKey(
        School,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        related_name="teachers",
    )

    # Указываем related_name для groups и user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='teacher_groups',
        blank=True,
        help_text='The groups this teacher belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='teacher_user_permissions',
        blank=True,
        help_text='Specific permissions for this teacher.',
        verbose_name='user permissions',
    )


class Student(AbstractUser):
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    date_of_birth = models.DateField(null=True, blank=True)
    form = models.ForeignKey(
        Form,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        related_name="students",
    )
    school = models.ForeignKey(
        School,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        related_name="students",
    )

    # Указываем related_name для groups и user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='student_groups',
        blank=True,
        help_text='The groups this student belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='student_user_permissions',
        blank=True,
        help_text='Specific permissions for this student.',
        verbose_name='user permissions',
    )
