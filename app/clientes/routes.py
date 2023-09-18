from flask import render_template, redirect, flash
from app.clientes import clientes
import app
import os
from .forms import NewClientForm, EditClientForm


@clientes.route('/create',methods=['GET', 'POST'])
def creat():
    p = app.models.Cliente()
    form = NewClientForm()
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.add(p)
        app.db.session.commit()
        flash("Cliente registrado correctamente")
        return redirect('/clientes/listar')
    return render_template('new_clientes.html', 
                            form = form)

@clientes.route('/listar')
def listar():
    clientes =app.models.Cliente.query.all()
    return render_template("list_clientes.html",
                            clientes = clientes)

@clientes.route('/update/<cliente_id>', methods=['GET', 'POST'])
def edit(cliente_id):
    p = app.models.Cliente.query.get(cliente_id)
    form = EditClientForm(obj=p)
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.commit()
        flash("Cliente actualizado")
        return redirect('/clientes/listar')
    return render_template('new_clientes.html', form=form)

@clientes.route('/delete/<cliente_id>')
def delete(cliente_id):
    p=app.models.Cliente.query.get(cliente_id)
    app.db.session.delete(p)
    app.db.session.commit()
    flash("cliente eliminado")
    return redirect('/clientes/listar')