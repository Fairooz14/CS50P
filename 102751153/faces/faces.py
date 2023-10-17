def main():
    #takes the input----------->
    case = input()
    #the input process to convert into emojies---------->
    conv = emoji(case)
    #the output in emojies
    print(conv)



def emoji(case):
    #happy face expration --------------->
    case1 = case.replace(":)", '🙂')
    #sad face expration ----------------->
    case2 = case1.replace(":(", '🙁')

    return case2

main()