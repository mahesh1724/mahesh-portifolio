from django.contrib import admin
from .models import VisitorLog

admin.site.register(VisitorLog)  # ✅ Only this should exist ONCE

