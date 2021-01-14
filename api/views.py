from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import pandas as pd

@api_view(['GET'])
def endpoint(request):
	df = pd.read_csv('aivo.csv')
	if 'value' not in request.GET:
		return Response(status=status.HTTP_400_BAD_REQUEST)

	if 'indicator' not in request.GET:
		indicator = 'Life satisfaction'
	else:
		indicator = request.GET['indicator']

	value = request.GET['value']

	try:
		value = float(value)
	except Exception as e:
		print(e)
		return Response(status=status.HTTP_400_BAD_REQUEST)		

	res = df[(df['Indicator'] == indicator) & (df['Value'] > float(value))]
	# print(res)
	return Response(res.to_json(), status=status.HTTP_200_OK)