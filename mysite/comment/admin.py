from django.contrib import admin
from mysite.comment.models import CommentModel, FamousCustomerModel

admin.site.register(CommentModel)
admin.site.register(FamousCustomerModel)
