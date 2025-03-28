# Generated by Django 3.2.12 on 2022-11-03 11:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tendenci.libs.tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('entities', '0005_entity_show_for_donation'),
    ]

    operations = [
        migrations.CreateModel(
            name='CertCat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('required_credits', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
            ],
            options={
                'verbose_name': 'Certification Category',
                'verbose_name_plural': 'Certification Categories',
            },
        ),
        migrations.CreateModel(
            name='SchoolCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150, unique=True)),
                ('status_detail', models.CharField(choices=[('enabled', 'Enabled'), ('disabled', 'Disabled')], default='enabled', max_length=10, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'School Category',
                'verbose_name_plural': 'School Categories',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allow_anonymous_view', models.BooleanField(default=True, verbose_name='Public can view')),
                ('allow_user_view', models.BooleanField(default=True, verbose_name='Signed in user can view')),
                ('allow_member_view', models.BooleanField(default=True)),
                ('allow_user_edit', models.BooleanField(default=False, verbose_name='Signed in user can change')),
                ('allow_member_edit', models.BooleanField(default=False)),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='Created On')),
                ('update_dt', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('creator_username', models.CharField(max_length=150)),
                ('owner_username', models.CharField(max_length=150)),
                ('status', models.BooleanField(default=True, verbose_name='Active')),
                ('name', models.CharField(db_index=True, max_length=150, unique=True)),
                ('location_type', models.CharField(choices=[('online', 'Online'), ('onsite', 'Onsite')], default='online', max_length=6, verbose_name='Type')),
                ('course_code', models.CharField(blank=True, max_length=50, null=True)),
                ('summary', models.TextField(blank=True, default='')),
                ('description', tendenci.libs.tinymce.models.HTMLField()),
                ('credits', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('min_score', models.DecimalField(decimal_places=1, default=80, max_digits=3)),
                ('status_detail', models.CharField(choices=[('enabled', 'Enabled'), ('disabled', 'Disabled')], default='enabled', max_length=10, verbose_name='Status')),
                ('creator', models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_creator', to=settings.AUTH_USER_MODEL)),
                ('entity', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_entity', to='entities.entity')),
                ('owner', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_owner', to=settings.AUTH_USER_MODEL)),
                ('school_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='trainings.schoolcategory')),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150, unique=True)),
                ('period', models.PositiveSmallIntegerField()),
                ('categories', models.ManyToManyField(through='trainings.CertCat', to='trainings.SchoolCategory')),
            ],
            options={
                'verbose_name': 'Certification',
                'verbose_name_plural': 'Certifications',
            },
        ),
        migrations.AddField(
            model_name='certcat',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainings.schoolcategory'),
        ),
        migrations.AddField(
            model_name='certcat',
            name='certification',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainings.certification'),
        ),
        migrations.AlterUniqueTogether(
            name='certcat',
            unique_together={('certification', 'category')},
        ),
    ]
