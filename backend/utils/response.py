def success_response(message, data=None, status=200):
    response = {'success': True, 'message': message}
    if data is not None:
        response['data'] = data
        return response, status
    
    def error_response(message, status=400):
        return{'success': False, 'message': message}, status