# Generated by Django 4.0.4 on 2022-05-22 22:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated at')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created at')),
                ('telegram_id', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
