
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone_num', models.CharField(max_length=10)),
                ('address', models.TextField()),
                ('prior_ailments', models.TextField()),
                ('bed_num', models.CharField(max_length=20)),
            ],
        ),
    ]
