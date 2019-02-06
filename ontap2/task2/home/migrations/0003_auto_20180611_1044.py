# Generated by Django 2.0.5 on 2018-06-10 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20180611_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beerinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('1', 'Bad'), ('2', 'Ok'), ('3', 'good'), ('4', 'Amazing'), ('5', 'Exceptional')], default='o', help_text='Beer Rating', max_length=1),
        ),
    ]
