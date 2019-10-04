import discord


client = discord.Client()

#플레잉 게임
@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("조혜련의 태보 다이어트")
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




    #히든
    if message.content.startswith("you are not simyoung you are Van Darkholme"):
        await message.channel.send("i'm van i'm artist l make a fantasy a DEEP♂ DARK♂ FANTASY♂")
    #도움말
    if message.content.startswith("!help"):
        await message.channel.send("```-심영봇 명령어-"
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
                                   "\n"
                                   "\n심영봇 버전-2.5     업데이트 내용-명령어 추가```"
                                   "\n``개발자-보리차, 버그나 추가사항이 있으면 개인 DM(보리차#2300)으로 보내주세요``")




#토큰
client.run("NjI5MTQyOTcwNjc0ODM5NTgz.XZVeDA.mV3eYcrpN2b3oP7Qv4vfvkCjeQ8")