from flask import Flask, render_template


app = Flask(__name__)


class Avaliacoes:
    def __init__(self, titulo, ano, autor, nota, usuario):
        self._titulo = titulo.title()
        self.ano = ano
        self._autor = autor.title()
        self._nota = nota
        self._usuario = usuario.title()


livro1 = Avaliacoes('harry potter e a pedra filosofal', 2001, 'j.k rowling', 9.5, 'Francisco José')
livro2 = Avaliacoes('1984', 1949, 'george orwell', 10, 'Cristina Maria')
livro3 = Avaliacoes('rápido e devagar', 2011, 'daniel kahneman', 9, 'Ana Maria')
lista = [livro1, livro2, livro3]


@app.route('/')
def index():
    return render_template('lista2.html',
                           titulo="IMDb Book",
                           descricao="Veja a opinião de leitores sobre diversos livros",
                           opinioes=lista)


app.run(debug=True)
