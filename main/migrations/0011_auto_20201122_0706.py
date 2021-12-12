from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_patient_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='doctors_notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='doctors_visiting_time',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
