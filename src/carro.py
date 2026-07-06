from database import conectar


def criar_carro(id_modelo, nome, renavam, placa, valor, ano):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO carro(id_modelo, nome, renavam, placa, valor, ano)
        VALUES (%s, %s, %s, %s, %s, %s)
        """,
        (id_modelo, nome, renavam, placa, valor, ano)
    )

    conn.commit()
    cursor.close()
    conn.close()


def listar_carros():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            carro.id,
            carro.nome,
            modelo.nome,
            carro.placa,
            carro.valor,
            carro.ano
        FROM carro
        INNER JOIN modelo
            ON carro.id_modelo = modelo.id
        ORDER BY carro.id
    """)

    dados = cursor.fetchall()

    cursor.close()
    conn.close()

    return dados


def atualizar_carro(id, id_modelo, nome, renavam, placa, valor, ano):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE carro
        SET id_modelo = %s,
            nome = %s,
            renavam = %s,
            placa = %s,
            valor = %s,
            ano = %s
        WHERE id = %s
        """,
        (id_modelo, nome, renavam, placa, valor, ano, id)
    )

    conn.commit()
    cursor.close()
    conn.close()


def excluir_carro(id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM carro WHERE id = %s",
        (id,)
    )

    conn.commit()
    cursor.close()
    conn.close()
