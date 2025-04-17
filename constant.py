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
        "easter_response": "This lovely Easter, I shall give you the most fun surprise of them all... me!",
        "sticker": "https://media.discordapp.net/attachments/1322857039847882853/1362413082709721281/Sticker_Spider.gif?ex=68024d8f&is=6800fc0f&hm=7303b089c4f4c7c4c39aac0ae9e8ffde7da3de984729affdc7eaf124df9039b9&=&width=256&height=256",
        "image": "https://media.discordapp.net/attachments/1318864196137648128/1362372361239793744/Portrait_Spider.png?ex=680227a2&is=6800d622&hm=0f02848f34689d00d099e396fbbcb31833f7c00e6e0926e58282740456d5d888&=&format=webp&quality=lossless&width=1222&height=1178",
        "color": discord.Color.from_rgb(176, 114, 225)
    },
    "Sonar": {
        "message": "Merry Christmas, FinFriends. While the tides carry joy to many today, my homeland still drifts…"
                   " waiting to be reborn. But you’re here. And every wave we ride together brings us closer to"
                   " that dream. Thank you.",
        "easter_response": "Welcome to my Easter Egg Giveaway! Oh wait... this is not my stream chat. Whoops! Greeting you all from the depths of our waters a nice Easter! Or should I call it, Sea-Easter season!",
        "sticker": "https://media.discordapp.net/attachments/1322857039847882853/1362413103882436658/Sticker_Sonar.gif?ex=68024d94&is=6800fc14&hm=9237713ff7c0901606c7cdfea385380b3198d1180fa87c8124a5d5008749be38&=&width=256&height=256",
        "image": "https://media.discordapp.net/attachments/1318864196137648128/1362372360677883964/Portrait_Sonar.png?ex=680227a2&is=6800d622&hm=e746dd5a3ea216f9087e5423ff8608f09822829867b93346e67de46d3362dd35&=&format=webp&quality=lossless&width=1646&height=1536",
        "color": discord.Color.from_rgb(106, 143, 225)
    },
    "Kismet": {
        "message": "Gifts are but fleeting; connection is eternal. Cherish this stillness while it lasts.",
        "easter_response": "Easter values family, mankind and tradition. Cherish them with your loved ones.",
        "sticker": "https://media.discordapp.net/attachments/1322857039847882853/1362413466270437578/Sticker_Kismet.gif?ex=68024dea&is=6800fc6a&hm=b19e308d530b488cce6dd2ba35e4630c715e8f1eaa6505b71d522ef7f1596539&=&width=256&height=256",
        "image": "https://media.discordapp.net/attachments/1318864196137648128/1362372326385258537/Portrait_Kismet.png?ex=6802279a&is=6800d61a&hm=250a03a762741e4d6771a9a81a5f41abac38c8fa8316bf0252269f0d9ffac08d&=&format=webp&quality=lossless&width=1256&height=1278",
        "color": discord.Color.from_rgb(88, 241, 152)
    },
    "Broker": {
        "message": "Happy holidays, everyone. I'm no Santa, but I do deliver—fireworks, wins, and a little bit of"
                   " chaos. Let’s light up the day, shall we?",
        "easter_response": "For this Easter, I will deliver you the greatest gift of all. The Golden Egg! Don't drop it like how I do it with my bombs, and don't put all your eggs in one basket!",
        "sticker": "https://media.discordapp.net/attachments/1322857039847882853/1362413590476488755/Sticker_Broker.gif?ex=68024e08&is=6800fc88&hm=4f3f9e5290ee8ffed6fdc616cc14fd885f60315ce96b893061bbc45dc71e3d39&=&width=256&height=256",
        "image": "https://media.discordapp.net/attachments/1318864196137648128/1362372325013585972/Portrait_Broker.png?ex=68022799&is=6800d619&hm=a884104714386e233b3ccad275d802ce1ae133c32d01956b1ccae592bcac4cbc&=&format=webp&quality=lossless&width=1326&height=1110",
        "color": discord.Color.from_rgb(198, 39, 230)
    },
    "Axon": {
        "message": "Who needs snowflakes when you've got the sound of electric guitars in the air, huh? Let’s"
                   " make this Christmas a holiday to remember, my friends. Merry Rockmas to you all!",
        "easter_response": "Eggs-citing times calls for eggs-citing starstudded moments! They got me pumping and jumping around like the Easter bunny! Have a rocking Easter to you all!",
        "sticker": "https://media.discordapp.net/attachments/1322857039847882853/1362413608298086591/Sticker_Axon.gif?ex=68024e0c&is=6800fc8c&hm=dc00a10713e8aa1aca90008bb53e0617b64cb9bd48be4240b0ead02b4b542bcb&=&width=256&height=256",
        "image": "https://media.discordapp.net/attachments/1318864196137648128/1362372324665331732/Portrait_Axon.png?ex=68022799&is=6800d619&hm=d1f523e9c803af3d7b3ab55868a4eeeff9f8d0c698fa17cee149cc84abd9aea4&=&format=webp&quality=lossless&width=1462&height=1018",
        "color": discord.Color.from_rgb(130, 9, 64)
    },
    "Nitro": {
        "message": "I hope you’re ready to ride because I’m bringing the cheer and the gear. Let’s make this"
                   " Christmas a record-breaking lap—Chug-Chug and I are already in overdrive!",
        "easter_response": "Hey! Are you ready to go Easter Egg hunting? Me and Chug Chug are all revved up to make this season, extra eggstraordinary!",
        "sticker": "https://media.discordapp.net/attachments/1322857039847882853/1362413445609160997/Sticker_Nitro.gif?ex=68024de5&is=6800fc65&hm=6934ee264947f39bd80ae5dfc3c5e3e65c760f55699df342507b64a0a7a4b0a1&=&width=256&height=256",
        "image": "https://media.discordapp.net/attachments/1318864196137648128/1362372359348162721/Portrait_Nitro.png?ex=680227a2&is=6800d622&hm=7aeda1fe7b89a59f3a7ebfba740603dae2db003b04c8daf25fd0514449523876&=&format=webp&quality=lossless&width=1244&height=1264",
        "color": discord.Color.from_rgb(239, 28, 98)
    },
    "Hollowpoint": {
        "message": "Another year, another battle. But hey, if we survive this one, maybe we'll get some downtime."
                   " Merry Christmas. Keep your heads on straight!",
        "easter_response": "My Meteora spotted these eggs from miles away. Hope you like them! Take a breather and and enjoy them for a bit, before we go back into the fight! ",
        "sticker": "https://media.discordapp.net/attachments/1322857039847882853/1362413533609988310/Sticker_Hollowpoint.gif?ex=68024dfa&is=6800fc7a&hm=22aaa7933e76f9910f567b9ffa8195e3d980e75becce9b3085eb9522929530ff&=&width=256&height=256",
        "image": "https://media.discordapp.net/attachments/1318864196137648128/1362372325802246194/Portrait_Hollowpoint.png?ex=6802279a&is=6800d61a&hm=a6ed9a346a83b3e35146e6c5456a67ac61f0e264a7ea55575fb6dd830efb5ec6&=&format=webp&quality=lossless&width=1200&height=1072",
        "color": discord.Color.from_rgb(228, 218, 50)
    },
    "Corona": {
        "message": "Huh. Christmas. Back in my day, we didn't have time for holiday cheer. Just fight, eat, sleep,"
                   " repeat. But if y'all need some holiday spirit, I'm here for the ride.",
        "easter_response": "Back in the old days, we barely have Easter. Guess times have changed. If you all need a kickstart your season, I can light it up for you anytime!",
        "sticker": "https://media.discordapp.net/attachments/1322857039847882853/1362413560424304781/Sticker_Corona.gif?ex=68024e01&is=6800fc81&hm=95fc1634ceb530e16a7c6d7943514836d4013a6e747497fe8609897f98dfeef5&=&width=256&height=256",
        "image": "https://media.discordapp.net/attachments/1318864196137648128/1362372325445472399/Portrait_Corona.png?ex=6802279a&is=6800d61a&hm=94d4cb9ad6659e7014b3c05d8de30010f25faca1895f5395e93d2a9e8b2aaf5f&=&format=webp&quality=lossless&width=1216&height=1082",
         "color": discord.Color.from_rgb(236, 137, 60)
    },
    "Zephyr": {
        "message": "Merry Christmas, I guess. You all can keep your presents. I’ll settle for another kill count.",
        "easter_response": "You all can run, but you can't hide all your easter eggs from me.",
        "sticker": "https://media.discordapp.net/attachments/1322857039847882853/1362413061025304667/Sticker_Zephyr.gif?ex=68024d8a&is=6800fc0a&hm=6a4c1d63fa3f611e148c3d7013e26e6fd1efb48f80ce748fe1a328aff3e7d967&=&width=256&height=256",
        "image": "https://media.discordapp.net/attachments/1318864196137648128/1362372361613217862/Portrait_Zephyr.png?ex=680227a2&is=6800d622&hm=ef04f4083cc5f689c28f4a8089ed9dd94915ffa3e240865225e14c34785d8975&=&format=webp&quality=lossless&width=1410&height=1162",
        "color": discord.Color.from_rgb(39, 230, 211)
    },
    "Serket": {
        "message": "On this day of humble festivities, I grant you all a gift—the privilege of basking in the"
                   " presence of a true goddess. May your fleeting lives be filled with a hint of glory before"
                   " the inevitable sands of time claim you.",
        "easter_response": "In times of solemnity, all of you are invited to the greatest feast of them all - a celebration with the presence of a true goddess. May you stay true to your faith, both the first and the last, and those who come after, enjoy your reward!",
        "sticker": "https://media.discordapp.net/attachments/1322857039847882853/1362413137504108555/Sticker_Serket.gif?ex=68024d9c&is=6800fc1c&hm=8089b355827c6f26a671e9d81a0424857cf80e9b5e750fd7931d91a2b5045aee&=&width=256&height=256",
        "image": "https://media.discordapp.net/attachments/1318864196137648128/1362372359998148770/Portrait_Serket.png?ex=680227a2&is=6800d622&hm=f36bbc5fa77c0f9f8f49fe1769ef92d78532c5e420e145d04693275cee2ee145&=&format=webp&quality=lossless&width=1074&height=1020",
        "color": discord.Color.from_rgb(230, 39, 83)
    },
    "Jaguar": {
        "message": "This season, I offer you no gifts. Only this: survival. May your instincts be sharp, your"
                   " senses keen, and may you never be the prey.",
        "easter_response": "We have hunted down the wildest rabbits in the grasslands, and the richest eggs in nests no one can reach. May you have the mightiest Easter for you all!",
        "sticker": "https://media.discordapp.net/attachments/1322857039847882853/1362413496930668704/Sticker_Jaguar.gif?ex=68024df2&is=6800fc72&hm=43bb9b989ef800d872c00650029cf71514d649538d106504ddbc895a85ff4df3&=&width=256&height=256",
        "image": "https://media.discordapp.net/attachments/1318864196137648128/1362372326091390976/Portrait_Jaguar.png?ex=6802279a&is=6800d61a&hm=90c730c61d379847b2295275f16f91614d6287f6c53d46c1481bed85d0599cea&=&format=webp&quality=lossless&width=1052&height=958",
        "color": discord.Color.from_rgb(39, 206, 230)
    },
    "Pathojen": {
        "message": "Let’s see what happens when we inject a little bit of festive cheer into our regular data"
                   " collection. Is there a difference between joy and madness? Perhaps we’ll find out this season.",
        "easter_response": "I'll let you in an Eggs-xperiment! We mixed these eggs with the finest shrooms I could find. Treat it like your ordinary easter egg, but with a little bit of surprising twist. Come back to me if you feel any side effects!",
        "sticker": "https://media.discordapp.net/attachments/1322857039847882853/1362413426512756827/Sticker_Pathojen.gif?ex=68024de1&is=6800fc61&hm=b4e4216878b44ef8b7cb81a42fa8475c0bd52360d74b5d36ba4795967df3e3b0&=&width=256&height=256",
        "image": "https://media.discordapp.net/attachments/1318864196137648128/1362372359662862466/Portrait_Pathojen.png?ex=680227a2&is=6800d622&hm=92328564fcea38f2520ac66446b90187ad3a332a1945d600628aa8611e5bd2e3&=&format=webp&quality=lossless&width=1338&height=1186",
        "color": discord.Color.from_rgb(199, 54, 230)
    },
    "Chum": {
        "message": "",
        "easter_response": "I was supposed to give you an egg, but Chomper ate it all! Oh well! Happy Easter!",
        "sticker": "",
        "image": "https://media.discordapp.net/attachments/1318864196137648128/1362374915575119882/portrait_chum.png?ex=68022a03&is=6800d883&hm=1519b620b190ea8441151196b78211c7f9fe87a558dc30bdca56eb1104f1b1ce&=&format=webp&quality=lossless&width=1122&height=1058",
        "color": discord.Color.from_rgb(199, 54, 230)
    },
    "?": {
        "message": "",
        "easter_response": "Take it, but understand the weight of death—for only through the depth of sacrifice can we truly rejoice in the power of resurrection. Wishing you a blessed and hope-filled Easter.",
        "sticker": "",
        "image": "https://media.discordapp.net/attachments/1318864196137648128/1362378059789107382/suspicious.jpeg?ex=68022cf1&is=6800db71&hm=271a81c0c38b8a4f244def635cf3f54dda0277ed41da343b3afd063ed2764557&=&format=webp&width=836&height=932",
        "color": discord.Color.from_rgb(199, 54, 230)
    },
}