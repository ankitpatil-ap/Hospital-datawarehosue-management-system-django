
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='dob',
            field=models.DateField(null=True),
        ),
    ]
