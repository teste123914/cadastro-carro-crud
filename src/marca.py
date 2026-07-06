from database import conectar


def criar_marca(nome):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO marca(nome) VALUES (%s)",
        (nome,)
    )

    conn.commit()
    cursor.close()
    conn.close()


def listar_marcas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT id, nome FROM marca ORDER BY id")

    dados = cursor.fetchall()

    cursor.close()
    conn.close()

    return dados


def atualizar_marca(id, nome):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE marca
        SET nome = %s
        WHERE id = %s
        """,
        (nome, id)
    )

    conn.commit()
    cursor.close()
    conn.close()


def excluir_marca(id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM marca WHERE id = %s",
        (id,)
    )

    conn.commit()
    cursor.close()
    conn.close()
