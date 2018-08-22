from django.contrib import admin

# Register your models here.
from .models import Shakha,Swaymsevak,Spersonal,Sshakha,Gat,Ghosh,Sangh_Shikshan,Utsav

admin.site.register(Shakha)
class GatAdmin(admin.ModelAdmin):
    '''
        Admin View for Sangh_Shikshan
    ''' 
    list_display = ('__str__','gatnayak','shakha','note')
admin.site.register(Gat,GatAdmin)

class SpersonalInline(admin.StackedInline):
	model = Spersonal

admin.site.register(Sshakha)
class SshakhaInline(admin.TabularInline):
	model = Sshakha

# admin.site.register(Sangh_Shikshan)
class Sangh_ShikshanInline(admin.TabularInline):
	model = Sangh_Shikshan
class Sangh_ShikshanAdmin(admin.ModelAdmin):
    '''
        Admin View for Sangh_Shikshan
    '''	
    list_display = ('__str__','shikshan','year')
    list_filter =['shikshan']
    verbose_name = "Shakha Related Information"

admin.site.register(Sangh_Shikshan, Sangh_ShikshanAdmin)



# admin.site.register(Ghosh)
class GhoshInline(admin.TabularInline):
	model = Ghosh
class GhoshAdmin(admin.ModelAdmin):
    '''
        Admin View for Ghosh
    '''
    list_display = ('__str__','ghosh','rachna')


admin.site.register(Ghosh, GhoshAdmin)


# @admin.site.register(Swaymsevak)
class SwaymsevakAdmin(admin.ModelAdmin):
    '''
        Admin View for Swaymsevak
    '''
# To do : colapsible inline
    inlines = [
        SpersonalInline,SshakhaInline,GhoshInline,Sangh_ShikshanInline
    ]
    def swaymsevak_type(self,obj):
        return obj.sshakha.get_swaymsevak_type_display()
    swaymsevak_type.short_description = 'Type of Swaymsevak'

    def swaymsevak_basti(self, obj):
        return obj.spersonal.get_basti_display()
    swaymsevak_basti.short_description = 'Basti'

    # def swaymsevak_join_year(self,obj):
    #     return obj.sshakha.join_Year
    # swaymsevak_join_year.short_description = 'Join_year'
    def ganvesh_count(self,obj):
        return obj.sshakha.ganvesh_count
    ganvesh_count.short_description = 'Ganvesh/6'
    # ganvesh_count.admin_order_field = 'sshakha.ganvesh_count'
    # ganvesh_count.admin_order_first_type = 'asc'
    def contact_number(self,obj):
        return obj.spersonal.contact
    contact_number.short_description = 'Phone'
    list_display = ('__str__','shakha','swaymsevak_type','swaymsevak_basti','ganvesh_count','contact_number','last_modified')
    search_fields = ['fname','lname']
    list_filter = ['shakha','sshakha__swaymsevak_type','spersonal__basti','sshakha__ganvesh_count']
    

admin.site.register(Swaymsevak, SwaymsevakAdmin)

class UtsavAdmin(admin.ModelAdmin):
    fields = ('name','shakha', ('location','time','cost','vakta'), ('bal','tarun','shishu','any'),'feedback')
    list_filter=['shakha','name']
    list_display = ('name','shakha','time','location','vakta')
admin.site.register(Utsav,UtsavAdmin)