from flask import Flask, jsonify
from conexion_oracle import query_to_dict


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def main_page():
        try:
            # prueba sencilla de una consulta a la base de datos
            data = query_to_dict(
                "SELECT TO_CHAR(SYSDATE, 'YYYY-MM-DD HH24:MI:SS') AS fecha_actual"
                " FROM dual"
            )

            return jsonify(
                {
                    "status": "Conexion exitosa a XE 21c Oracle",
                    "data": data,
                }
            )
        except Exception as ex:
            return jsonify({"errorStatus": str(ex)}), 500
    return app