sajan = {}#먼저 사전을 할당한다

def saojak():
    a = input("성적을 기록하실 것입니까? (그렇다면 g)(아니면 성적기록을 조회하시겠습니까?(그렇다면 j))")#여기서 성적을 조회할지 성적을 기록할지 정함
    if a == 'j':#조회할 수 있다면 만약 키를 못 찾으면 오류가 나지만 이때를 위해서 try명령어를 써서 혹시 모를 오류의 대비한다.
        jb = str(input("어떤 항목을 조회하실 것 입니까 예)hogildo "))
        try:
            print(sajan[jb])
            saojak()#조회만 하고 끝내진 않을 것 같아서 다시 자기 자신을 호출한다.
        except KeyError as e:
            print("이 키는 없는 키입니다")
            saojak()
    elif a == 'g':
        gb = str(input("어떤 키를 만들것입니까?"))#이부분은 input 을 이용해 해당되는 키와 내용을 적을 수 있게 하였다.
        gbe = str(input("그 키 안에 성적을 기록해주세요"))
        sajan[gb] = gbe
        saojak()

saojak()
        
