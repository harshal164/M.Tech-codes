
d = 256
def rabin_karp(pattern, txt, q):
	M = len(pattern)
	N = len(txt)
	i = 0
	j = 0
	p = 0
	t = 0
	h = 1
	for i in range(M-1):
		h = (h*d)%q

	for i in range(M):
		p = (d*p + ord(pattern[i]))%q
		t = (d*t + ord(txt[i]))%q


	for i in range(N-M+1):

		if p==t:

			for j in range(M):
				if txt[i+j] != pattern[j]:
					break

			j+=1

			if j==M:
				print ("pattern found at index " + str(i))


		if i < N-M:
			t = (d*(t-ord(txt[i])*h) + ord(txt[i+M]))%q


			if t < 0:
				t = t+q



txt=input("enter any string ")
pattern=input("enter any pattern")
q = 103 # A prime number
rabin_karp(pattern,txt,q)


