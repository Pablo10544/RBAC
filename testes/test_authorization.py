from models.permissions import Permission
from models.role import Role
from models.user import User
from services.authorization import AuthorizationService
import config.roles as roles

# TESTE DE ADMIN PODER DELETAR USUARIOS
def test_admin_can_execute_permission():
    admin = roles.get_admin_role()
    user = User("joao")
    user.add_role(admin)

    authorization = AuthorizationService()

    assert authorization.can(user, "DELETAR_USUARIO")


# TESTE VIEWER NÃO PODE CRIAR USUARIOS
def test_viewer_cannot_execute_permission():
    viewer = roles.get_viewer_role()
    user = User("joao")
    user.add_role(viewer)
    authorization = AuthorizationService()
    assert not authorization.can(user, "CRIAR_USUARIO")

# TESTE EDITOR PODE ATUALIZAR USUARIO
def test_editor_can_edit_permission():
    editor = roles.get_editor_role()
    user = User("joao")
    user.add_role(editor)
    auth = AuthorizationService()
    assert auth.can(user,"ATUALIZAR_USUARIO")