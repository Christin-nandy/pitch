from flask import render_template, request, redirect, url_for, abort  
from . import main 
from .forms import CommentsForm, UpdateProfile, PitchForm, UpvoteForm

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to one of the best pitching in the entire world'

    search_pitch = request.args.get('pitch_query')
    pitches= Pitch.get_all_pitches()  

    return render_template('index.html', title = title, pitches= pitches)

@main.route('/select_lines/pitches/')
def select_line():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Select Lines'

    pitches= Pitch.get_all_pitches()

    return render_template('select_lines.html', title = title, pitches= pitches)

@main.route('/promotion/pitches/')
def promotion():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Promotion Pitches'

    pitches= Pitch.get_all_pitches()

    return render_template('promotion.html', title = title, pitches= pitches)

@main.route('/product/pitches/')
def product():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Product Pitches'
    pitches= Pitch.get_all_pitches()
    return render_template('product.html', title = title, pitches= pitches)

#  end of category root functions

@main.route('/pitch/<int:pitch_id>')
def pitch(pitch_id):

    '''
    View pitch page function that returns the pitch details page and its data
    '''
    found_pitch= get_pitch(pitch_id)
    title = pitch_id
    pitch_comments = Comment.get_comments(pitch_id)

    return render_template('pitch.html',title= title ,found_pitch= found_pitch, pitch_comments= pitch_comments)

@main.route('/search/<pitch_name>')
def search(pitch_name):
    '''
    View function to display the search results
    '''
    searched_pitches = search_pitch(pitch_name)
    title = f'search results for {pitch_name}'

    return render_template('search.html',pitches = searched_pitches)

     



