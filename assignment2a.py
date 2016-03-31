def solve (nug):
    solutionFound = False
    for nugSix in range(0,nug + 1):
        for nugNine in range(0, nug - nugSix + 1):
                nugTwenty = (nug - 6 * nugSix - 9 * nugNine)/20
                if (nugTwenty > 0):
                    totNug = 6 * nugSix + 9 * nugNine + 20 * nugTwenty
                if totNug == nug:
                    print 'nugSix' + str(nugSix)
                    print 'nugNine' + str(nugNine)
                    print 'nugTwenty' + str(nugTwenty)
                    solutionFound = True
        if not solutionFound: print 'There is no solution'


        
