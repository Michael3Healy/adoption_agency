from flask import Flask, request, render_template,  redirect, flash, session
from pdb import set_trace
from flask_debugtoolbar import DebugToolbarExtension
from models import db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_agency'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)
app.app_context().push()
db.init_app(app)

@app.route('/')
def homepage():
    '''Lists all pets'''
    pets = db.session.query(Pet).all()
    return render_template('home.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    '''Add Pet Form'''
    form = AddPetForm()
    if form.validate_on_submit():
        # name = form.data['name']
        # species = form.data['species']
        # photo_url = form.data['photo_url'] or 'https://tinyurl.com/244z6ece'
        # age = form.data['age']
        # notes = form.data['notes']

        form_data = form.data.copy()
        form_data.pop('csrf_token', None)
        if not form_data['photo_url']:
            form_data['photo_url'] = 'https://tinyurl.com/244z6ece'
        new_pet = Pet(**form_data)
        db.session.add(new_pet)    # pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('add_pet.html', form=form)

@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def edit_pet(pet_id):
    '''Shows pet details and has form for editing photo, notes, and availability'''
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.data['photo_url'] or 'https://tinyurl.com/244z6ece'
        pet.notes = form.data['notes']
        pet.available = form.data['available']
        db.session.commit()
        return redirect(f'/{pet_id}')
    else:
        return render_template('pet_details.html', pet=pet, form=form)
