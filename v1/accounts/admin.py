from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        ('Account Information', {
            'fields': (
                ('email', 'username', 'password',),
            )
        },),
        (('Personal Information'), {
            'fields': (
                ('avatar', 'first_name', 'last_name',),
            )
        },),
        (('Permissions'), {
            'fields': (
                ('is_active', 'is_staff', 'is_admin', 'is_superuser',),
                'groups',
                'user_permissions',
            ),
            'classes': ('collapse',)
        },),
        (('Important Dates'), {
            'fields': (
                ('date_joined', 'last_login',),
            ),
            'classes': ('collapse',)
        },),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name', 'last_name', 'password1', 'password2',),
        },),
    )

    readonly_fields = ('date_joined', 'last_login',)
    search_fields = ('username',)
    ordering = ('username',)


admin.site.register(get_user_model(), UserAdmin)
