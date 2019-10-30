import discord


client = discord.Client()

#플레잉 게임
@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("happy halloween")
    await client.change_presence(status=discord.Status.online, activity=game)




@client.event
async def on_message(message):
#심영봇DM
    if message.content.startswith("/ds"):
        author = message.guild.get_member(int(message.content[4:22]))
        msg = message.content[23:]
        await  author.send(msg)

#심영봇채널메세지
    if message.content.startswith("/cs"):
        channel = message.content[4:22]
        msg = message.content[23:]
        await client.get_channel(int(channel)).send(msg)



#플레잉 게임 보내기
    if message.content.startswith("어이쿠 이게 지금 뭐하는 거야?"):
        await message.channel.send("조혜련의 태보 다이어트")







#사진 명령어
    if message.content.startswith("행복"):
        await  message.channel.send(file=discord.File("웃음.jpg"))
    if message.content.startswith("웃음"):
        await  message.channel.send(file=discord.File("웃음2.jpg"))
    if message.content.startswith("개소리집어쳐!"):
        await message.channel.send("?????!!!!!!!!!!")
        await  message.channel.send(file=discord.File("simnol.jpg"))
    if message.content.startswith("님!"):
        await message.channel.send("님은 바로 사회주의 낙원을 말하는 것입니다. 여러부우우운!")
        await  message.channel.send(file=discord.File("여러분.gif"))
    if message.content.startswith("정말 위대합니다, 선생!"):
        await message.channel.send("고맙소, 고맙소, 동무들!")
        await  message.channel.send(file=discord.File("고맙소고맙소동무들.png"))
    if message.content.startswith("빠큐"):
        await message.channel.send(":middle_finger: ")
        await  message.channel.send(file=discord.File("fuck.jpeg"))
    if message.content.startswith("아 하필이면 총알이 영좋지 않은곳에 맞았어요"):
        await  message.channel.send(file=discord.File("그건무슨소리오.jpg"))
    if message.content.startswith("이름을 써라"):
        await  message.channel.send(file=discord.File("알겠소.jpg"))
    if message.content.startswith("아이스께끼 이정재"):
        await  message.channel.send(file=discord.File("에엫따.jpg"))
    if message.content.startswith("여기있었구만 심영이"):
        await  message.channel.send(file=discord.File("놀람.jpg"))
    if message.content.startswith("이봐 심영이"):
        await  message.channel.send(file=discord.File("예.jpg"))
    if message.content.startswith("넌 고자야"):
        await  message.channel.send(file=discord.File("이게무슨소리.jpg"))
    if message.content.startswith("폭☆8"):
        await  message.channel.send(file=discord.File("폭8.gif"))
    if message.content.startswith("함께 폭사하자"):
        await  message.channel.send(file=discord.File("ㅈ폭8.gif"))


#메세지 수정
    if message.content.startswith("태보해"):
        feedback = await message.channel.send("@(^0 ^)==@")
        await feedback.edit(content="@==(^ 0^)@")
        await feedback.edit(content="@(^0 ^)==@")
        await feedback.edit(content="@==(^ 0^)@")



