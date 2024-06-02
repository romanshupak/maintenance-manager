from django.core.management import call_command
from io import StringIO

# Підключення до Django
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "maintenance_manager.settings")
django.setup()

# Експорт даних
output = StringIO()
call_command("dumpdata", "--indent", "4", stdout=output)

# Запис у файл з явним зазначенням кодування
with open("data.json", "w", encoding="utf-8") as json_file:
    json_file.write(output.getvalue())
