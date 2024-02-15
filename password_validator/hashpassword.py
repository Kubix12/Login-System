import bcrypt


class Login:
    @staticmethod
    def validate_password(password: str) -> str:
        bytes_password = password.encode('utf-8')
        salt_password = bcrypt.gensalt()
        hash_password = bcrypt.hashpw(bytes_password, salt_password)
        return hash_password.decode('utf-8')
