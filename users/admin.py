from django.contrib import admin
from .models import User
from .forms import CreateUserForm

class UserAdmin(admin.ModelAdmin):
    model = User
    add_form = CreateUserForm
# Register your models here.
admin.site.register(User,UserAdmin)