sajan = {}

def saojak():
    a = input("성적을 기록하실 것입니까? (그렇다면 g)(아니면 성적기록을 조회하시겠습니까?(그렇다면 j))")
    if a == 'j':
        jb = str(input("어떤 항목을 조회하실 것 입니까 예)hogildo "))
        try:
            print(sajan[jb])
            saojak()
        except KeyError as e:
            print("이 키는 없는 키입니다")
            saojak()
    elif a == 'g':
        gb = str(input("어떤 키를 만들것입니까?"))
        gbe = str(input("그 키 안에 성적을 기록해주세요"))
        sajan[gb] = gbe
        saojak()

saojak()
        
