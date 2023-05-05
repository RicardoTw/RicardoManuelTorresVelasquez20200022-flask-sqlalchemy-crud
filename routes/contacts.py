from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.contact import Contact
from utils.db import db

contacts = Blueprint("contacts", __name__)


@contacts.route('/')
def index():
    contacts = Contact.query.all()
    return render_template('index.html', contacts=contacts)


@contacts.route('/new', methods=['POST'])
def add_contact():
    if request.method == 'POST':

        # Recibir datos del formulario
        fullname = request.form['fullname']
        email = request.form['email']
        phone = request.form['phone']

        # Crear un nuevo objeto Contacto
        new_contact = Contact(fullname, email, phone)

        # Guardar el objeto en la base de datos
        db.session.add(new_contact)
        db.session.commit()

        flash('Contact added successfully!')

        return redirect(url_for('contacts.index'))


@contacts.route("/update/<string:id>", methods=["GET", "POST"])
def update(id):
    # Obtener contacto por Id
    print(id)
    contact = Contact.query.get(id)

    if request.method == "POST":
        contact.fullname = request.form['fullname']
        contact.email = request.form['email']
        contact.phone = request.form['phone']

        db.session.commit()

        flash('Contact updated successfully!')

        return redirect(url_for('contacts.index'))

    return render_template("update.html", contact=contact)

#Define una ruta para eliminar un registro de contacto en la base de datos a través de una solicitud GET.
@contacts.route("/delete/<id>", methods=["GET"])
def delete(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()

    flash('Contact deleted successfully!')

    return redirect(url_for('contacts.index'))


@contacts.route("/about")
def about():
    return render_template("about.html")