#대화봇
    if message.content.startswith("선생은 앞으로 아이를 가질 수 없습니다"):
        await message.channel.send("뭐요? 이보시오! 이보시오! 의사양반!")
    if message.content.startswith("전화는 해로우니 푹 쉬세요"):
        await message.channel.send("뭐라고? 전화가 없다고?")
    if message.content.startswith("곶!"):
        await message.channel.send("내가 고자라니...내가...내가! 고자라니!!")
    if message.content.startswith("당신 심영이란 배우 맞소?"):
        await message.channel.send("그렇소")
    if message.content.startswith("안된다고 했잖소!"):
        await message.channel.send("이 반동노무 쉐키들")
    if message.content.startswith("그러게 왜 공산당인가 뭔가를 해서 이 모양이냐"):
        await message.channel.send("아유..어서요 어머니")
    if message.content.startswith("나라에 큰 죄를 지은 사람입니다"):
        await message.channel.send("왜 들이러시오 나한테 내가 무슨죄를 지엇다고")
    if message.content.startswith("할거야!안할거야!"):
        await message.channel.send("안하겠소..닷씨는 안하겠소")
    if message.content.startswith("야이 빨갱이새끼야!"):
        await message.channel.send("으어어어어어")
    if message.content.startswith("다음에 걸리면 그땐 진짜로 죽을줄 알아 알겠어?"):
        await message.channel.send("으아아하하하하하하핳")
    if message.content.startswith("상태"):
        await message.channel.send("온라인")
    if message.content.startswith("선동하살법!"):
        await message.channel.send("단죄하살법! 불알치기!")
    if message.content.startswith("나 김두한이다"):
        await message.channel.send("반동이다! 전위대!전위대!")
    if message.content.startswith("흠 터레스팅"):
        await message.channel.send(":thinking:")
    if message.content.startswith("폭8전야"):
        await message.channel.send("https://www.youtube.com/watch?v=ZhHmbVlicLE&t=232s")
    if message.content.startswith("키보드"):
        await message.channel.send("|| ` || || 1 || ||2|| ||3|| ||4|| ||5|| ||6|| ||7|| ||8|| ||9|| ||0|| || - || || = || ||← B A S P||"
                                   "\n||T A B|| ||Q|| ||W|| ||E|| ||R|| ||T|| ||Y|| ||U|| || I || ||O|| ||P|| || [ || || ] || || { || || } ||"
                                   "\n||C A P S|| ||A|| ||S|| ||D|| ||F|| ||G|| ||H|| || J || ||K|| ||L|| || ; || || ' || ||E N T E R||"
                                   "\n||S H I F T|| ||Z|| ||X|| ||C|| ||V|| ||B|| ||N|| ||M|| || , || || . || || / || ||S H I F T|| "
                                   "\n||CTRL||||FN||||田||||AL||||SPACEBAR||||AL||||CT||||LE||||UD||||CTRI||")
    if message.content.startswith("무지개"):
        await message.channel.send("```diff"
                                   "\n-red"
                                   "\n```"
                                   "\n```css"
                                   "\n[orange]"
                                   "\n```"
                                   "\n```fix"
                                   "\nyellow"
                                   "\n```"
                                   "\n```css"
                                   "\ngreen"
                                   "\n```"
                                   "\n```css"
                                   "\n.blue"
                                   "\n```")
    if message.content.startswith("체스"):
        await message.channel.send("♖♘♗♔♕♗♘♖"
                                   "\n♙♙♙♙♙♙♙♙"
                                   "\n                "
                                   "\n                "
                                   "\n                "
                                   "\n♟♟♟♟♟♟♟♟"
                                   "\n♜♞♝♛♚♞♝♜")
    if message.content.startswith("초대링크"):
        await message.channel.send("https://discordapp.com/oauth2/authorize?client_id=629142970674839583&scope=bot")
    if message.content.startswith("공짜 배그"):
        await message.channel.send("컴사양도낮고 돈도 없는데 배그가 하고싶다고요? 지금바로시작하세요!"
                                   "\n http://zombsroyale.io/")


