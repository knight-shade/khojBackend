from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.


class LibraryAdminManager(BaseUserManager):
    """Helps Django work with our custom admin model"""

    def create_user(self, employee_code, name, password):
        """Create a new user's profile."""
        if not employee_code:
            raise ValueError("Users must provide a Employee code.")
        if not name:
            raise ValueError("Users must provide a valid Name.")
        if not password:
            raise ValueError("Users must provide a valid password.")

        employee_code = self.normalize_email(employee_code)
        user = self.model(employee_code=employee_code, name=name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, employee_code, name, password):
        """Creates a new library admin profile."""

        admin = self.create_user(employee_code, name, password)
        admin.is_superuser = True
        admin.is_staff = True
        admin.save(using=self._db)

        return admin


class AdminProfile(AbstractBaseUser, PermissionsMixin):
    """Represents a library admin inside the system."""

    employee_code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=255)

    # Required fields when making our custom user model.
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    # User to manager admin's profile
    objects = LibraryAdminManager()

    # Default username field is a custom username, we want it to be set to employee code.
    USERNAME_FIELD = 'employee_code'
    REQUIRED_FIELDS = ['name']

    def get_name(self):
        """Returns the admin's name."""

        return self.name

    def get_employee_code(self):
        """Returns the admin's employee code."""

        return self.employee_code

    def __str__(self):
        """Django uses this when it needs to convert the object to a string."""

        return self.employee_code


class Employee(models.Model):
    """Represents an Employee of the institution inside the sytem."""

    employee_code = models.CharField(max_length=50)
    employee_name = models.CharField(max_length=100)

    def __str__(self):
        """Returns an employee's name"""

        return self.employee_name


class BookProfile(models.Model):
    """Represents a Book inside the system"""

    serial_no = models.PositiveIntegerField(primary_key=True)
    account_no = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    year_of_edition = models.PositiveIntegerField()
    no_of_pages = models.PositiveIntegerField()
    publisher = models.CharField(max_length=100)

    def __str__(self):
        """Returns a book's account number and name."""

        return self.account_no + " : " + self.title


class BooksCurrentlyIssued(models.Model):
    """Represents all the books that are currently issued to employee."""
    serial_no = models.PositiveIntegerField(primary_key=True)
    employee_code = models.CharField(max_length=100)
    issue_date = models.DateTimeField()

    def __str__(self):
        """Returns books's serial number"""

        return str(self.serial_no) + " : " + str(self.employee_code)


class BooksIssueReturnHistory(models.Model):
    """Represents all the book issue and return taken place till date."""

    serial_no = models.PositiveIntegerField(primary_key=True)
    employee_code = models.CharField(max_length=100)
    issue_date = models.DateTimeField()
    return_date = models.DateTimeField(null=True)

    def __str__(self):
        """Returns book's serial number"""

        return str(self.serial_no) + " : " + str(self.employee_code)