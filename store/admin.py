from django.contrib import admin

# Register your models here.


from store.models import Product, Client, Buy

class Products(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'thumbnailHd', 'date')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_per_page = 25
    
admin.site.register(Product, Products)
    

class Clients(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25
    
admin.site.register(Client, Clients)
    
    
class Buys(admin.ModelAdmin):
    list_display = ('id', 'cliente_id', 'card_number', 'value', 'cvv', 'card_holder_name', 'exp_date', 'data',)
    list_display_links = ('id', 'cliente_id')
    search_fields = ('cliente_id',)
    list_per_page = 25
    
admin.site.register(Buy, Buys)
    