#할로윈
    if message.content.startswith("트릭 오어 트릿"):
        await message.channel.send(":candy: :lollipop:")
    if message.content.startswith("잭오랜턴"):
        await message.channel.send("본인 심영 잭오랜턴이라구요!")
        await  message.channel.send(file=discord.File("jackosim.png"))
    if message.content.startswith("아주 무서운 귀신"):
        await message.channel.send("아주 무서운 해골과 귀신임"
                                   "\n:skull: :ghost:"
                                   "\n암튼 무서움")
    if message.content.startswith("아주 무서운 글"):
        await message.channel.send("이 편지는 영국에서 최초로 시작되어 일년에 한 바퀴 돌면서 받는 사람에게 행운을 주었고 지금은 당신에게로 옮겨진 이 편지는 4일 안에 당신 곁을 떠나야 합니다. "
                                   "이 편지를 포함해서 7통을 행운이 필요한 사람에게 보내 주셔야 합니다. 복사를 해도 좋습니다. 혹 미신이라 하실지 모르지만 사실입니다. "
                                   "영국에서 HGXWCH이라는 사람은 1930년에 이 편지를 받았습니다. 그는 비서에게 복사해서 보내라고 했습니다. 며칠 뒤에 복권이 당첨되어 20억을 받았습니다. "
                                   "어떤 이는 이 편지를 받았으나 96시간 이내 자신의 손에서 떠나야 한다는 사실을 잊었습니다. 그는 곧 사직되었습니다. 나중에야 이 사실을 알고 7통의 편지를 보냈는데 "
                                   "다시 좋은 직장을 얻었습니다. 미국의 케네디 대통령은 이 편지를 받았지만 그냥 버렸습니다. 결국 9일 후 그는 암살 당했습니다. 기억해 주세요. "
                                   "이 편지를 보내면 7년의 행운이 있을 것이고 그렇지 않으면 3년의 불행이 있을 것입니다. 그리고 이 편지를 버리거나 낙서를 해서는 절대로 안됩니다. 7통입니다. 이 편지를 받은 사람은 행운이 깃들 것입니다. "
                                   "힘들겠지만 좋은게 좋다고 생각하세요. 7년의 행운을 빌면서..")
    if message.content.startswith("halloween"):
        await message.channel.send("happy halloween")



    #히든
    if message.content.startswith("you are not simyoung you are Van Darkholme"):
        await message.channel.send("i'm van i'm artist l make a fantasy a DEEP♂ DARK♂ FANTASY♂")
    #도움말
    if message.content.startswith("$help"):
        await message.channel.send("```-심영봇 명령어-"
                                   "\n--------------할로윈--------------"
                                   "\n1. 트릭 오어 트릿"
                                   "\n2. 잭오랜턴"
                                   "\n3. 아주 무서운 귀신"
                                   "\n4. 아주 무서운 글"
                                   "\n5. halloween"
                                   "\n--------------명령어--------------"
                                   "\n1. 정말 위대합니다, 선생!  (사진)"
                                   "\n2. 아 하필이면 총알이 영좋지 않은곳에 맞았어요  (사진)"
                                   "\n3. 선생은 앞으로 아이를 가질 수 없습니다"
                                   "\n4. 전화는 해로우니 푹 쉬세요"
                                   "\n5. 곶!"
                                   "\n6. 당신 심영이란 배우 맞소? "
                                   "\n7. 아이스께끼 이정재  (사진)"
                                   "\n8. 안된다고 했잖소!"
                                   "\n9. 그러게 왜 공산당인가 뭔가를 해서 이 모양이냐"
                                   "\n10. 여기있었구만 심영이  (사진)"
                                   "\n11. 나라에 큰 죄를 지은 사람입니다"
                                   "\n12. 이봐 심영이  (사진)"
                                   "\n13. 할거야!안할거야!"
                                   "\n14. 이름을 써라  (사진)"
                                   "\n15. 야이 빨갱이새끼야!"
                                   "\n16. 다음에 걸리면 그땐 진짜로 죽을줄 알아 알겠어?"
                                   "\n17. 상태"
                                   "\n18. 선동하살법!"
                                   "\n19. 나 김두한이다"
                                   "\n20. 흠 터레스팅"
                                   "\n21. 폭8전야"
                                   "\n22. 행복  (사진)"
                                   "\n23. 웃음  (사진)"
                                   "\n24. 개소리집어쳐!  (사진)"
                                   "\n25. 님!  (사진)"
                                   "\n26. 어이쿠 이게 지금 뭐하는 거야?"
                                   "\n27. 빠큐  (사진)"
                                   "\n28. 넌 고자야"
                                   "\n29. 폭☆8"
                                   "\n30. 태보해"
                                   "\n31. 키보드"
                                   "\n32. 무지개"
                                   "\n33. 함께 폭사하자  (사진)"
                                   "\n34. 체스"
                                   "\n35. 초대링크"
                                   "\n36. 공짜 배그"
                                   "\n"
                                   "\n심영봇 버전-Halloween     업데이트 내용-할로윈 이벤트 명령어 추가```"
                                   "\n``개발자-보리차, 버그나 추가사항이 있으면 개인 DM(보리차#2300)으로 보내주세요``")




#토큰
client.run("NjI5MTQyOTcwNjc0ODM5NTgz.XbmK1Q.KSlpushtE_w5fNsq9wfEyC90tNk")
