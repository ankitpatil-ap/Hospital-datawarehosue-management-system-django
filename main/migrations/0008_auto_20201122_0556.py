
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20201121_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='doctors_notes',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='doctors_visiting_time',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
