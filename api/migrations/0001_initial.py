# Generated by Django 3.1.7 on 2021-04-16 12:24

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('wardadhaar', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(100000000000), django.core.validators.MaxValueValidator(999999999999)])),
                ('bloodgroup', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=100)),
                ('dob', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('crnumber', models.CharField(default='_', max_length=100)),
                ('wardadhaar', models.IntegerField(validators=[django.core.validators.MinValueValidator(100000000000), django.core.validators.MaxValueValidator(999999999999)])),
                ('patientname', models.CharField(default='Patient', max_length=100)),
                ('docnumber', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('createdby', models.CharField(default='admin', max_length=100)),
                ('createdat', models.DateTimeField(auto_now_add=True)),
                ('department', models.CharField(default='default-department', max_length=100)),
                ('consultantuname', models.CharField(max_length=100)),
                ('bsa', models.FloatField()),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('nurseflag', models.CharField(default='_', max_length=100)),
                ('perfusionistflag', models.CharField(default='_', max_length=100)),
                ('doctorflag', models.CharField(default='_', max_length=100)),
                ('technicianflag', models.CharField(default='_', max_length=100)),
                ('consultantflag', models.CharField(default='_', max_length=100)),
                ('state', models.CharField(default='Approved', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CardiacSupplied',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('A_1_name', models.CharField(default='_', max_length=500)),
                ('A_1_descr', models.CharField(default='_', max_length=500)),
                ('A_1_brand', models.CharField(default='_', max_length=500)),
                ('A_1_qty', models.CharField(default='0', max_length=100)),
                ('A_2A_name', models.CharField(default='_', max_length=500)),
                ('A_2A_descr', models.CharField(default='_', max_length=500)),
                ('A_2A_brand', models.CharField(default='_', max_length=500)),
                ('A_2A_qty', models.CharField(default='0', max_length=100)),
                ('A_2B_name', models.CharField(default='_', max_length=500)),
                ('A_2B_descr', models.CharField(default='_', max_length=500)),
                ('A_2B_brand', models.CharField(default='_', max_length=500)),
                ('A_2B_qty', models.CharField(default='0', max_length=100)),
                ('A_3A_name', models.CharField(default='_', max_length=500)),
                ('A_3A_descr', models.CharField(default='_', max_length=500)),
                ('A_3A_brand', models.CharField(default='_', max_length=500)),
                ('A_3A_qty', models.CharField(default='0', max_length=100)),
                ('A_3B_name', models.CharField(default='_', max_length=500)),
                ('A_3B_descr', models.CharField(default='_', max_length=500)),
                ('A_3B_brand', models.CharField(default='_', max_length=500)),
                ('A_3B_qty', models.CharField(default='0', max_length=100)),
                ('B_1_name', models.CharField(default='_', max_length=500)),
                ('B_1_descr', models.CharField(default='_', max_length=500)),
                ('B_1_brand', models.CharField(default='_', max_length=500)),
                ('B_1_qty', models.CharField(default='0', max_length=100)),
                ('B_2A_name', models.CharField(default='_', max_length=500)),
                ('B_2A_descr', models.CharField(default='_', max_length=500)),
                ('B_2A_brand', models.CharField(default='_', max_length=500)),
                ('B_2A_qty', models.CharField(default='0', max_length=100)),
                ('B_2B_name', models.CharField(default='_', max_length=500)),
                ('B_2B_descr', models.CharField(default='_', max_length=500)),
                ('B_2B_brand', models.CharField(default='_', max_length=500)),
                ('B_2B_qty', models.CharField(default='0', max_length=100)),
                ('B_3A_name', models.CharField(default='_', max_length=500)),
                ('B_3A_descr', models.CharField(default='_', max_length=500)),
                ('B_3A_brand', models.CharField(default='_', max_length=500)),
                ('B_3A_qty', models.CharField(default='0', max_length=100)),
                ('B_3B_name', models.CharField(default='_', max_length=500)),
                ('B_3B_descr', models.CharField(default='_', max_length=500)),
                ('B_3B_brand', models.CharField(default='_', max_length=500)),
                ('B_3B_qty', models.CharField(default='0', max_length=100)),
                ('B_3C_name', models.CharField(default='_', max_length=500)),
                ('B_3C_descr', models.CharField(default='_', max_length=500)),
                ('B_3C_brand', models.CharField(default='_', max_length=500)),
                ('B_3C_qty', models.CharField(default='0', max_length=100)),
                ('B_3D_name', models.CharField(default='_', max_length=500)),
                ('B_3D_descr', models.CharField(default='_', max_length=500)),
                ('B_3D_brand', models.CharField(default='_', max_length=500)),
                ('B_3D_qty', models.CharField(default='0', max_length=100)),
                ('request', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='api.requests')),
            ],
        ),
        migrations.CreateModel(
            name='CardiacRequested',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('A_1_name', models.CharField(default='ACT Tubes', max_length=500)),
                ('A_1_descr', models.CharField(default='_', max_length=500)),
                ('A_1_brand', models.CharField(default='_', max_length=500)),
                ('A_1_qty', models.CharField(blank=True, default='0', max_length=100)),
                ('A_2A_name', models.CharField(default='Arterial line cannula (Adult)', max_length=500)),
                ('A_2A_descr', models.CharField(default='_', max_length=500)),
                ('A_2A_brand', models.CharField(default='_', max_length=500)),
                ('A_2A_qty', models.CharField(blank=True, default='0', max_length=100)),
                ('A_2B_name', models.CharField(default='Arterial line cannula (Pediatric)', max_length=500)),
                ('A_2B_descr', models.CharField(default='_', max_length=500)),
                ('A_2B_brand', models.CharField(default='_', max_length=500)),
                ('A_2B_qty', models.CharField(blank=True, default='0', max_length=100)),
                ('A_3A_name', models.CharField(default='Blood glucose strip', max_length=500)),
                ('A_3A_descr', models.CharField(default='_', max_length=500)),
                ('A_3A_brand', models.CharField(default='_', max_length=500)),
                ('A_3A_qty', models.CharField(blank=True, default='0', max_length=100)),
                ('A_3B_name', models.CharField(default='Blood transfusion Set', max_length=500)),
                ('A_3B_descr', models.CharField(default='_', max_length=500)),
                ('A_3B_brand', models.CharField(default='_', max_length=500)),
                ('A_3B_qty', models.CharField(blank=True, default='0', max_length=100)),
                ('B_1_name', models.CharField(default='_', max_length=500)),
                ('B_1_descr', models.CharField(default='_', max_length=500)),
                ('B_1_brand', models.CharField(default='_', max_length=500)),
                ('B_1_qty', models.CharField(default='0', max_length=100)),
                ('B_2A_name', models.CharField(default='_', max_length=500)),
                ('B_2A_descr', models.CharField(default='_', max_length=500)),
                ('B_2A_brand', models.CharField(default='_', max_length=500)),
                ('B_2A_qty', models.CharField(default='0', max_length=100)),
                ('B_2B_name', models.CharField(default='_', max_length=500)),
                ('B_2B_descr', models.CharField(default='_', max_length=500)),
                ('B_2B_brand', models.CharField(default='_', max_length=500)),
                ('B_2B_qty', models.CharField(default='0', max_length=100)),
                ('B_3A_name', models.CharField(default='_', max_length=500)),
                ('B_3A_descr', models.CharField(default='_', max_length=500)),
                ('B_3A_brand', models.CharField(default='_', max_length=500)),
                ('B_3A_qty', models.CharField(default='0', max_length=100)),
                ('B_3B_name', models.CharField(default='_', max_length=500)),
                ('B_3B_descr', models.CharField(default='_', max_length=500)),
                ('B_3B_brand', models.CharField(default='_', max_length=500)),
                ('B_3B_qty', models.CharField(default='0', max_length=100)),
                ('B_3C_name', models.CharField(default='_', max_length=500)),
                ('B_3C_descr', models.CharField(default='_', max_length=500)),
                ('B_3C_brand', models.CharField(default='_', max_length=500)),
                ('B_3C_qty', models.CharField(default='0', max_length=100)),
                ('B_3D_name', models.CharField(default='_', max_length=500)),
                ('B_3D_descr', models.CharField(default='_', max_length=500)),
                ('B_3D_brand', models.CharField(default='_', max_length=500)),
                ('B_3D_qty', models.CharField(default='0', max_length=100)),
                ('docnumber', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='api.requests')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('category', models.CharField(default='Nurse', max_length=100)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
