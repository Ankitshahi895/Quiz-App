# Generated by Django 2.2.28 on 2024-03-08 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_delete_userprofile'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='answer',
            table='answer_table',
        ),
        migrations.AlterModelTable(
            name='marks_of_user',
            table='Marks_table',
        ),
        migrations.AlterModelTable(
            name='question',
            table='Question_table',
        ),
        migrations.AlterModelTable(
            name='quiz',
            table='Quiz_table',
        ),
    ]