from django.contrib import admin

from .models import Complaints, Flat, Owner


class OwnerInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ["owner"]
    extra = 3


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'addres',)
    list_editable = ['new_building']
    list_display = ['address', 'price', 'new_building', 'construction_year', 'town']
    readonly_fields = ['created_at']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ('liked_by',)
    inlines = [OwnerInline, ]


@admin.register(Complaints)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat', 'who',)


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)
