from database import conectar


def criar_modelo(nome, id_marca):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO modelo(nome, id_marca) VALUES (%s, %s)",
        (nome, id_marca)
    )

    conn.commit()
    cursor.close()
    conn.close()


def listar_modelos():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            modelo.id,
            modelo.nome,
            marca.nome
        FROM modelo
        INNER JOIN marca
            ON modelo.id_marca = marca.id
        ORDER BY modelo.id
    """)

    dados = cursor.fetchall()

    cursor.close()
    conn.close()

    return dados


def atualizar_modelo(id, nome, id_marca):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE modelo
        SET nome = %s,
            id_marca = %s
        WHERE id = %s
        """,
        (nome, id_marca, id)
    )

    conn.commit()
    cursor.close()
    conn.close()


def excluir_modelo(id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM modelo WHERE id = %s",
        (id,)
    )

    conn.commit()
    cursor.close()
    conn.close()
