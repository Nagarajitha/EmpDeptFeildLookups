from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from django.db.models import Q
# Create your views here.

def insert_dept(request):

    DEPTNO = int(input('Enter DEPTNO : '))

    DNAME = input('Enter DNAME : ')

    LOC = input('Enter LOC : ')

    QLDO= Dept.objects.get_or_create(DEPTNO=DEPTNO , DNAME =DNAME ,LOC=LOC)[0]
    QLDO.save()


    d={'QLDO':Dept.objects.all()}
    return render(request,'display_dept.html',d)


def insert_emp(request):

    DEPTNO = int(input('Enter DEPTNO : '))#foreign key

    DO =Dept.objects.filter(DEPTNO=DEPTNO)
    if DO : 
        EMPNO = int(input('Enter EMPNO : ')) #pk
        ENAME = input('Enter ENAME : ')
        JOB = input('Enter JOB : ')
        MGR = input('Enter MGR : ')

        if MGR:
            MEO=Emp.objects.get(EMPNO=int(MGR))
        else:
            MEO=None

            #MGR =int(input('Enter MGR : ')) #object 

        HIREDATE = input('Enter HIREDATE : ')
        SAL = int(input('Enter SAL : '))
        COMM = input('Enter COMM :')
        if COMM :
            COMM = int(COMM)
        else:
            COMM=None
        QLEO= Emp.objects.get_or_create(EMPNO=EMPNO , ENAME = ENAME , JOB = JOB , MGR=MEO , HIREDATE = HIREDATE,SAL=SAL,COMM =COMM , DEPTNO=DO[0])[0]
        QLEO.save()
        d={'QLEO':Emp.objects.all()}
        return render(request,'display_emp.html',d)
    else:
        return HttpResponse('Given DEPTNO is Not present in My Parent Table DEPT')



def insert_salgrade(request):
    GRADE = int(input('Enter GRADE : ') )           
    LOSAL = int(input('Enter LOSAL : '))              
    HISAL  =int(input('Enter HISAL : '))             


    QLSO= Salgrade.objects.get_or_create(GRADE=GRADE , LOSAL=LOSAL , HISAL=HISAL)[0]
    QLSO.save()

    d={'QLSO':Salgrade.objects.all()}
    return render(request,'display_salgrade.html',d)


def display_dept(request):
    #query to fetch dname starts with 'r'
    QLDO = Dept.objects.filter(DNAME__startswith ='r')

    #query to fetch LOC starts with 'd'
    QLDO = Dept.objects.filter(LOC__startswith ='d')

    #query to fetch dno in 10 or 20
    QLDO = Dept.objects.filter(DEPTNO__in =(10,20))

    #query to fetch dname not starts with 'r'
    QLDO = Dept.objects.exclude(DNAME__startswith='r')

    #query to fetch dname contains 's' in it
    QLDO = Dept.objects.filter(DNAME__contains='s')

    #query to fetch dname contains 't' in it
    QLDO = Dept.objects.filter(DNAME__contains='t')

    #query to fetch where loc is BOSTON
    QLDO = Dept.objects.filter(LOC='BOSTON')

    #query to fetch where loc is BOSTON or CHICAGO
    QLDO = Dept.objects.filter(Q(LOC ='CHICAGO') | Q(LOC ='BOSTON'))

    #Query to fetch departments located in 'Dallas' and with department names containing 'Research'
    QLDO = Dept.objects.filter(Q(LOC ='DALLAS') & Q(DNAME__contains ='RESEARCH'))

    #Query to get departments located in 'New York' or 'Boston' and with department names starting with 'S'
    QLDO = Dept.objects.filter(Q(LOC ='NEW YORK') | Q(LOC ='BOSTON') & Q(DNAME__startswith='S'))
    

    d={'QLDO':QLDO}
    return render(request,'display_dept.html',d)



def display_emp(request):
    #query to fetch all employees data
    QLEO = Emp.objects.all()

    #query to fetch ename contains 's' in it
    QLEO = Emp.objects.filter(ENAME__contains='s')


    #query to get employees with job title 'SALESMAN;
    QLEO = Emp.objects.filter(JOB = 'SALESMAN')

    #Query to get employees with a salary greater than 2000
    QLEO = Emp.objects.filter(SAL__gt = 2000)

    #Query to get employees with a salary greater than 2000 and hired after '01-JAN-81':
    QLEO = Emp.objects.filter(SAL__gt = 2000 ,HIREDATE__gt='1981-01-01')

    #Retrieve all clerks who earn more than 800 or analysts with a salary over 2900
    QLEO = Emp.objects.filter(Q(JOB='CLERK',SAL__gt = 800) |Q(JOB='ANALYST',SAL__gt = 2900))

    #Qurery to get  employees who are either managers or analysts 
    QLEO = Emp.objects.filter(Q(JOB='MANAGER')|Q( JOB='ANALYST') )

    #Qurery to get  employees who are either managers or analysts and have been hired before 01-JAN-85
    QLEO = Emp.objects.filter((Q(JOB='MANAGER') | Q(JOB='ANALYST')) & Q(HIREDATE__lt='1985-01-01'))

    # Query to get  all employees in department 30 who either have a commission or earn a salary less than 1600
    QLEO = Emp.objects.filter(Q(DEPTNO=30) & (Q(COMM__isnull=False) | Q(SAL__lt=1600)))

    # Retrieve data for employees hired between Jan -1- 1981, and Dec 31, 1981, with a salary either less than 1500 or greater than 3000
    QLEO = Emp.objects.filter(Q(HIREDATE__range=('1981-01-01', '1981-12-31')) & (Q(SAL__lt=1500) | Q(SAL__gt=3000)))
    

    #QLEO = Emp.objects.all()

    d={'QLEO':QLEO}
    return render(request,'display_emp.html',d)



def display_salgrade(request):
    #query to fetch all salgrade data
    QLSO = Salgrade.objects.all()

    #Retrieve all data for grades where the low salary is less than 1500.
    QLSO = Salgrade.objects.filter(LOSAL__lt = 1500)
    
    #Retrieve all data for grades where the high salary is greater than 3000
    QLSO = Salgrade.objects.filter(HISAL__gt = 3000)

    #Retrieve all data for grades with a  grade range 2-4
    QLSO = Salgrade.objects.filter(GRADE__range =[2,4])
    
    #Retrieve all data for grades with a specific low salary is 1401
    QLSO = Salgrade.objects.filter(LOSAL = 1401)

    #Retrieve all data for grades with a  grade range 2-4 and a high salary greater than 3000.
    QLSO = Salgrade.objects.filter(GRADE__range =(2,4) ,HISAL__gte = 3000)

    #Retrieve all data for grades where the low salary is less than 1500 or the high salary is greater than 4000
    QLSO = Salgrade.objects.filter(Q(LOSAL__lt = 1500 ) | Q(HISAL__gt = 4000))



    #QLSO = Salgrade.objects.all()

    d={'QLSO':QLSO}
    return render(request,'display_salgrade.html',d)

