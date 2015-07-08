"""
               #   # ####  ##### #   # ##### #   # #   #
               #  #  #   # #     ## ##  #  # #  ## #   #
               ###   ####  ####  # # #  #  # # # # #####
               #  #  #     #     #   #  #  # ##  # #   #
               #   # #     ##### #   # #   # #   # #   #

                   Kremlin Magical Everything System
               Glasnost Image Board and Boredom Inhibitor

"""
import hashlib, os


from flask import request, session, render_template, flash, url_for, \
        redirect, send_from_directory
from werkzeug import secure_filename
from kremlin import app, db, dbmodel, forms, imgutils, uploaded_images
from pagination import Pagination

@app.route('/')
def home_index():
    """ Display the glasnost logo, attempt to replicate old behavior """
    return render_template('home.html')

@app.route('/images', defaults={'page': 1})
@app.route('/images/page/<int:page>')
def entries_index(page):
    """ Show an index of image thumbnails """
    posts = dbmodel.Post.query.all()
    pagination = Pagination(page, 2, len(posts))
    return render_template('board.html', form=forms.NewPostForm(),
        posts=posts, pagination=pagination)

def url_for_other_page(page):
    args = request.view_args.copy()
    args['page'] = page
    return url_for(request.endpoint, **args)
    app.jinja_env.globals['url_for_other_page'] = url_for_other_page

#def entries_index():
#    """ Show an index of image thumbnails """
#    #FIXME: limit with pagination
#    posts = dbmodel.Post.query.all()
#    return render_template('board.html', form=forms.NewPostForm(),
#        posts=posts)

@app.route('/logs')
def logs_index():
    """ Show irc logs """
    return "Unimplemented"

@app.route('/services')
def services_index():
    return "Unimplemented"


@app.route('/images/<int:post_id>')
def view_post(post_id):
    """ Show post identified by post_id """
    post = dbmodel.Post.query.get_or_404(post_id)
    comments = dbmodel.Comment.query.filter_by(parent_post_id=post_id)
    return render_template('post.html', post=post, comments=comments)

@app.route('/images/get/<filename>')
def send_file(filename):
    """Send image file to browser"""
    return send_from_directory(app.config['UPLOADED_IMAGES_DEST'],
        filename)

@app.route('/images/add/', methods=['POST'])
def add_image():
    """ Add a new image """

    form = forms.NewPostForm()

    if form.validate_on_submit():
        filename = secure_filename(form.upload.file.filename)
        fileext = os.path.splitext(filename)[1]
        filedata = form.upload.file.stream.read()

        # Calculate SHA1 checksum
        h = hashlib.new('sha1')
        h.update(filedata)
        filehash = h.hexdigest()

        # Validate file uniqueness
        dupe = dbmodel.Image.query.filter_by(sha1sum=filehash).first()

        if dupe:
            flash("Image already exists: %s" % (dupe))
            return redirect(url_for('entries_index'))
        else:
            # File is unique, proceed to create post and image.
            # Save file to filesystem

            # Rewind file, it was read() by the SHA1 checksum
            # routine
            form.upload.file.seek(0)

            # Proceed with storage
            try:
                uploaded_images.save(storage=form.upload.file,
                                     name=''.join([filehash, '.']),
                                    )

                # FIXME: generate thumbnail in a safer way.
                # This is fairly horrible and I'm sorry.
                imagepath = uploaded_images.path(''.join([filehash, fileext]))
                imgutils.mkthumb(imagepath)
            except IOError:
                flash("Oh god a terrible error occured while saving %s" %
                    (filename))
            else:
                dbimage = dbmodel.Image(filename, filehash)
                db.session.add(dbimage)

                user = None

                if "uid" in session:
                    user = dbmodel.User.query.filter_by(
                            id=session['uid']
                        ).first()

                note = form.note.data

                #TODO: Implement tags.

                # Create a new post with the image
                post = dbmodel.Post(image=dbimage, title=filename,\
                        note=note, user=user)
                db.session.add(post)

                # Commit database transaction
                db.session.commit()
                flash("Image successfully posted!")

        return redirect(url_for('entries_index'))
    else:
        flash("Your form has terrible errors in it.")
        return(redirect(url_for("entries_index")))


@app.route('/login', methods=['GET','POST'])
def login():
    """ Login to imageboard """

    form = forms.LoginForm(request.form)
    errtxt = "Invalid username or password, please try again."

    if request.method == 'POST' and form.validate_on_submit():
        user = dbmodel.User.query.filter_by(name=form.username.data).first()
        if user is None:
            flash(errtxt)
            return redirect(url_for('login'))
        else:
            if user.check_password(form.password.data):
                session['logged_in'] = True
                flash("Hello, %s, you have been logged in." % user.name)
                return redirect(url_for('home_index'))
            else:
                flash(errtxt)
                return redirect(url_for('login'))

    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    """ Logout of imageboard """
    session.pop('logged_in', None)
    flash('Logged out of Kremlin.')
    return redirect(url_for('home_index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    """ Register a new user """
    error = None

    form = forms.RegisterForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        # FIXME: Use sqlalchemy.exc.IntegrityError, let the database
        # handle it instead of writing our own shitty test?
        dupe = dbmodel.User.query.filter_by(name=form.username.data).first()
        if dupe:
            flash("Username %s is already taken." % form.username.data)
            return redirect(url_for('register'))
        else:
            user = dbmodel.User(form.username.data, form.email.data,
                form.password.data)
            db.session.add(user)
            db.session.commit()
            flash("Registration complete! Please login.")
            return redirect(url_for('login'))
    else:
        return render_template('register.html', form=form)

@app.route('/about')
def about():
    return "Kremlin Everything System and Boredom Inhibitor v 0.0.0-None"


