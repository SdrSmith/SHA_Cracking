import sys
import hashlib
from pwn import *

def sha256sumhex(data):
    """Retourne le hash SHA-256 des données fournies."""
    sha256 = hashlib.sha256()
    sha256.update(data)
    return sha256.hexdigest()

if len(sys.argv) != 3:
    print("Arguments invalides!")
    print(f">>> Usage: {sys.argv[0]} <sha256sum> <path_to_password_file>")
    sys.exit(1)

wanted_hash = sys.argv[1]
password_file = sys.argv[2]
attempts = 0

with log.progress("En cours de craquage...") as p:
    try:
        with open(password_file, "r", encoding='latin-1') as password_list:
            for password in password_list:
                password = password.strip("\n").encode('latin-1')
                password_hash = sha256sumhex(password)
                print(f"[{attempts}] >>> {password.decode('latin-1')} hash = [{password_hash}]")
                if password_hash == wanted_hash:
                    p.success(f"Hash du mot de passe trouvé après {attempts} tentatives! {password.decode('latin-1')} donne le hash {password_hash}!")
                    sys.exit(0)
                attempts += 1
    except FileNotFoundError:
        p.failure("Fichier de mots de passe introuvable !")
    except Exception as e:
        p.failure(f"Une erreur s'est produite : {str(e)}")

    p.failure("Hash du mot de passe non trouvé !")
