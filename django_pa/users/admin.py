from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    # Поля, выводящиеся в таблице с пользователями на главном экране
    list_display = ['username', 'full_name', 'status']

    # Поля, по которым выполняется поиск в таблице с пользователями на главном экране
    search_fields = ('full_name', 'username')

    # Сортировка в таблице с пользователями на главном экране
    ordering = ('full_name', 'username')

    # Фильтр по в таблице с пользователями на главном экране
    list_filter = ('status',)

    # Добавление полей в форме существующего элемента
    fieldsets = UserAdmin.fieldsets + (
        ('Реквизиты 1С', {'fields': ('full_name', 'status')}),
    )

    # Добавление полей в форме нового элемента
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Реквизиты 1С', {'fields': ('full_name', 'status')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)