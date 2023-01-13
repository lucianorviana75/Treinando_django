
# vews.py
import datetime

def home (request):
    data={}
    data ['Transações'] =['t1','t2','t3']

    data['now']= datetime.datetime.now()
    #html = "<html><body>It is now %s.</body></html>" %now
    return render(request,'conta/home.html',data )

def listagem (request):
    data={}
    data ['Transações'] = Transação.objects.all()    
    return render(request,'conta/listagem.html',data)
