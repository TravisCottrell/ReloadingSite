from django.contrib import admin
from .models import Gun, Bullet, TestResult, Velocity

admin.site.register(Gun)
admin.site.register(Bullet)
admin.site.register(TestResult)
admin.site.register(Velocity)
