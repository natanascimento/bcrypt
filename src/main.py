import bcrypt

password = '12345'

# Criptografando uma senha pela primeira vez com um salt aleatorio
hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Método para chegar se a senha digitada é igual a senha criptografada
def check_password(password, hashed_password):
    if not bcrypt.checkpw(password.encode('utf-8'), hashed_password):
        print("403 Forbidden")
    else:
        print("Authenticated")

check_password('12345', hashed)