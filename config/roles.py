
from models.permissions import Permission
from models.role import Role

def __init__():
    create_default_roles()

def create_default_roles():
    create = Permission("CRIAR_USUARIO")
    read = Permission("LER_USUARIO")
    update = Permission("ATUALIZAR_USUARIO")
    delete = Permission("DELETAR_USUARIO")

    admin = Role("ADMIN")
    admin.add_permission(create)
    admin.add_permission(read)
    admin.add_permission(update)
    admin.add_permission(delete)

    editor = Role("EDITOR")
    editor.add_permission(read)
    editor.add_permission(update)

    viewer = Role("VIEWER")
    viewer.add_permission(read)

    return admin, editor, viewer
admin,editor,viewer =create_default_roles()
def get_admin_role():
    return admin
def get_editor_role():
    return editor
def get_viewer_role():
    return viewer
