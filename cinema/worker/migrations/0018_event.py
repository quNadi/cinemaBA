# Generated by Django 3.0.1 on 2020-01-31 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0017_auto_20200129_2051'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(null=True)),
                ('showtime_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='worker.Reservation')),
            ],
        ),
    ]
