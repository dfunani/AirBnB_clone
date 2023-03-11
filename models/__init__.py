from models.engine.file_storage import FileStorage
import importlib

storage = FileStorage()
storage.reload()

class Modules:
    __base_model = importlib.import_module('.base_model', package='models')
    __user = importlib.import_module('.user', package='models')
    __place = importlib.import_module('.place', package='models')
    __state = importlib.import_module('.state', package='models')
    __city = importlib.import_module('.city', package='models')
    __amenity = importlib.import_module('.amenity', package='models')
    __review = importlib.import_module('.review', package='models')


    def factory(self):
        return {
            "BaseModel": Modules.__base_model.BaseModel,
            "User": Modules.__user.User,
            "Place": Modules.__place.Place,
            "State": Modules.__state.State,
            "City": Modules.__city.City,
            "Amenity": Modules.__amenity.Amenity,
            "Review": Modules.__review.Review
    }

CLASSES = Modules().factory()
FileStorage.CLASSES = CLASSES
