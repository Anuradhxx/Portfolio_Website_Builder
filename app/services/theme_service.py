from sqlalchemy.orm import Session
from app.models.theme import Theme

def get_or_create_theme(db: Session, user_id: int) -> Theme:
    theme = db.query(Theme).filter(Theme.user_id == user_id).first()
    if not theme:
        theme = Theme(user_id=user_id)
        db.add(theme)
        db.commit()
        db.refresh(theme)
    return theme


def update_theme(db: Session, user_id: int, data):
    theme = get_or_create_theme(db, user_id)
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(theme, key, value)
    db.commit()
    db.refresh(theme)
    return theme
