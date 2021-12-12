from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_patient_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='status',
            field=models.CharField(default='recovering', max_length=50),
            preserve_default=False,
        ),
    ]
