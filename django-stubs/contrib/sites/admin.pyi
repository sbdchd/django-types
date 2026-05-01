from typing import Any

import django.contrib.admin as admin

class SiteAdmin(admin.ModelAdmin[Any]):
    list_display: Any = ...
    search_fields: Any = ...
