from db.models import Student


def test_create_student(db_session):
    # 1. создаём студента
    student = Student(email="test_student@example.com")
    db_session.add(student)
    db_session.commit()

    # 2. проверяем, что студент появился в БД
    saved_student = (
        db_session.query(Student).filter_by(email="test_student@example.com").one()
    )

    assert saved_student.email == "test_student@example.com"
    assert saved_student.deleted_at is None


def test_update_student_email(db_session):
    # 1. создаём студента
    student = Student(email="old_email@example.com")
    db_session.add(student)
    db_session.commit()

    # 2. меняем email
    student.email = "new_email@example.com"
    db_session.commit()

    # 3. проверяем, что email обновился
    updated_student = db_session.query(Student).filter_by(id=student.id).one()

    assert updated_student.email == "new_email@example.com"


def test_soft_delete_student(db_session):
    # 1. создаём студента
    student = Student(email="delete_me@example.com")
    db_session.add(student)
    db_session.commit()

    # 2. мягко удаляем
    student.soft_delete()
    db_session.commit()

    # 3. проверяем, что студент помечен как удалённый
    deleted_student = db_session.query(Student).filter_by(id=student.id).one()

    assert deleted_student.deleted_at is not None
