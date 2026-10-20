from django.contrib import admin
from .models import Department, Program, Teacher, HomePage, ExchangeProgram

admin.site.register(Department)
admin.site.register(Program)
admin.site.register(Teacher)
admin.site.register(HomePage)
admin.site.register(ExchangeProgram)