import funciones
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    return '''
    <h2>Instructions:</h2>
    <ul>
        <li>Regresa cuantas hojas hay en el archivo: <code>/num_hojas/pagina.xls</code></li>
        <li>Cuenta el numero de filas y columnas en la hoja especificada: <code>/count_row_col/pagina.xls/&lt;int:num_hoja&gt;</code></li>
        <li>Regresa el contenido de una celda en una hoja especifica: <code>/cell_value/pagina.xls/&lt;int:num_hoja&gt;/&lt;int:row&gt;/&lt;int:col&gt;</code></li>
        <li>Regresa el contenido de una columna completa: <code>/col_values/pagina.xls/&lt;int:num_hoja&gt;/&lt;int:col&gt;</code></li>
        <li>Verifica si una columna contiene un valor de cabecera especifico: <code>/verify_col/pagina.xls/&lt;int:num_hoja&gt;/&lt;int:col&gt;/&lt;cabecera&gt;</code></li>
        <li>Regresa el contenido de N columnas en la hoja X: <code>/get_multiple_cols/pagina.xls/&lt;int:num_hoja&gt;/&lt;cols&gt;</code></li>
        <li>Regresa toda la hoja en una matriz ordenada: <code>/ord_matrix/pagina.xls/&lt;int:num_hoja&gt;</code></li>
    </ul>
    '''

# punto 1
@app.route('/num_hojas/<path:pagina>')
def num_hojas(pagina):
    return jsonify({"Numero de hojas": funciones.num_hojas(pagina)})

# punto 2
@app.route('/count_row_col/<path:pagina>/<int:num_hoja>')
def count_row_col(pagina, num_hoja):
    num_rows, num_cols = funciones.count_row_col(pagina, num_hoja)

    return jsonify({'archivo': pagina, 'hoja': num_hoja,  'rows': num_rows, 'cols': num_cols})

# punto 3
@app.route('/cell_value/<path:pagina>/<int:num_hoja>/<int:row>/<int:col>')
def get_cell_value(pagina, num_hoja, row, col):
    cell_value = funciones.get_cell_value(
        pagina, num_hoja, row, col)

    return jsonify(cell_value)

# punto 4
@app.route('/col_values/<path:pagina>/<int:num_hoja>/<int:col>')
def get_col(pagina, num_hoja, col):
    col_values = funciones.get_col(
        pagina, num_hoja, col)

    return jsonify(col_values)

# punto 5
@app.route('/verify_col/<path:pagina>/<int:num_hoja>/<int:col>/<cabecera>')
def verify_col(pagina, num_hoja, col, cabecera):
    col_value = funciones.verify_col(pagina, num_hoja, col, cabecera)
    return jsonify(col_value)

# punto 6
@app.route('/get_multiple_cols/<path:pagina>/<int:num_hoja>/<cols>')
def get_multiple_cols(pagina, num_hoja, cols):
    index = []
    for col in cols.split(','):
        index.append(int(col))
    return jsonify(funciones.get_multiple_cols(pagina, num_hoja, index))

# punto 7
@app.route('/ord_matrix/<path:pagina>/<int:num_hoja>')
def ord_matrix(pagina, num_hoja):
    return jsonify(funciones.ord_matrix(pagina, num_hoja))


if __name__ == '__main__':
    app.run()
