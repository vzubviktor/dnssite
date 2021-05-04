from django.shortcuts import render
from django.http import HttpResponse 



def index(request):
	return render(request, 'index.html')


def compute(request):

	val1= request.POST['domains']
	val2= request.POST['records']
	domain_list=val1.split(', ')
	

	def get_records(domain):
		import dns.resolver
		final_answers=[]

		try:
			answers=dns.resolver.resolve(domain, val2)
			for value in answers:
				final_answers.append(value.to_text())			
		except Exception as e:
			final_answers.append(e)
		return final_answers

	res = [get_records(i) for i in domain_list]
	output = dict(zip(domain_list, res)) 


	return render(request, 'result.html', { 'val2' : val2,  'output' : output })
# Create your views here.

def csrf_failure(request, reason=""):
	return render(request, 'csrf_failure.html')