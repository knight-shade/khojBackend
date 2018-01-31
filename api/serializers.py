from django.utils import timezone

from rest_framework import serializers

from . import models


class BookProfileSerializer(serializers.ModelSerializer):
    """A serializer for our book profile objects."""

    class Meta:
        model = models.BookProfile
        fields = ('serial_no', 'account_no', 'author', 'title', 'year_of_edition', 'no_of_pages', 'publisher')

    def create(self, validated_data):
        """Create and return a new book profile."""

        book = models.BookProfile(
            serial_no=validated_data['serial_no'],
            account_no=validated_data['account_no'],
            author=validated_data['author'],
            title=validated_data['title'],
            year_of_edition=validated_data['year_of_edition'],
            no_of_pages=validated_data['no_of_pages'],
            publisher=validated_data['publisher']
        )

        book.save()
        return book

    def update(self, instance, validated_data):
        """Update and return an existing book instance, given validated datad."""

        instance.serial_no = validated_data.get('serial_no', instance.serial_no)
        instance.account_no = validated_data.get('account_no', instance.account_no)
        instance.author = validated_data.get('author', instance.author)
        instance.title = validated_data.get('title', instance.title)
        instance.year_of_edition = validated_data.get('year_of_edition', instance.year_of_edition)
        instance.no_of_pages = validated_data.get('no_of_pages', instance.no_of_pages)
        instance.publisher = validated_data.get('publisher', instance.publisher)

        instance.save()
        return instance


class IssueReturnSerializer(serializers.ModelSerializer):
    """A serializer for books currently issused object."""

    class Meta:
        model = models.BooksCurrentlyIssued
        fields = ('serial_no', 'employee_code', 'issue_date')

    def create(self, validated_data):
        """Create a a new entry in book's issue return model."""
        issued_book = models.BooksCurrentlyIssued(
            serial_no=validated_data['serial_no'],
            employee_code=validated_data['employee_code'],
            issue_date=timezone.now()
        )

        issued_book.save()
        return issued_book

    def update(self, instance, validated_data):
        """Update an existing record in case of a reissue."""
        instance.serial_no = validated_data.get('serial_no', instance.serial_no)
        instance.employee_code = validated_data.get('employee_code', instance.employee_code)
        instance.issue_date = validated_data.get('issue_date', instance.issue_date)

        instance.save()
        return instance


class IssueReturnHistorySerializer(serializers.ModelSerializer):
    """A serializer for books currently issused object."""

    class Meta:
        model = models.BooksCurrentlyIssued
        fields = ('serial_no', 'employee_code')

    def create(self, validated_data):
        """Createa a new entry in book's issue return model."""
        issued_book = models.BooksIssueReturnHistory(
            serial_no=validated_data['serial_no'],
            employee_code=validated_data['employee_code'],
            issue_date=timezone.now()
        )

        issued_book.save()
        return issued_book

    def update(self, instance, validated_data):
        """Update an existing record in case of a reissue."""
        instance.serial_no = validated_data.get('serial_no', instance.serial_no)
        instance.employee_code = validated_data.get('employee_code', instance.employee_code)
        instance.issue_date = validated_data.get('issue_date', instance.issue_date)
        instance.return_date = validated_data.get('return_date', instance.return_date)
        instance.save()
        return instance




