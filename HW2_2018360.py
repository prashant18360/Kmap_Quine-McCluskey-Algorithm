# CSE 101 - IP HW2
# K-Map Minimization
# Name : PRASHANT
# Roll Number : 2018360
# Section : B
# Group : 1
# Date : October 12, 2018

def minFunc(numVar, stringIn):
        # conditon checking no. of variable
        # Here in this condition minimization of 4 variable k-map
        if(numVar==4):
                '''function to convert a list into dictionary
                        in which the L variable has list and
                        dic variable contain a dictionary'''
                def list_dict(L):
                        dic={}
                        for i in range(len(L)):
                                dc=0
                                for j in range(4):
                                        dc=int(L[i][j])*2**(3-j)+dc
                                dcs=str(dc)
                                dic[dcs]=L[i]
                        return(dic)

                #input string stored in dec variable
                dec=stringIn
                l=len(dec)
                a=dec.find('d')

                #string slicing of 1st bracket number
                A=[]; b=0; c=0
                for i in range(0,dec[:a].count(',')+1):
                        if(i==dec[:a].count(',')):
                                b=dec.find(')',b+1)
                                A.append(int(dec[c+1:b]))
                        else:
                                b=dec.find(',',b+1)
                                A.append(int(dec[c+1:b]))
                                c=b
                B=list(A)
                B.sort()

                #string slicing of 2nd bracket number if the don't care condition exist
                if(dec[a+1]=='('):
                        dec1=dec[a+1:]
                        b=0; c=0
                        for j in range(0,dec1.count(',')+1):
                                if(j==dec1.count(',')):
                                        b=dec1.find(')',b+1)
                                        A.append(int(dec1[c+1:b]))
                                else:
                                        b=dec1.find(',',b+1)
                                        A.append(int(dec1[c+1:b]))
                                        c=b
                A.sort()

                '''Funtion to determine the binary number
                        of corresponding decimal number in its t passes the binary number'''
                def dec_bin(n):
                        t=''
                        if(n==0):
                                t='0000'
                        else:
                                while n>0 :
                                        d=n%2
                                        n=n//2
                                        t=str(d)+t
                                if(len(t)==3):
                                        t='0'+t
                                elif(len(t)==2):
                                        t='00'+t
                                elif(len(t)==1):
                                        t='000'+t
                        return(t)

                #Calling of the function dec_bin to find binary of the list of number A and append all binary number into list s1 
                s1=[]
                for k in range(len(A)):
                        n1=A[k]
                        s1.append(dec_bin(n1))

                '''step 1 is started
                        in which binary number is grouped according to the
                        occurance of 1 in binary number and it convert
                        into multiple list like s1_gp1, s1_gp2, s1_gp3, s1_gp4, and s1_gp5'''
                s1_gp1=[]; s1_gp2=[]; s1_gp3=[]; s1_gp4=[]; s1_gp5=[]
                for i in range(len(s1)):
                        if(s1[i].count('1')==0):
                                s1_gp1.append(s1[i])
                        elif(s1[i].count('1')==1):
                                s1_gp2.append(s1[i])
                        elif(s1[i].count('1')==2):
                                s1_gp3.append(s1[i])
                        elif(s1[i].count('1')==3):
                                s1_gp4.append(s1[i])
                        else:
                                s1_gp5.append(s1[i])

                #To append the group(multiple list) s1_gp1 to s1_gp5 into the list s1_gp and it become list of sub-list
                s1_gp=[]
                s1_gp.append(s1_gp1); s1_gp.append(s1_gp2); s1_gp.append(s1_gp3); s1_gp.append(s1_gp4); s1_gp.append(s1_gp5)

                '''step 2 is started
                        in which the group of step 1 sub-list's element,combining from the
                        nth sublist to the (n+1)th sublist according to bit changing in the
                        two binary number (only bit change to be considered into the grouping)
                        and we will get list (s2_g) in every steps and s2_g append into
                        s2_gp after every sublist changing of step 1 and s2_gp becomes the list of sublist
                        and also the decimal number to be group with the corresponding binary number's decimal number into dk2_gp'''        
                s2_gp=[]; dk2_gp=[]
                for i in range(len(s1_gp)-1):
                        s2_g=[]; dk2=[]
                        for j in range(len(s1_gp[i])):
                                for k in range(len(s1_gp[i+1])):
                                        f=0; h=-1
                                        for m in range(4):
                                                if(s1_gp[i][j][m]==s1_gp[i+1][k][m]):
                                                        f=f+1
                                                else:
                                                        h=m
                                        if(f==3 and h>=0):
                                                X=[]; X.append(s1_gp[i][j]); X.append(s1_gp[i+1][k])
                                                #print(X)
                                                Y=list_dict(X)
                                                ky=Y.keys()
                                                for t in ky:
                                                        dk2.append(t)
                                                s=s1_gp[i][j]
                                                ty=s[:h]+'_'+s[h+1:]
                                                s2_g.append(ty)
                        s2_gp.append(s2_g)
                        dk2_gp.append(dk2)

                '''step 3 is started
                        in which the group of step 2 sub-list's element,combining from the
                        nth sublist to the (n+1)th sublist according to bit changing in the
                        two binary number (only bit change to be considered into the grouping)
                        and we will get list (s3_g) in every steps and s3_g append into
                        s3_gp after every sublist changing of step 2 and s3_gp becomes the list of sublist
                        and also the decimal number to be group with the corresponding binary number's decimal number into dk3_gp'''
                s3_gp=[]; dk3_gp=[]
                #print(s2_gp,dk2_gp)
                for i in range(len(s2_gp)-1):
                        s3_g=[]; dk3=[]
                        for j in range(len(s2_gp[i])):
                                for k in range(len(s2_gp[i+1])):
                                        f=0; h=-1
                                        for m in range(4):
                                                if(s2_gp[i][j][m]==s2_gp[i+1][k][m]):
                                                        f=f+1
                                                else:
                                                        h=m
                                        if(f==3 and h>=0):
                                                for w in range(2):
                                                        t1=dk2_gp[i][j*2+w]
                                                        t2=dk2_gp[i+1][k*2+w]
                                                        dk3.append(t1); dk3.append(t2)
                                                s=s2_gp[i][j]
                                                ty=s[:h]+'_'+s[h+1:]
                                                s3_g.append(ty)
                        s3_gp.append(s3_g)
                        dk3_gp.append(dk3)

                '''step 4 is started
                        in which the group of step 3 sub-list's element,combining from the
                        nth sublist to the (n+1)th sublist according to bit changing in the
                        two binary number (only bit change to be considered into the grouping)
                        and we will get list (s4_g) in every steps and s4_g append into
                        s4_gp after every sublist changing of step 3 and s4_gp becomes the list of sublist
                        and also the decimal number to be group with the corresponding binary number's decimal number into dk4_gp'''
                s4_gp=[]; dk4_gp=[]
                #print(s3_gp,dk3_gp)
                for i in range(len(s3_gp)-1):
                        s4_g=[]; dk4=[]
                        for j in range(len(s3_gp[i])):
                                for k in range(len(s3_gp[i+1])):
                                        f=0; h=-1
                                        for m in range(4):
                                                if(s3_gp[i][j][m]==s3_gp[i+1][k][m]):
                                                        f=f+1
                                                else:
                                                        h=m
                                        if(f==3 and h>=0):
                                                for w in range(4):
                                                        t1=dk3_gp[i][j*4+w]
                                                        t2=dk3_gp[i+1][k*4+w]
                                                        dk4.append(t1); dk4.append(t2)
                                                s=s3_gp[i][j]
                                                ty=s[:h]+'_'+s[h+1:]
                                                s4_g.append(ty)
                        s4_gp.append(s4_g)
                        dk4_gp.append(dk4)

                #checking of s4_gp list has its non-empty sublist or not ,if it is yes
                #then get the grouped binary into bin1 and grouped decimal number into num
                #then check binary number bit if it has 0 then stored the boolean variable Y1 with its not(') symbol
                #if it has 1 then stored the variable without any symbol and we can say it is prime implicant
                Y1=''
                #print(s4_gp,dk4_gp)
                num=[]; bin1=[]
                if(len(s4_gp[0])>0 or len(s4_gp[1])>0):
                        if(len(s4_gp[0])>0):
                                bin1=s4_gp[0][0]; num=dk4_gp[0][:8]
                        if(len(s4_gp[1])>0):
                                bin1=s4_gp[1][0]; num=dk4_gp[1][:8]
                        for t in range(4):
                                if(bin1[t]=='0'):
                                        if(t==0):
                                                Y1="A'"
                                        elif(t==1):
                                                Y1="B'"
                                        elif(t==2):
                                                Y1="C'"
                                        else:
                                                Y1="D'"
                                elif(bin1[t]=='1'):
                                        if(t==0):
                                                Y1="A"
                                        elif(t==1):
                                                Y1="B"
                                        elif(t==2):
                                                Y1="C"
                                        else:
                                                Y1="D"

                #Checking of s3_gp list has its non-empty sublist or not ,if it is yes
                #then excluded the repeating elements from the sub-list of s3_gp and the new list in L
                #and also excluded the repeating corresponding decimal number new list is ld and also in dkm3_gp
                #then excluded the step 4 decimal term(num) which may be present in ld
                #and the new list is Ltl and after that new is L
                Y2=''; L=[]; ld=[]
                if(len(s3_gp[0])>0 or len(s3_gp[1])>0):
                        for p in range(len(s3_gp)):
                                for q in range(len(s3_gp[p])-1):
                                        for r in range(len(s3_gp[p])-1-q):
                                                if(s3_gp[p][q]==s3_gp[p][r+1+q]):
                                                        L.append(s3_gp[p][q])
                                                        ld.append(dk3_gp[p][q*4:q*4+4])
                        #print(L,ld)
                        dkm3_gp=ld
                        if(len(s4_gp[0])>0 or len(s4_gp[1])>0):
                                li=[]; g=[]; tl=[]
                                for m in range(len(ld)):
                                        h=0; xc=[]
                                        for n in range(len(ld[m])):
                                                for u in range(len(num)):
                                                        if(ld[m][n]==num[u]):
                                                                h=h+1
                                                xc.append(h)
                                                if(h==4):
                                                        g.append(m)
                                        c=0
                                        for x in range(4):
                                                if(0<=xc[x]<3):
                                                        c=c+1
                                        if(c==4):
                                                li.append(ld[m])
                                for z in range(len(g)):
                                        tl.append(L[g[z]])
                                Ltl=list(set(L).difference(set(tl)))
                                L=Ltl
                                ld=li
                                dkm3_gp=li

                        #As we check the bit of binary in L,
                        #whether bit is '0' it represent boolean variable with not(') symbol, otherwise it represent boolean variable 
                        La=[]
                        #print(L,ld)
                        for i in range(len(L)):
                                Y2=''
                                for j in range(4):
                                        if(L[i][j]=='0'):
                                                if(j==0):
                                                        Y2=Y2+"A'"
                                                elif(j==1):
                                                        Y2=Y2+"B'"
                                                elif(j==2):
                                                        Y2=Y2+"C'"
                                                else:
                                                        Y2=Y2+"D'"
                                        elif(L[i][j]=='1'):
                                                if(j==0):
                                                        Y2=Y2+"A"
                                                elif(j==1):
                                                        Y2=Y2+"B"
                                                elif(j==2):
                                                        Y2=Y2+"C"
                                                else:
                                                        Y2=Y2+"D"
                                La.append(Y2)

                '''check the sublist of s2_gp is non-empty or not ,if it is yes then checking the dk2_gp element of sublist
                        is present in dk3_gp ,if yes then we excluded the these sublist then we have not included terms in
                        ld2 and sm2_gp and also same process for binary ,so sm2_gp is binary'''
                ld2=[]; sm2_gp=[]
                #print(La)
                if(len(s2_gp[0])>0 or len(s2_gp[1])>0 or len(s2_gp[2])>0):
                        for i in range(len(dk2_gp)):
                                for j in range(len(dk2_gp[i])):
                                        f=0
                                        for k in range(len(dk3_gp)):
                                                for l in range(len(dk3_gp[k])):
                                                        if(dk2_gp[i][j]==dk3_gp[k][l]):
                                                                f=f+1
                                        if(f==0):
                                                if(j%2==0):
                                                        ld2.append(dk2_gp[i][j:j+2])
                                                        sm2_gp.append(s2_gp[i][j//2])
                                                else:
                                                        ld2.append(dk2_gp[i][j-1:j+1])
                                                        sm2_gp.append(s2_gp[i][(j-1)//2])
                        sms2_gp=[]
                        for i in range(len(sm2_gp)-1):
                                for j in range(i+1,len(sm2_gp)):
                                        if(sm2_gp[i]==sm2_gp[j]):
                                                sms2_gp.append(sm2_gp[i])
                        for k in range(len(sms2_gp)):
                                sm2_gp.remove(sms2_gp[k])
                        lds2=[]
                        
                        for i in range(len(ld2)-1):
                                for j in range(i+1,len(ld2)):
                                        if(ld2[i]==ld2[j]):
                                                lds2.append(ld2[i])
                        for k in range(len(lds2)):
                                ld2.remove(lds2[k])
                        La2=[]
                        
                        #As we check the bit of binary in sm2_gp,
                        #whether bit is '0' it represent boolean variable with not(') symbol, otherwise it represent boolean variable 
                        for i in range(len(sm2_gp)):
                                Y3=''
                                for t in range(4):
                                        if(sm2_gp[i][t]=='0'):
                                                if(t==0):
                                                        Y3=Y3+"A'"
                                                elif(t==1):
                                                        Y3=Y3+"B'"
                                                elif(t==2):
                                                        Y3=Y3+"C'"
                                                else:
                                                        Y3=Y3+"D'"
                                        elif(sm2_gp[i][t]=='1'):
                                                if(t==0):
                                                        Y3=Y3+"A"
                                                elif(t==1):
                                                        Y3=Y3+"B"
                                                elif(t==2):
                                                        Y3=Y3+"C"
                                                else:
                                                        Y3=Y3+"D"
                                La2.append(Y3)

                '''looking to the very first list A, A is checking its element which is also present in the dk2_gp
                        so we excluded these terms and the new list is ld3 and similarly,same work its corresponding
                        binary number list and the new list is sm1_gp'''
                ld3=[]
                for i in range(len(A)):
                        a=0
                        for j in range(len(dk2_gp)):
                                for k in range(len(dk2_gp[j])):
                                        if(str(A[i])==dk2_gp[j][k]):
                                                a=a+1
                        if(a==0):
                                ld3.append(A[i])
                sm1_gp=[]
                for p in range(len(ld3)):
                        e1=ld3[p]
                        sm1_gp.append(dec_bin(e1))

                #As we check the bit of binary in sm1_gp,
                #whether bit is '0' it represent boolean variable with not(') symbol, otherwise it represent boolean variable
                La3=[]
                for x in range(len(sm1_gp)):
                        Y4=''
                        for z in range(4):
                                if(sm1_gp[x][z]=='0'):
                                        if(z==0):
                                                Y4=Y4+"A'"
                                        elif(z==1):
                                                Y4=Y4+"B'"
                                        elif(z==2):
                                                Y4=Y4+"C'"
                                        else:
                                                Y4=Y4+"D'"
                                elif(sm1_gp[x][z]=='1'):
                                        if(z==0):
                                                Y4=Y4+"A"
                                        elif(z==1):
                                                Y4=Y4+"B"
                                        elif(z==2):
                                                Y4=Y4+"C"
                                        else:
                                                Y4=Y4+"D"
                        La3.append(Y4)

                '''Below part is determine the Essential prime implicant from the prime implicant'''
                fb=[]; fc=[]; fd=[]; O=[]
                if(len(num)>0):
                        O.append(Y1)
                for i in range(len(B)):
                        n1=0; n2=0
                        if(len(ld)>0):
                                for j in range(len(ld)):
                                        if(ld[j].count(str(B[i]))==1):
                                                n1=n1+1
                                                if(n1==1):
                                                        fb.append(j)
                        if(len(ld2)>0):
                                for k in range(len(ld2)):
                                        if(ld2[k].count(str(B[i]))==1):
                                                n2=n2+1
                                                if(n2==1):
                                                        fc.append(k)
                        if(len(ld3)>0):
                                for m in range(len(ld3)):
                                        if(ld3[m]==B[i]):
                                                fd.append(m)
                        if(n1>1 or n2>1 or n1==0 and n2==0):
                                fb=[]; fc=[]
                        if(n1==1 and n2<1):
                                for h in range(len(fb)):
                                        O.append(La[fb[h]])
                        if(n2==1 and n1<1):
                                for g in range(len(fc)):
                                        O.append(La2[fc[g]])
                        if(len(ld3)>0):
                                for m in range(len(fd)):
                                        O.append(La3[fd[m]])
                outp=list(set(O))
                outp=sorted(outp)
                outpt=''
                for i in range(len(outp)):
                        outpt=outpt+(outp[i])+'+'
                stringOut=outpt[:len(outpt)-1]
                return(stringOut)
        
        '''---------------------------------------------3 VARIABLE K MAP MINIMIZATION-------------------------------------------'''
        #Here the 3 variable k-map minimization implementation
        if(numVar==3):
                '''function to convert a list into dictionary
                        in which the L variable has list and
                        dic variable contain a dictionary'''
                def list_dict2(L):
                        dic={}
                        for i in range(len(L)):
                                dc=0
                                for j in range(3):
                                        dc=int(L[i][j])*2**(2-j)+dc
                                dcs=str(dc)
                                dic[dcs]=L[i]
                        return(dic)

                #input string is stored in dec
                dec=stringIn
                l=len(dec)
                a=dec.find('d')

                #string slicing of 1st bracket number
                A=[]; b=0; c=0
                for i in range(0,dec[:a].count(',')+1):
                        if(i==dec[:a].count(',')):
                                b=dec.find(')',b+1)
                                A.append(int(dec[c+1:b]))
                        else:
                                b=dec.find(',',b+1)
                                A.append(int(dec[c+1:b]))
                                c=b
                B=list(A)
                B.sort()

                #string slicing of 2nd bracket number if the don't care condition exist
                if(dec[a+1]=='('):
                        dec1=dec[a+1:]
                        b=0; c=0
                        for j in range(0,dec1.count(',')+1):
                                if(j==dec1.count(',')):
                                        b=dec1.find(')',b+1)
                                        A.append(int(dec1[c+1:b]))
                                else:
                                        b=dec1.find(',',b+1)
                                        A.append(int(dec1[c+1:b]))
                                        c=b
                A.sort()

                '''Funtion to determine the binary number
                        of corresponding decimal number in its t passes the binary number'''
                def dec_bin2(n):
                        t=''
                        if(n==0):
                                t='000'
                        else:
                                while n>0 :
                                        d=n%2
                                        n=n//2
                                        t=str(d)+t
                                if(len(t)==2):
                                        t='0'+t
                                elif(len(t)==1):
                                        t='00'+t
                        return(t)

                #Calling of the function dec_bin to find binary of the list of number A and append all binary number into list s1 
                s1=[]
                for k in range(len(A)):
                        n1=A[k]
                        s1.append(dec_bin2(n1))

                '''step 1 is started
                        in which binary number is grouped according to the
                        occurance of 1 in binary number and it convert
                        into multiple list like s1_gp1, s1_gp2, s1_gp3 and s1_gp4'''
                s1_gp1=[]; s1_gp2=[]; s1_gp3=[]; s1_gp4=[]; s1_gp5=[]
                for i in range(len(s1)):
                        if(s1[i].count('1')==0):
                                s1_gp1.append(s1[i])
                        elif(s1[i].count('1')==1):
                                s1_gp2.append(s1[i])
                        elif(s1[i].count('1')==2):
                                s1_gp3.append(s1[i])
                        elif(s1[i].count('1')==3):
                                s1_gp4.append(s1[i])

                #To append the group(multiple list) s1_gp1 to s1_gp5 into the list s1_gp and it become list of sub-list
                s1_gp=[]
                s1_gp.append(s1_gp1); s1_gp.append(s1_gp2); s1_gp.append(s1_gp3); s1_gp.append(s1_gp4)

                '''step 2 is started
                        in which the group of step 1 sub-list's element,combining from the
                        nth sublist to the (n+1)th sublist according to bit changing in the
                        two binary number (only bit change to be considered into the grouping)
                        and we will get list (s2_g) in every steps and s2_g append into
                        s2_gp after every sublist changing of step 1 and s2_gp becomes the list of sublist
                        and also the decimal number to be group with the corresponding binary number's decimal number into dk2_gp'''        
                s2_gp=[]; dk2_gp=[]
                for i in range(len(s1_gp)-1):
                        s2_g=[]; dk2=[]
                        for j in range(len(s1_gp[i])):
                                for k in range(len(s1_gp[i+1])):
                                        f=0; h=-1
                                        for m in range(3):
                                                if(s1_gp[i][j][m]==s1_gp[i+1][k][m]):
                                                        f=f+1
                                                else:
                                                        h=m
                                        if(f==2 and h>=0):
                                                X=[]; X.append(s1_gp[i][j]); X.append(s1_gp[i+1][k])
                                                Y=list_dict2(X)
                                                ky=Y.keys()
                                                for t in ky:
                                                        dk2.append(t)
                                                s=s1_gp[i][j]
                                                ty=s[:h]+'_'+s[h+1:]
                                                s2_g.append(ty)
                        s2_gp.append(s2_g)
                        dk2_gp.append(dk2)

                '''step 3 is started
                        in which the group of step 2 sub-list's element,combining from the
                        nth sublist to the (n+1)th sublist according to bit changing in the
                        two binary number (only bit change to be considered into the grouping)
                        and we will get list (s3_g) in every steps and s3_g append into
                        s3_gp after every sublist changing of step 2 and s3_gp becomes the list of sublist
                        and also the decimal number to be group with the corresponding binary number's decimal number into dk3_gp'''
                s3_gp=[]; dk3_gp=[]
                for i in range(len(s2_gp)-1):
                        s3_g=[]; dk3=[]
                        for j in range(len(s2_gp[i])):
                                for k in range(len(s2_gp[i+1])):
                                        f=0; h=-1
                                        for m in range(3):
                                                if(s2_gp[i][j][m]==s2_gp[i+1][k][m]):
                                                        f=f+1
                                                else:
                                                        h=m
                                        if(f==2 and h>=0):
                                                for w in range(2):
                                                        t1=dk2_gp[i][j*2+w]
                                                        t2=dk2_gp[i+1][k*2+w]
                                                        dk3.append(t1); dk3.append(t2)
                                                s=s2_gp[i][j]
                                                ty=s[:h]+'_'+s[h+1:]
                                                s3_g.append(ty)
                        s3_gp.append(s3_g)
                        dk3_gp.append(dk3)

                ld=[]; L=[]; La=[]
                if(len(s3_gp[0])>0 or len(s3_gp[1])>0):
                        for p in range(len(s3_gp)):
                                for q in range(len(s3_gp[p])-1):
                                        for r in range(len(s3_gp[p])-1-q):
                                                if(s3_gp[p][q]==s3_gp[p][r+1+q]):
                                                        L.append(s3_gp[p][q])
                                                        ld.append(dk3_gp[p][q*4:q*4+4])
                        dkm3_gp=ld
                        for t in range(3):
                                if(L[0][t]=='0'):
                                        if(t==0):
                                                Y1="A'"
                                        elif(t==1):
                                                Y1="B'"
                                        elif(t==2):
                                                Y1="C'"
                                elif(L[0][t]=='1'):
                                        if(t==0):
                                                Y1="A"
                                        elif(t==1):
                                                Y1="B"
                                        elif(t==2):
                                                Y1="C"
                        La.append(Y1)

                '''check the sublist of s2_gp is non-empty or not ,if it is yes then checking the dk2_gp element of sublist
                        is present in dk3_gp ,if yes then we excluded the these sublist then we have not included terms in
                        ld2 and sm2_gp and also same process for binary ,so sm2_gp is binary'''
                ld2=[]; sm2_gp=[]
                if(len(s2_gp[0])>0 or len(s2_gp[1])>0 or len(s2_gp[2])>0):
                        for i in range(len(dk2_gp)):
                                for j in range(len(dk2_gp[i])):
                                        f=0
                                        for k in range(len(dk3_gp)):
                                                for l in range(len(dk3_gp[k])):
                                                        if(dk2_gp[i][j]==dk3_gp[k][l]):
                                                                f=f+1
                                        if(f==0):
                                                if(j%2==0):
                                                        ld2.append(dk2_gp[i][j:j+2])
                                                        sm2_gp.append(s2_gp[i][j//2])
                                                else:
                                                        ld2.append(dk2_gp[i][j-1:j+1])
                                                        sm2_gp.append(s2_gp[i][(j-1)//2])
                        sms2_gp=[]
                        for i in range(len(sm2_gp)-1):
                                for j in range(i+1,len(sm2_gp)):
                                        if(sm2_gp[i]==sm2_gp[j]):
                                                sms2_gp.append(sm2_gp[i])
                        for k in range(len(sms2_gp)):
                                sm2_gp.remove(sms2_gp[k])
                        lds2=[]
                        for i in range(len(ld2)-1):
                                for j in range(i+1,len(ld2)):
                                        if(ld2[i]==ld2[j]):
                                                lds2.append(ld2[i])
                        for k in range(len(lds2)):
                                ld2.remove(lds2[k])
                        La2=[]
                        
                        #As we check the bit of binary in sm2_gp,
                        #whether bit is '0' it represent boolean variable with not(') symbol, otherwise it represent boolean variable 
                        for i in range(len(sm2_gp)):
                                Y2=''
                                for t in range(3):
                                        if(sm2_gp[i][t]=='0'):
                                                if(t==0):
                                                        Y2=Y2+"A'"
                                                elif(t==1):
                                                        Y2=Y2+"B'"
                                                elif(t==2):
                                                        Y2=Y2+"C'"
                                        elif(sm2_gp[i][t]=='1'):
                                                if(t==0):
                                                        Y2=Y2+"A"
                                                elif(t==1):
                                                        Y2=Y2+"B"
                                                elif(t==2):
                                                        Y2=Y2+"C"
                                La2.append(Y2)
                '''looking to the very first list A, A is checking its element which is also present in the dk2_gp
                        so we excluded these terms and the new list is ld3 and similarly,same work its corresponding
                        binary number list and the new list is sm1_gp'''
                ld3=[]
                for i in range(len(A)):
                        a=0
                        for j in range(len(dk2_gp)):
                                for k in range(len(dk2_gp[j])):
                                        if(str(A[i])==dk2_gp[j][k]):
                                                a=a+1
                        if(a==0):
                                ld3.append(A[i])
                sm1_gp=[]
                for p in range(len(ld3)):
                        e1=ld3[p]
                        sm1_gp.append(dec_bin2(e1))

                #As we check the bit of binary in sm1_gp,
                #whether bit is '0' it represent boolean variable with not(') symbol, otherwise it represent boolean variable
                La3=[]
                for x in range(len(sm1_gp)):
                        Y3=''
                        for z in range(3):
                                if(sm1_gp[x][z]=='0'):
                                        if(z==0):
                                                Y3=Y3+"A'"
                                        elif(z==1):
                                                Y3=Y3+"B'"
                                        elif(z==2):
                                                Y3=Y3+"C'"
                                elif(sm1_gp[x][z]=='1'):
                                        if(z==0):
                                                Y3=Y3+"A"
                                        elif(z==1):
                                                Y3=Y3+"B"
                                        elif(z==2):
                                                Y3=Y3+"C"
                        La3.append(Y3)

                '''Below part is determine the Essential prime implicant from the prime implicant'''
                fb=[]; fc=[]; fd=[]; O=[]
                for i in range(len(B)):
                        n1=0; n2=0
                        if(len(ld)>0):
                                for j in range(len(ld)):
                                        if(ld[j].count(str(B[i]))==1):
                                                n1=n1+1
                                                if(n1==1):
                                                        fb.append(j)
                        if(len(ld2)>0):
                                for k in range(len(ld2)):
                                        if(ld2[k].count(str(B[i]))==1):
                                                n2=n2+1
                                                if(n2==1):
                                                        fc.append(k)
                        if(len(ld3)>0):
                                for m in range(len(ld3)):
                                        if(ld3[m]==B[i]):
                                                fd.append(m)
                        if(n1>1 or n2>1 or n1==0 and n2==0):
                                fb=[]; fc=[]
                        if(n1==1 and n2<1):
                                for h in range(len(fb)):
                                        O.append(La[fb[h]])
                        if(n2==1 and n1<1):
                                for g in range(len(fc)):
                                        O.append(La2[fc[g]])
                        if(len(ld3)>0):
                                for m in range(len(fd)):
                                        O.append(La3[fd[m]])
                outp=list(set(O))
                outp=sorted(outp)
                outpt=''
                for i in range(len(outp)):
                        outpt=outpt+(outp[i])+'+'
                stringOut=outpt[:len(outpt)-1]
                return(stringOut)

        '''---------------------------------------------2 variable k-map implementation----------------------------------------------------'''
        # 2 variable k-map implementation
        if(numVar==2):
                '''function to convert a list into dictionary
                        in which the L variable has list and
                        dic variable contain a dictionary'''
                def list_dict(L):
                        dic={}
                        for i in range(len(L)):
                                dc=0
                                for j in range(2):
                                        dc=int(L[i][j])*2**(1-j)+dc
                                dcs=str(dc)
                                dic[dcs]=L[i]
                        return(dic)
                #input string stored into dec variable
                dec=stringIn
                a=dec.find('d')

                #string slicing of 1st bracket number
                A=[]; b=0; c=0
                for i in range(0,dec[:a].count(',')+1):
                        if(i==dec[:a].count(',')):
                                b=dec.find(')',b+1)
                                A.append(int(dec[c+1:b]))
                        else:
                                b=dec.find(',',b+1)
                                A.append(int(dec[c+1:b]))
                                c=b
                B=list(A)
                B.sort()
                #string slicing of 2nd bracket number if the don't care condition exist
                if(dec[a+1]=='('):
                        dec1=dec[a+1:]
                        b=0; c=0
                        for j in range(0,dec1.count(',')+1):
                                if(j==dec1.count(',')):
                                        b=dec1.find(')',b+1)
                                        A.append(int(dec1[c+1:b]))
                                else:
                                        b=dec1.find(',',b+1)
                                        A.append(int(dec1[c+1:b]))
                                        c=b
                A.sort()
                
                '''determine the binary number of corresponding decimal number in its t passes the binary number'''
                s1=[]
                for i in range(len(A)):
                        if(A[i]==0):
                                s1.append('00')
                        elif(A[i]==1):
                                s1.append('01')
                        elif(A[i]==2):
                                s1.append('10')
                        else:
                                s1.append('11')

                '''step 1 is started
                        in which binary number is grouped according to the
                        occurance of 1 in binary number and it convert
                        into multiple list like s1_gp1, s1_gp2, s1_gp3'''
                s1_gp1=[]; s1_gp2=[]; s1_gp3=[]
                for i in range(len(s1)):
                        if(s1[i].count('1')==0):
                                s1_gp1.append(s1[i])
                        elif(s1[i].count('1')==1):
                                s1_gp2.append(s1[i])
                        elif(s1[i].count('1')==2):
                                s1_gp3.append(s1[i])

                s1_gp=[]
                s1_gp.append(s1_gp1); s1_gp.append(s1_gp2); s1_gp.append(s1_gp3)

                '''step 2 is started
                        in which the group of step 1 sub-list's element,combining from the
                        nth sublist to the (n+1)th sublist according to bit changing in the
                        two binary number (only bit change to be considered into the grouping)
                        and we will get list (s2_g) in every steps and s2_g append into
                        s2_gp after every sublist changing of step 1 and s2_gp becomes the list of sublist
                        and also the decimal number to be group with the corresponding binary number's decimal number into dk2_gp'''
                s2_gp=[]; dk2_gp=[]
                for i in range(len(s1_gp)-1):
                        s2_g=[]; dk2=[]
                        for j in range(len(s1_gp[i])):
                                for k in range(len(s1_gp[i+1])):
                                        f=0; h=-1
                                        for m in range(2):
                                                if(s1_gp[i][j][m]==s1_gp[i+1][k][m]):
                                                        f=f+1
                                                else:
                                                        h=m
                                        if(f==1 and h>=0):
                                                X=[]; X.append(s1_gp[i][j]); X.append(s1_gp[i+1][k])
                                                Y=list_dict(X)
                                                ky=Y.keys()
                                                for t in ky:
                                                        dk2.append(t)
                                                s=s1_gp[i][j]
                                                ty=s[:h]+'_'+s[h+1:]
                                                s2_g.append(ty)
                        s2_gp.append(s2_g)
                        dk2_gp.append(dk2)

                Y1=[]
                if(len(s2_gp[0])>0 or len(s2_gp[1])>0):
                        for u in range(len(s2_gp)):
                                for w in range(len(s2_gp[u])):
                                        for t in range(2):
                                                if(s2_gp[u][w][t]=='0'):
                                                        if(t==0):
                                                                Y1.append("A'")
                                                        else:
                                                                Y1.append("B'")
                                                elif(s2_gp[u][w][t]=='1'):
                                                        if(t==0):
                                                                Y1.append("A")
                                                        else:
                                                                Y1.append("B")
                else:
                        for v in range(len(B)):
                                if(B[v]==0):
                                        Y1.append("A'B'")
                                elif(B[v]==1):
                                        Y1.append("A'B")
                                elif(B[v]==2):
                                        Y1.append("AB'")
                                else:
                                        Y1.append("AB")
                Y1=sorted(Y1)
                Y=''
                for i in range(len(Y1)):
                        Y=Y+Y1[i]+'+'
                stringOut=Y[:len(Y)-1]
                return(stringOut)

#print(minFunc(4,'(0,1)d(2,3,4,5,6,7,8,9,10,12,13,14)'))
#print(minFunc(4,'(3,6,10,13)d(0,2,5,7,8,9,12)'))
#print(minFunc(2,'(1,2)d(3)'))
#print(minFunc(2,'(1)d(0,3)'))
#print(minFunc(2,'(1,2)d-'))
#print(minFunc(3,'(2,5)d(0,4,6)'))
#print(minFunc(4,'(1,2,4,5,6,10,11,12,13)d-'))
