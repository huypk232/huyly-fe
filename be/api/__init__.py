from flask_restx import Api

# from .users import api as users_api
# from .gateway import api as gateway_api
# from .update import api as update_api
# from .listings import api as listings_api
# from .triggers import api as triggers_api
# from .tasks import api as tasks_api
# from .listings_review import api as listings_review_api
# from .admins import api as admins_api
# from .statistic import api as statistic_api
# from .support import api as support_api

from .category import api as category_api

api = Api(
    title='HighFive API',
    version='1.0',
    description='A description',
)

api.add_namespace(category_api)
# api.add_namespace(gateway_api)
# api.add_namespace(listings_api)
# api.add_namespace(update_api)
# api.add_namespace(triggers_api)
# api.add_namespace(tasks_api)
# api.add_namespace(listings_review_api)
# api.add_namespace(admins_api)
# api.add_namespace(statistic_api)
# api.add_namespace(support_api)
