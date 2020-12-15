#! usr/bin/ env python
# encoding: utf-8

from start import app, db
from models import Event, Registration
from flask import render_template, jsonify, redirect, request, flash
import random


@app.route('/')
def start():
    events = Event.get_all_events()
    registered = [Registration.query.filter_by(event_id=event.id).all() for event in events]
    return render_template('page_layout/home/templates/index.html', events=events, registered=registered)


@app.route('/events/all')
def events():
    events = Event.get_all_events()
    return jsonify(events)


@app.route('/events/<int:event_id>')
def get_event(event_id):
    event = Event.query.get_or_404(event_id)
    return jsonify(event)


def generate_code(n):
    signs = 'QWERTYUIOPLKJHGFDSAZXCVBNMqwertyuioplkjhgfdsazxcvbnm1234567890'
    code = ''
    for i in range(n):
        code = code + (random.choice(signs))
    return code


@app.route('/registration/add', methods=['POST'])
def add_registration():
    if request.method == 'POST':
        fullname = request.form.get('fullname')
        event_id = request.form.get('event_id')
        if fullname and event_id:
            manage_code = generate_code(8)
            db.session.add(Registration(event_id, fullname, manage_code))
            db.session.commit()
            flash('You have been successfully registered to the event! Here is your manage code: {}'.format(manage_code))

    return redirect('/')


@app.route('/registrations/all')
def registrations():
    registrations = Registration.get_all_registrations()
    return jsonify(registrations)


@app.route('/registration/<int:registration_id>')
def get_registration(registration_id):
    registration = Registration.query.get_or_404(registration_id)
    return jsonify(registration)


@app.route('/registration/cancel', methods=['POST'])
def delete_registration():
    if request.method == 'POST':
        code = request.form.get('code')
        event_id = request.form.get('event_id')
        registration = Registration.query.filter_by(event_id=event_id).filter_by(manage_code=code).first()
        if registration:
            db.session.delete(registration)
            flash('You have successfully cancelled your registration.')

    db.session.commit()
    return redirect('/')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
