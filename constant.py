import discord


OFFICIAL_IMAGE = "https://pbs.twimg.com/profile_images/1853287937284489216/VcKq8D5I_400x400.jpg"

PERMITTED_USERS = ['<@568179896459722753>', '<@1265258448694542357>']

ME = 568179896459722753

ERROR_RESPONSES = [
    "_magic 🪄... try the command again </hero:1302652188148891690>_",
    "_ghost came into the way 👻... try the command again </hero:1302652188148891690>_",
    "_ uf! high traffic  🚦... try the command again </hero:1302652188148891690>_",
    "_ is this your parcel?  📦... try the command again </hero:1302652188148891690>_"
]

CHARACTER = {
    "Spider": {
        "message": "Christmas, a day to give... but I'm still the greatest gift here.",
        "image": "https://cdn.discordapp.com/attachments/1199253624350576692/1319258567534186536/Portrait_Spider.png"
                 "?ex=67654ec9&is=6763fd49&hm=e7e832db6fd8d9915360bc960c973d16c194b9615d7e794e2b9232c449f56288&",
        "color": discord.Color.from_rgb(176, 114, 225)
    },
    "Sonar": {
        "message": "Merry Christmas, FinFriends. While the tides carry joy to many today, my homeland still drifts…"
                   " waiting to be reborn. But you’re here. And every wave we ride together brings us closer to"
                   " that dream. Thank you.",
        "image": "https://cdn.discordapp.com/attachments/1199253624350576692/1319258282329772074/Portrait_Sonar.png"
                 "?ex=67654e85&is=6763fd05&hm=4df643a7c106f63c211c215faa5dbf9f47f965fb5ec7cbcbaf35c9232472f6ad&",
        "color": discord.Color.from_rgb(106, 143, 225)
    },
    "Kismet": {
        "message": "Gifts are but fleeting; connection is eternal. Cherish this stillness while it lasts.",
        "image": "https://cdn.discordapp.com/attachments/1199253624350576692/1319257024038436884/Portrait_Kismet.png"
                 "?ex=67654d59&is=6763fbd9&hm=311f1d0b49d13eaef69f57ba9cafcc7cf2486a32d9a573d794b57cedd6b92ae8&",
        "color": discord.Color.from_rgb(88, 241, 152)
    },
    "Broker": {
        "message": "Happy holidays, everyone. I'm no Santa, but I do deliver—fireworks, wins, and a little bit of"
                   " chaos. Let’s light up the day, shall we?",
        "image": "https://cdn.discordapp.com/attachments/1199253624350576692/1319254443182522439/Portrait_Broker.png"
                 "?ex=67654af1&is=6763f971&hm=403765ba7693eca1e5add7fa28ddb2e58954476d5e6da972d80d3f8a785d76c3&",
        "color": discord.Color.from_rgb(198, 39, 230)
    },
    "Axon": {
        "message": "Who needs snowflakes when you've got the sound of electric guitars in the air, huh? Let’s"
                   " make this Christmas a holiday to remember, my friends. Merry Rockmas to you all!",
        "image": "https://cdn.discordapp.com/attachments/1199253624350576692/1319252601019174952/Portrait_Axon.png"
                 "?ex=6765493a&is=6763f7ba&hm=888aa0201d8426941cc28043f4b858357c6e52cc4afc315c40cc6541fa241ae2&",
        "color": discord.Color.from_rgb(130, 9, 64)
    },
    "Nitro": {
        "message": "I hope you’re ready to ride because I’m bringing the cheer and the gear. Let’s make this"
                   " Christmas a record-breaking lap—Chug-Chug and I are already in overdrive!",
        "image": "https://cdn.discordapp.com/attachments/1199253624350576692/1319257380072067122/Portrait_Nitro.png"
                 "?ex=67654dae&is=6763fc2e&hm=29f5a0c23e51716f842872c31f25f18ab02c6f65f258dde0dce3e5211e6b4546&",
        "color": discord.Color.from_rgb(239, 28, 98)
    },
    "Hollowpoint": {
        "message": "Another year, another battle. But hey, if we survive this one, maybe we'll get some downtime."
                   " Merry Christmas. Keep your heads on straight!",
        "image": "https://cdn.discordapp.com/attachments/1199253624350576692/1319256571816972299/Portrait_Hollowpoint"
                 ".png?ex=67654ced&is=6763fb6d&hm=b04f7380dafc9ca51614a5045920ad97691de05e406bd8fdda8e876e62297ef9&",
        "color": discord.Color.from_rgb(228, 218, 50)
    },
    "Corona": {
        "message": "Huh. Christmas. Back in my day, we didn't have time for holiday cheer. Just fight, eat, sleep,"
                   " repeat. But if y'all need some holiday spirit, I'm here for the ride.",
        "image": "https://cdn.discordapp.com/attachments/1199253624350576692/1319256279524311090/Portrait_Corona.png"
                 "?ex=67654ca7&is=6763fb27&hm=e4851b464b6c0d6646291dcc501cc81de4e0514bd7849fbdc95dc90b8a635d2d&",
         "color": discord.Color.from_rgb(236, 137, 60)
    },
    "Zephyr": {
        "message": "Merry Christmas, I guess. You all can keep your presents. I’ll settle for another kill count.",
        "image": "https://cdn.discordapp.com/attachments/1199253624350576692/1319258762070196254/Portrait_Zephyr.png"
                 "?ex=67654ef7&is=6763fd77&hm=1335bcd2c16cae1847f310e93669666db8e6677fbc092bcd233b17095bb4a1f7&",
        "color": discord.Color.from_rgb(39, 230, 211)
    },
    "Serket": {
        "message": "On this day of humble festivities, I grant you all a gift—the privilege of basking in the"
                   " presence of a true goddess. May your fleeting lives be filled with a hint of glory before"
                   " the inevitable sands of time claim you.",
        "image": "https://cdn.discordapp.com/attachments/1199253624350576692/1319257787427192833/Portrait_Serket.png"
                 "?ex=67654e0f&is=6763fc8f&hm=aa8c12b1a7c0c6ca705c01ef2040d88dd2a9912a834a2898f2f4c7c2ef2bb1d5&",
        "color": discord.Color.from_rgb(230, 39, 83)
    },
    "Jaguar": {
        "message": "This season, I offer you no gifts. Only this: survival. May your instincts be sharp, your"
                   " senses keen, and may you never be the prey.",
        "image": "https://cdn.discordapp.com/attachments/1199253624350576692/1319256818995822592/Portrait_Jaguar."
                 "png?ex=67654d28&is=6763fba8&hm=dd0aa60e1ede40690c877d130c2bef0a938abb2c124d39f7b48ffa7bca0d332f&",
        "color": discord.Color.from_rgb(39, 206, 230)
    },
    "Pathojen": {
        "message": "Let’s see what happens when we inject a little bit of festive cheer into our regular data"
                   " collection. Is there a difference between joy and madness? Perhaps we’ll find out this season.",
        "image": "https://cdn.discordapp.com/attachments/1199253624350576692/1319257571286061117/Portrait_Pathojen.png"
                 "?ex=67654ddb&is=6763fc5b&hm=c98fa82b567ae17ca8e77a6e5b648aa6de2559086bade5cdab86db8d2c8fcfb8&",
        "color": discord.Color.from_rgb(199, 54, 230)
    }
}