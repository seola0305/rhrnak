import discord, asyncio, random #모듈 불러오기
token = "ODcxOTk0NTkwMjA5NjQ2NjMy.YQjaPw.27Ik9rAB94eK-L1GrqtIKY7Fsao" #봇 토큰 설정하기
client = discord.Client() #client 설정하기

@client.event 
async def on_ready(): #봇이 준비되었을때
    print("봇 준비 완료!")
    print(client.user)
    print("안녕하세요!")

@client.event
async def on_message(message): #사용자가 메세지를 입력했을때
    if message.content.startswith("발냥이님"): #만일 사용자가 "사랑해" 라고 입력했을때
        await message.channel.send(random.choice(['알겠다늉','아니다늉','♥','마쟈!','모르겠다냥!']))
    if message.content.startswith("여보야"): #만일 사용자가 "사랑해" 라고 입력했을때
        await message.channel.send(random.choice(['나두','웅','♥','싫어','몰랑']))
    if message.content.startswith("좆냥"): #만일 사용자가 "사랑해" 라고 입력했을때
        await message.channel.send(random.choice(['찌발련아','꺼져','ㅋ','어쩔','ㅗ','시벨롬ㅋ','아ㅋㅋ']))



client.run(token)

