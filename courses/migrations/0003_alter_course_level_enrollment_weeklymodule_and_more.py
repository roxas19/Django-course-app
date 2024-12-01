# Generated by Django 5.1.1 on 2024-11-27 11:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_week'),
        ('users', '0004_remove_instructor_photo_remove_student_grade_level_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='level',
            field=models.CharField(choices=[('Beginner', 'Beginner'), ('Advanced', 'Advanced')], max_length=50),
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('progress', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('enrolled_on', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollments', to='courses.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.student')),
            ],
        ),
        migrations.CreateModel(
            name='WeeklyModule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('video', models.FileField(blank=True, null=True, upload_to='weekly_modules/videos/')),
                ('resources', models.FileField(blank=True, null=True, upload_to='weekly_modules/resources/')),
                ('quiz', models.TextField(blank=True)),
                ('order', models.PositiveIntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weekly_modules', to='courses.course')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.DeleteModel(
            name='Week',
        ),
    ]
