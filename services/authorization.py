class AuthorizationService:

    def can(self, user, permission_name):
        for role in user.roles:
            for permission in role.permissions:
                if permission.name == permission_name:
                    return True

        return False