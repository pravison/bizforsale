# Generated by Django 4.2.4 on 2023-10-05 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_comment_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-date']},
        ),
    ]
