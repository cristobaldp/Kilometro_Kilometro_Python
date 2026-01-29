from app.repository.usuario_repository import UsuarioRepository


class UsuarioService:

    def __init__(self):
        self.repo = UsuarioRepository()

    # -------------------------
    # LOGIN
    # -------------------------
    def login(self, username, password):
        if not username or not password:
            return None
        return self.repo.find_by_username_and_password(username, password)

    # -------------------------
    # REGISTRO
    # -------------------------
    def registrar_usuario(self, datos):
        # 🔒 Comprobar si el username ya existe
        if self.repo.existe_username(datos["username"]):
            return None  # ← el controller mostrará el mensaje

        self.repo.insert(datos)
        return self.login(datos["username"], datos["password"])

    # -------------------------
    # PERFIL
    # -------------------------
    def actualizar_perfil(self, datos):
        self.repo.update_perfil(datos)

    # -------------------------
    # CONTRASEÑA
    # -------------------------
    def cambiar_password(self, user_id, nueva_password):
        if not nueva_password or len(nueva_password) < 4:
            raise ValueError("La contraseña debe tener al menos 4 caracteres")

        self.repo.update_password(user_id, nueva_password)

    # -------------------------
    # BORRAR CUENTA
    # -------------------------
    def eliminar_cuenta(self, user_id):
        self.repo.delete_user(user_id)

    # -------------------------
    # AJUSTES
    # -------------------------
    def obtener_ajustes(self, user_id):
        return self.repo.get_ajustes(user_id)

    def guardar_ajustes(self, user_id, datos):
        self.repo.update_ajustes(user_id, datos)