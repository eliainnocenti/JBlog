from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'image')     # Add the fields you want to display in the list
    list_filter = ('user',)                     # Filter by user
    search_fields = ('user__username', 'bio')   # Allow search by username and bio
    ordering = ('user',)                        # Order by user

    # If you have specific fields to display in the edit form, you can use fieldsets
    fieldsets = (
        (None, {
            'fields': ('user', 'bio', 'image')
        }),
    )

    # If you have slugs or similar fields, you can use prepopulated_fields
    # prepopulated_fields = {"slug": ("title",)}

# If you need to add custom actions
# def make_published(modeladmin, request, queryset):
#     queryset.update(status='published')
# make_published.short_description = "Mark selected stories as published"
# actions = [make_published]
