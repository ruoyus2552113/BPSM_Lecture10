#!/usr/bin/python3
#step1
my_dna="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
A_count=my_dna.count('A')
T_count=my_dna.count('T')
len_dna=len(my_dna)
at_count=(A_count + T_count)/len_dna
print("A+T content is" + str(at_count))

#final-1
my_dna="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
at_count=(my_dna.count('A')+my_dna.count('T'))/len(my_dna)
print("A+T content is",str(int(100*at_count)),"percent")

#step2
my_dna="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
replace_A=my_dna.replace('A','t')
print(replace_A)
replace_G=replace_A.replace('G','c')
print(replace_G)
replace_T=replace_G.replace('T','a')
print(replace_T)
replace_C=replace_T.replace('C','g')
print(replace_C)
print("complementing DNA is" + str(replace_C.upper()))

#final-2
my_dna="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
print("The complementing sequence is",my_dna.replace('A','t').replace('T','a').replace('G','c').replace('C','g').upper())

#step3
#3.1 find the position of the motif in the sequence
my_dna="ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
motif="AATTC"
position=my_dna.find(motif)
#3.2 use that to figure out the position of the cut
print(f"The position of the cut is {position}")
#3.3 calculate the length of the second fragment based on the cut position
print(f"The second fragment based on the cut position is {len(my_dna)-position}")

#step4
#4.1.1 extract the first and second exon based on the coordinates and store these as variables
my_dna="ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
exon_1=my_dna[0:63]
exon_2=my_dna[90:]
#4.1.2 join together the two exons to make the coding sequence
print(f"The coding sequence is {exon_1+exon_2}")
#4.2.1 figure out the length of the coding sequence
exon=exon_1+exon_2
print("The length of the first exon is",len(exon))
#percentage of the DNA sequence coding
#4.2.2 divide by the length of the original sequence and multiply by 100
percentage=len(exon)/len(my_dna)*100
print(f"The percentage of the DNA sequence is {int(percentage)}")
#4.3.1 store the exons and intron separately as variables
intron=my_dna[63:90]
#4.3.2 convert the intron to lower case
intron_low=intron.lower()
#4.3.3 concatenate the exons and intron to make one long sequence
print("My present DNA is ",exon_1+intron_low+exon_2)


