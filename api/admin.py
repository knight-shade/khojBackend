from django.contrib import admin

from . import models
# Register your models here.
admin.site.register(models.BookProfile)
admin.site.register(models.BooksIssueReturnHistory)
admin.site.register(models.Employee)
admin.site.register(models.AdminProfile)
admin.site.register(models.BooksCurrentlyIssued)