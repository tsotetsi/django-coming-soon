from django.contrib import admin

from coming_soon.models import PrelaunchSignUp


class PrelaunchSignUpAdmin(admin.ModelAdmin):
    pass


admin.site.register(PrelaunchSignUp, PrelaunchSignUpAdmin)
