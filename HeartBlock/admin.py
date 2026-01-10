from django.contrib import admin
from .models import Group, Member

class MemberInline(admin.TabularInline):
    model = Member
    extra = 0

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'code_number', 'group_type', 'group_bio')
    inlines = [MemberInline]

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'group', 'age')
    list_filter = ('group',)