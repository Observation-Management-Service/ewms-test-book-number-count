def get_token(token_file: str) -> str:
    with open(token_file, "r") as tf:
        token = tf.read()
    return token