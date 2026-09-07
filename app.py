from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

livros = [
    {
        'id': 1,
        'titulo': 'Dom Casmurro',
        'autor': 'Machado de Assis',
        'descricao': 'Um clássico da literatura brasileira, narrado por Bentinho.'
    },
    {
        'id': 2,
        'titulo': '1984',
        'autor': 'George Orwell',
        'descricao': 'Uma distopia sobre um regime totalitário e o controle da informação.'
    },
    {
        'id': 3,
        'titulo': 'O Pequeno Príncipe',
        'autor': 'Antoine de Saint-Exupéry',
        'descricao': 'Uma fábula poética sobre amizade e descobertas.'
    }
]

@app.route('/')
def index():
    return render_template('index.html', livros=livros)

@app.route('/livro/<int:id>')
def detalhes(id):
    livro = next((l for l in livros if l['id'] == id), None)
    return render_template('detalhes.html', livro=livro)

if __name__ == '__main__':
    app.run(debug=True)
