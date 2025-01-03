from sqlalchemy import select

from fast_zero.models import User


def teste_create_user(session):
    user = User(
        username='geziel',
        email='geziel@gmail.com',
        password='senha123',
    )
    session.add(user)
    session.commit

    result = session.scalar(select(User).where(User.email == 'geziel@gmail.com'))

    assert result.id == 1
