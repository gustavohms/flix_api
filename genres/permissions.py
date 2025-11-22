from rest_framework import permissions
## Código de exemplo, estamos usando o global.
class GenrePermissionClass(permissions.BasePermission):

    def has_permission(self, request, view):
        #Lógica da permissão
        if request.method in ['GET', 'OPTIONS', 'HEAD']:
            return request.user.has_perm('genres.view_genre')
        
        if request.method == 'POST':
            return request.user.has_perm('genres.add_genre')
        
        if request.method in ['PATCH', 'PUT']:
            return request.user.has_perm('genre.change_genre')
        
        if request.method == 'DELETE':
            return request.user.has_perm('genres.delete_genre')
        return False