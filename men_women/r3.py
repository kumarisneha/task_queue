from r1 import check,time
import r2

print "Please check either the person is men or women(m/w)"
s = raw_input()
if(s== 'm'):    
    result = r2.q1.enqueue(check, s)
else:
    result = r2.q2.enqueue(check, s)
   
