from os.path import join, dirname, realpath
class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///shop.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'shop/static/img/product/')