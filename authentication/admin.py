from django.contrib import admin
from authentication.models import User
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'email', 'is_superuser')
    list_display_links = ('username', 'email')

admin.site.register(User, UserAdmin)
