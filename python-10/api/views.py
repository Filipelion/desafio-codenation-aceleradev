
from collections import Counter
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST'])
def lambda_function(request):
    request_data = request.data.get('question')
    solution = count_numbers(request_data)

    return Response({'solution': solution})

def count_numbers(number_list):
    solution_list = []
    counter = Counter()

    for i in number_list:
        counter[i] += 1


    for i in counter.most_common():
        for j in range(i[1]):
            solution_list.append(i[0])

    return solution_list