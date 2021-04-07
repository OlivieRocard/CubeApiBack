# coding: utf-8
from sqlalchemy import Column, Date, Enum, ForeignKey, String
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'users'

    id_user = Column(INTEGER(11), primary_key=True)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    password_user = Column(String(100), nullable=False)
    mail_user = Column(String(100), nullable=False)
    zip_code_user = Column(String(5), nullable=False)
    pseudo_user = Column(String(50), nullable=False)
    birthdate_user = Column(Date, nullable=False)
    created_at_user = Column(Date, nullable=False)
    updated_at_user = Column(Date)
    deleted_at_user = Column(Date)
    id_roles = Column(ForeignKey('roles.id_roles', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)

    role = relationship('Role')
    consulter = relationship('Consulter', primaryjoin='Consulter.id_user==User.id_user', lazy='joined')



class Category(Base):
    __tablename__ = 'categories'

    id_cat = Column(INTEGER(11), primary_key=True)
    label_cat = Column(String(100), nullable=False)

    #caracterise = relationship('Ressource', primaryjoin='Category.id_cat==Caracterise.id_cat', viewonly=True)


class Relation(Base):
    __tablename__ = 'relations'

    id_rel = Column(INTEGER(11), primary_key=True)
    label_rel = Column(String(100), nullable=False)

    #est_valable = relationship('Ressource', primaryjoin='Relation.id_rel==EstValable.id_rel')


class Role(Base):
    __tablename__ = 'roles'

    id_roles = Column(INTEGER(11), primary_key=True)
    label_role = Column(String(100), nullable=False)


class TypeRessource(Base):
    __tablename__ = 'type_ressources'

    id_type_res = Column(INTEGER(11), primary_key=True)
    label_type_res = Column(String(100), nullable=False)


class Ressource(Base):
    __tablename__ = 'ressources'

    id_res = Column(INTEGER(11), primary_key=True)
    title_res = Column(String(100), nullable=False)
    status_res = Column(Enum('Validated', 'Refused', 'Pending'))
    acces_res = Column(TINYINT(1))
    created_at_res = Column(Date, nullable=False)
    content_res = Column(String(255))
    source_res = Column(String(50), nullable=False)
    updated_at_res = Column(Date)
    deleted_at_res = Column(Date)
    difficulty = Column(Enum('1', '2', '3'))
    id_user = Column(ForeignKey('users.id_user', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    id_type_res = Column(ForeignKey('type_ressources.id_type_res', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)

    type_ressource = relationship('TypeRessource')
    user = relationship('User')
    caracterise = relationship('Caracterise', primaryjoin='Ressource.id_res==Caracterise.id_res', lazy='joined')
    valable = relationship('EstValable', primaryjoin='Ressource.id_res==EstValable.id_res', lazy='joined')
    consulter = relationship('Consulter', primaryjoin='Consulter.id_res==Ressource.id_res', lazy='joined')


class Token(Base):
    __tablename__ = 'tokens'

    id_tokens = Column(INTEGER(11), primary_key=True)
    created_at = Column(Date, nullable=False)
    deleted_at = Column(Date)
    updated_at = Column(Date)
    id_user = Column(ForeignKey('users.id_user', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)

    user = relationship('User')


class Caracterise(Base):
    __tablename__ = 'caracterise'

    id_res = Column(ForeignKey('ressources.id_res', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
    id_cat = Column(ForeignKey('categories.id_cat', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False, index=True)

    categorie = relationship('Category', lazy='joined')
    ressource = relationship('Ressource', lazy='joined')


class Commentaire(Base):
    __tablename__ = 'commentaires'

    id_com = Column(INTEGER(11), primary_key=True)
    content_com = Column(String(255), nullable=False)
    status_com = Column(Enum('Validated', 'Refused', 'Pending'))
    created_at_com = Column(Date, nullable=False)
    updated_at_com = Column(Date)
    deleted_at_com = Column(Date)
    id_res = Column(ForeignKey('ressources.id_res', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    id_user = Column(ForeignKey('users.id_user', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)

    ressource = relationship('Ressource')
    user = relationship('User')


class Consulter(Base):
    __tablename__ = 'consulter'

    id_cons = Column(INTEGER(11), primary_key=True)
    id_res = Column(ForeignKey('ressources.id_res', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    id_user = Column(ForeignKey('users.id_user', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    favorite = Column(TINYINT(1), nullable=False)
    start_date = Column(Date)
    end_date = Column(Date)
    note_user = Column(INTEGER(1))

    ressource = relationship('Ressource', lazy='joined')
    user = relationship('User', lazy='joined')


class EstValable(Base):
    __tablename__ ='est_valable'

    id_res = Column(ForeignKey('ressources.id_res', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
    id_rel = Column(ForeignKey('relations.id_rel', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False, index=True)

    ressource = relationship('Ressource', lazy='joined')
    relation = relationship('Relation', lazy='joined')

