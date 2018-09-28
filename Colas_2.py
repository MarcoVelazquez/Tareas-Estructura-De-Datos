
def New_Cola():
	Cola = [0,0,0,0,0]
	i = 4
	return Cola,i

def Pop(Cola_,i):
	del(Cola_[4])
	i += 1
	return Cola_, i

def Push(Cola_,item,i):
	if i == 4:
		Cola_[i] = item
		i -= 1
		
	elif i == 3:
		Cola_[i] = item
		i -= 1
	elif i == 2:
		Cola_[i] = item
		i -= 1
	elif i == 1:
		Cola_[i] = item
		i -= 1
	elif i == 0:
		Cola_[i] = item
		i -= 1
	elif i < 0:
		Cola_[4] = Cola_[3]
		Cola_[3] = Cola_[2]
		Cola_[2] = Cola_[1]
		Cola_[1] = Cola_[0]
		Cola_[0] = item
		

	return Cola_,i

Cola_,i = New_Cola()
print(Cola_)
print
Cola_,i = Push(Cola_,1,i)
print(Cola_)
print
Cola_,i = Push(Cola_,2,i)
print(Cola_)
print
Cola_,i = Push(Cola_,3,i)
print(Cola_)
print
Cola_,i = Push(Cola_,4,i)
print(Cola_)
print
Cola_,i = Push(Cola_,5,i)
print(Cola_)
print
Cola_,i = Push(Cola_,6,i)
print(Cola_)




	



