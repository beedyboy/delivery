# Generated by Django 2.0 on 2018-11-27 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ('created_at',), 'verbose_name': 'Delivery Task', 'verbose_name_plural': 'Delivery Tasks'},
        ),
        migrations.AddField(
            model_name='task',
            name='celery_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='completed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]