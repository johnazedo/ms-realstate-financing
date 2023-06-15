# Generated by Django 4.2.2 on 2023-06-12 00:42

from django.db import migrations, models
import loan.manager
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fee',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True, null=True)),
                ('fee_percent_per_year', models.FloatField(default=12.0)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('active', loan.manager.ActiveBaseEntityManager()),
                ('objects', loan.manager.DefaultEntityManager()),
            ],
        ),
    ]