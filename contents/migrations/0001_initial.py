# Generated by Django 2.0.13 on 2020-02-10 06:22

import contents.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('text', models.TextField(default='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '컨텐츠',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to=contents.models.image_upload_to)),
                ('order', models.SmallIntegerField()),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contents.Content')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='image',
            unique_together={('content', 'order')},
        ),
    ]
