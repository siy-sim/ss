# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.
define d = Character('도리언 그레이', color="#2c694b")
define h = Character('헨리 경', color="#2c694b")
define b = Character('바질 홀워드', color="#2c694b")
define s = Character('시빌 베인', color="#2c694b")
define j = Character('제임스 베인', color="#2c694b")

image ch bb = im.Scale("ch bb.png", 400, 1000)
image ch hh = im.Scale("ch hh.png", 600, 1000)

image bg hs = im.Scale("bg hs.png", 1920, 1080) #화실
#image bg gw = im.Scale("bg gw.png", 1920, 1080) #공원
#image bg kg = im.Scale("bg kg.png", 1920, 1080) #극장
#image bg room = im.Scale("bg room.png", 1920, 1080) #다락방




#screen love_ber():
    ##text "호감 [love]"


# 여기에서부터 게임이 시작합니다.
label start:

    #scene black with fade
    #show screen love_ber
    scene black with fade
    scene bg hs

    show ch hh #at right with move

    h "가장 멋진 작품이야, 배질."

    h "네가 그린 작품 가운데 단연 최고야"

    h "이 작품을 내년엔 반드시 그로브너 갤러리에 보내야해."

    h "왕립 미술원은 규모가 너무 크고 크고 세속적이야, 사람도 어찌나 많던지... 끔찍해"

    h "그로브너 갤러리가 딱 안성 맞춤이야. 거기 밖에 없다고"

    hide ch hh

    show ch bb
    
    b "아무데도 안 보낼 거야"

    b "안 보내. 어디가 됐든 안 보내."

    hide ch bb

    show ch hh

    h "어디에도 안 보낸다고? 이봐, 그러는 이유가 뭔가?"

    h "무슨 특별한 이유가 있는거야?"

    h "참으로 자네 같은 화가들은 알다가도 모르겠군"

    h "명성을 얻으려고 기를 쓰다가 일단 이름을 얻으면 그걸 내던지고 싶어 하니 바보같은 짓이야"

    h "사람들 입에 오르내리는 것 보다 더 나쁜게 뭔 줄 아나?"

    h "사람들이 거론조차 하지 않는다는 거야"

    show ch hh at right with move

    h "이 초상화 한점으로 넌 영국의 어느 젊은이들보다 뛰어나다는 것을 보여줄 수 있어."

    h "늙은이들은 부러움과 질시로 안절부절 못할테지. {w} 감정을 표출할 능력이나 있을지 모르겠지만"

    hide ch hh

    show ch bb

    b "알아. {w} 너는 나를 비웃고도 남을 친구지."

    b "하지만 전시하지 않을거야. 이 그림속에 나 자신을 너무 많이 집어 넣어서 그래"
   
    hide ch bb

    show ch hh 

    h "{size=+5}너 자신을 너무 많이 투사했다!{/size}"
    h "이거 원. 배질."
    h "그 얼굴로 상아의 장미잎으로 만든 것 같은 이 젊은 아도니스 사이에 비슷한 구석이 어디있어?" ##

    h "하나도 없어 배질."
    h "그 초상화 인물은 나르키소스 같은 젊은이지만.. {w} 너는..."
    h "{size=+2}그래,{/size} 물론 너한테는 지적인 표정을 읽을 수가 있지."

    h "근데 그것뿐이야."

    h "또 문제는 지적인 표정이 시작되면 {size=+5}아름다움 {/size}"
    h "진정한 아름다움이 끝나고 말아."

    h "지성은 본질적으로 과장된 표정으로 나타나"
    h "그래서 어떤 얼굴에서든 그 얼굴에 조화를 무너뜨리는 법이지"

    h "네가 이름도 말해주지도 않는 그 젊은이의 초상이 난 정말 마음에들어"
    h "생각하는 기미가 전혀 없잖아"
    h "그 친구는 머리를 쓰지 않는 아름다운 젊은이야"

    h "겨울에 바라볼 꽃이 없어도 늘 이곳에 있을테고, {w} 우리가 우리의 지성을 서늘하게 하고 싶은 여름에도 이곳에 그대로 있을테지."
    h "괜히 우쭐해하지마, 배질"
    h "넌 저 젊은이와 하나도 안 닮았어"
    h "쌤이 수정한 내용이야 이게!"
    hide ch hh

    return
