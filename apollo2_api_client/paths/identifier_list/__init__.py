# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from apollo2_api_client.paths.identifier_list import Api

from apollo2_api_client.paths import PathValues

path = PathValues.IDENTIFIER_LIST