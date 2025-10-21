# Solución ejercicio 81: CLI simple que usa una clase para procesar comandos (sin input blocking)
class CLI:
    def __init__(self): self.commands = {}
    def register(self,name,func): self.commands[name]=func
    def run(self, name, *args, **kwargs):
        fn = self.commands.get(name)
        if not fn: return 'Comando no encontrado'
        return fn(*args, **kwargs)

if __name__ == '__main__':
    cli = CLI()
    cli.register('hola', lambda: 'Hola!')
    print(cli.run('hola'))
