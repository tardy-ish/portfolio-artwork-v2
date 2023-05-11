from app import app, artwork,db
import json
with app.app_context():
    paintings = json.load(open('./static/assets/paintings.json',encoding='utf-8'))
    for painting in paintings:
        db.session.add(artwork(**painting))
    db.session.commit()