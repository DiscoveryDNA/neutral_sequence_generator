from Neutral_Sequence_Generator import sequence_generator

def control_generator(probability_range):
	probability_range+=1
	for i in range(1,probability_range):
		for j in range(1,probability_range):
			for k in range(1,probability_range):
				for l in range(1,probability_range):
					freq = [i/1000,j/1000,k/1000,l/1000]
					filename = "control_seqs/freq" +str(i)+str(j)+str(k)+str(l)+'.fa'
					sequence_generator(1000,freq,24,filename=filename)

control_generator(10)
