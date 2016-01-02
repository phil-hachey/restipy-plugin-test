from restipy.plugins.base import InterceptorBase

class RegionExtractor(InterceptorBase):
    def response(self, request, response, ctx):

        response_data = response.json()
        session_data = ctx.obj['SESSION']

        session_data['regionId'] = response_data['result'][0]['id']

        return response
