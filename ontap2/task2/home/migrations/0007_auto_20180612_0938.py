# Generated by Django 2.0.5 on 2018-06-11 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20180612_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewer',
            name='provider',
            field=models.CharField(choices=[('Garage Project', 'Wellington'), ('Tuatara', 'Wellington')], max_length=30),
        ),
    ]