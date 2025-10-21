# Solución ejercicio 85: Clase que controla acceso (simple ACL) con roles
class ACL:
    def __init__(self): self.roles = {}
    def add_role(self,user,role): self.roles[user]=role
    def permitido(self,user,perm): return self.roles.get(user)=='admin' or perm=='read'

if __name__ == '__main__':
    a = ACL(); a.add_role('juan','admin'); print(a.permitido('juan','write'))
