
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST'])
def lambda_function(request):
    request_data = request.data.get('question')
    solution = count_numbers(request_data)

    return Response({'solution': solution})

def count_numbers(number_list):
    question_list = number_list
    solution_list = []
    lista_final = []
    lista_num = [0] * 99

    for i in question_list:
        lista_num[i] += 1

    for elem, num in enumerate(lista_num):
        if num:
            solution_list.append((elem, num))

    final = sorted(solution_list, key=lambda x: (x[1], x[0]), reverse=True)

    for i in final:
        for j in range(i[1]):
            lista_final.append(i[0])

    return lista_final