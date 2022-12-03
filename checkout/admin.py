from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date', 'order_total', 'original_cart',
              'stripe_pid',)

    fields = ('order_number', 'user_profile', 'date', 'first_name', 'last_name',
              'email',
              'phone_number',
              'street_address1',
              'street_address2',
              'town_or_city',
              'county',
              'country',
              'postcode',
              'order_total',
              'original_cart',
              'stripe_pid',)

    list_display = ('order_number', 'date', 'first_name',
                    'last_name', 'order_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
