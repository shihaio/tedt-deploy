from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea, CharField
from django import forms
from django.db import models
from django.contrib import admin
from .models import User
from .models import Task


class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('email', 'username',)
    list_filter = ('email', 'username', 'is_active', 'is_staff')
    ordering = ('-user_created_date',)
    list_display = ('email', 'id','username',
                    'is_active', 'is_staff')

    fieldsets = ()
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_admin', 'is_active', 'is_staff')}
         ),
    )
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdminConfig)

admin.site.register(Task)
