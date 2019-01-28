from . import db
from models.dictionary import Dictionary


def get_all(model):
    data = model.query.all()
    return data


def add_instance(model, **kwargs):
    instance = model(**kwargs)
    db.session.add(instance)
    commit_changes()
    return instance


def get_instance(model, id):
    data = model.query.get(id)
    return data


def delete_instance(model, id):
    model.query.filter_by(id=id).delete()
    commit_changes()


def edit_instance(model, id, **kwargs):
    instance = model.query.filter_by(id=id).all()[0]
    for attr, new_value in kwargs:
        setattr(instance, attr, new_value)
    commit_changes()


def commit_changes():
    db.session.commit()


def get_social_status(social_status_id):
    return Dictionary.query.filter_by(category='social_status_id', int_id=social_status_id).first()


def get_gender(gender_id):
    return Dictionary.query.filter_by(category='gender', str_id=gender_id).first()


def get_full_client_data(client):
    soc_status = get_social_status(client.social_status_id)
    gender = get_gender(client.gender)
    client_data = client.to_dict()
    client_data.update({'social_status': soc_status.value,
                        'gender_id': client_data['gender'],
                        'gender': gender.value})
    return client_data
