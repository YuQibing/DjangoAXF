from django.utils.deprecation import MiddlewareMixin


class ProcessResponse(MiddlewareMixin):

    def process_response(self, request, response):

        print('middleware')
        response['Access-Control-Allow-Origin'] = '*'
        return response
