from .models import words
def seed_test(db,app):

    with app.app_context():
        db.drop_all()
        db.create_all()

        w1 = words.Words(
            kanji="test kanji",
            phonetics="test phonetic",
            pronunciation="test prounciation",
            english="test english",
            spanish="test spanish",
            is_katakana=False
        )

        db.session.add_all([w1])

        db.session.commit()