from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Post model.
    """
    list_display = ('title', 'author', 'published_date', 'image')
    list_filter = ('published_date', 'author')
    search_fields = ('title', 'content')
    #fields = ('title', 'author', 'content', 'published_date', 'image')  # TODO: do i have to uncomment this? how does it work?
    #prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_date'
    ordering = ('-published_date',)

    def save_model(self, request, obj, form, change): # TODO: is this method necessary?
        """
        Method to automatically set the post's author as the logged-in user.
        """
        if not obj.author:  # Set the author only if it's not already set
            obj.author = request.user
        obj.save()
